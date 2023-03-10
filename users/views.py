from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from integrations.models import AadhaarCard, Informant
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.core.cache import cache
from twilio.rest import Client
from .serializers import VerifyOTPSerializer
import os

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')

class LoginView(APIView):
    def post(self, request, format=None):
        data = request.data
        
        phone_number = None
        if 'phone_number' in data:
            phone_number = request.data.get('phone_number')
        
        if 'aadhaar_card' in data:
            aadhaar_card = request.data.get('aadhaar_card')
            phone_number = AadhaarCard.objects.get(aadhaar_number=aadhaar_card).phone_number
        
            if not AadhaarCard.objects.get(aadhaar_number=aadhaar_card).is_active:
                return Response({'error': 'account is not active'}, status=status.HTTP_401_UNAUTHORIZED)
            
        otp = generate_otp()
        cache.set(phone_number, otp, timeout=900)
        phone_number = "+91" + phone_number
        
        #uncomment to print it on console for testing: save twilio credits
        print(otp)
        
        #uncomment below line to send OTP via twilio: it is paid after certain free credits
        # send_otp(phone_number, otp)
        data = {'message': 'OTP sent successfully', 'phone_number': phone_number}
        return Response(data, status=status.HTTP_200_OK)

class VerifyOTPView(APIView):
    def post(self, request, format=None):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')
        serializer = VerifyOTPSerializer(data=request.data)
        aadhaar_card = get_object_or_404(AadhaarCard, phone_number=phone_number)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        cached_otp = cache.get(phone_number)
        
        if not cached_otp:
            return Response({'error': 'otp has expired or is invalid'}, status=status.HTTP_400_BAD_REQUEST)
        if otp != cached_otp:
            return Response({'error': 'invalid otp'}, status=status.HTTP_401_UNAUTHORIZED)

        informant= Informant.objects.get_or_create(phone_number=phone_number)

        # Create a user object using the phone number as the username
        user, _ = User.objects.get_or_create(username=phone_number)
        
        # Authenticate the user and get the token
        data = {'token': generate_token(user)}
        
        return Response(data, status=status.HTTP_200_OK)

def generate_otp():

    import random
    return '{:04d}'.format(random.randint(0, 9999))

def send_otp(phone_number, otp):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=f'Your OTP is {otp}',
        from_=TWILIO_PHONE_NUMBER,
        to=phone_number
    )


def generate_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key
