from rest_framework import views, status, permissions
from .models import AadhaarCard, VoterID, DrivingLicense, PANCard, DeathCertificate, Informant, InformantDeathCertificate, Pensioner
from rest_framework.response import Response
from .serializers import DeathCertificateSerializer, InformantDeathCertificateSerializer


#dissolve documents
class DissolveDocuments(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self,request):
        reg_no = request.GET.get('death_registration_number')
        adhaar_no = DeathCertificate.objects.get(registration_number=reg_no).aadhaar_number
        
        resp = {
            "adhaar_card": AadhaarCard.objects.get(aadhaar_number=adhaar_no).is_active,
        }
        try:
            voter_id = VoterID.objects.get(adhaar_number=adhaar_no)
            resp["voter_id"] = voter_id.is_active
        except VoterID.DoesNotExist:
            resp["voter_id"] = None

        try:
            driving_license = DrivingLicense.objects.get(adhaar_number=adhaar_no)
            resp["driving_license"] = driving_license.is_active
        except DrivingLicense.DoesNotExist:
            resp["driving_license"] = None
            
        try:
            pan_card = PANCard.objects.get(aadhaar_number=adhaar_no)
            resp["pan_card"] = pan_card.is_active
        except PANCard.DoesNotExist:
            resp["pan_card"] = None


        return Response(resp, status=status.HTTP_200_OK)
        
    def post(self, request):
        data = request.data
        reg_no = data.get('death_registration_number')
        doc_list = data.get('documents')
        adhaar_no = DeathCertificate.objects.get(registration_number=reg_no).aadhaar_number
        resp = []
        
        if 'adhaar_card' in doc_list:
            resp.append("adhaar_card")
            AadhaarCard.objects.get(aadhaar_number=adhaar_no).update(is_active=False)
            
        if 'voter_id' in doc_list:
            try:
                VoterID.objects.get(adhaar_number=adhaar_no).update(is_active=False)
                resp.append("voterid")
            except:
                pass
        if 'driving_license' in doc_list:
            try:
                DrivingLicense.objects.get(adhaar_number=adhaar_no).update(is_active=False)
                resp.append("driving_license")
            except:
                pass
        if 'pan_card' in doc_list:
            try:
                PANCard.objects.get(aadhaar_number=adhaar_no).update(is_active=False)
                resp.append("pan_card")
            except:
                pass
        return Response(resp, status=status.HTTP_200_OK)
        
#choose death reg number
class InformantDeathCertificateList(views.APIView):
    serializer_class = InformantDeathCertificateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        informant = Informant.objects.get(phone_number=self.request.user.username)
                # Get the queryset of death certificates associated with the informant
        death_certificates = informant.death_certificates.filter(status='Approved')

        # Serialize the queryset using the DeathCertificateSerializer
        serializer = DeathCertificateSerializer(death_certificates, many=True)

        # Return the serialized data as a JSON response
        return Response(serializer.data)
    
class PensionStatus(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        reg_no = request.GET.get('death_registration_number')
        aadhaar_no = DeathCertificate.objects.get(registration_number=reg_no).aadhaar_number
        pension = Pensioner.objects.get(adhaar_number=aadhaar_no)
        resp = {
            "name" :pension.pensioner_name,
            "status" : pension.pension_status,
            "bank_name" : pension.bank_name,
            "PPO_number" : pension.PPO,
            "bank_account_number" : pension.bank_account_number,
            "address" : pension.pensioner_address,
            "amount" : pension.pension_amount,
            "bank_account_type" : pension.bank_account_type,
            "distribution_date" : pension.created_at
        }
        return Response(resp, status=status.HTTP_200_OK)
    
