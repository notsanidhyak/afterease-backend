from django.db import models
from django.db import transaction
import random
# Create your models here.

class AadhaarCard(models.Model):
    aadhaar_number = models.CharField(max_length=12, unique=True)
    full_name = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    address_line = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
        
    def __str__(self):
        return str(self.full_name) + str(self.aadhaar_number)

class InformantDeathCertificate(models.Model):
    informant = models.ForeignKey('integrations.Informant', on_delete=models.CASCADE)
    death_certificate = models.ForeignKey('integrations.DeathCertificate', on_delete=models.CASCADE)
    
class Informant(models.Model):
    death_certificates = models.ManyToManyField('integrations.DeathCertificate', through=InformantDeathCertificate)
    phone_number = models.CharField(max_length=10) #adhaar registered

class DeathCertificate(models.Model):
    name = models.CharField(max_length=100)
    date_of_death = models.DateField()
    place_of_death = models.CharField(max_length=100)
    cause_of_death = models.CharField(max_length=100)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    informant_relationship = models.CharField(max_length=100)
    informant_adhaar = models.CharField(max_length=12, unique= False, null=True, blank=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    registration_place = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=20, null=True, blank=True)
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=False)
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved')
    ]
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='Pending')

    def __str__(self):
        return (str(self.name) + str(self.registration_number))
    
    def save(self, *args, **kwargs):
        if not self.registration_number:
            while True:
                new_no = random.randint(1000000, 9999999)
                if not DeathCertificate.objects.filter(registration_number=new_no).exists():
                    self.registration_number = new_no
                    break
            
        if not self.pk:
            informant = None
            informant_death_certificate = None
            informant_phone_number = AadhaarCard.objects.get(aadhaar_number=self.informant_adhaar).phone_number
            # Check if the informant Aadhaar number is provided
            if self.informant_adhaar:
                try:
                    print("informant object being added")
                    informant = Informant.objects.get(phone_number=informant_phone_number)
                except Informant.DoesNotExist:
                    print("Informant getting created of particular adhaar ID")
                    informant = Informant.objects.create(phone_number=informant_phone_number)
                
                print("death certificate getting attached to informant")
                informant_death_certificate = InformantDeathCertificate(informant=informant, death_certificate=self)
            
            # Use a transaction to ensure that all related objects are saved atomically
            with transaction.atomic():
                super().save(*args, **kwargs)
                # save the informant_death_certificate object if it was created
                if informant_death_certificate:
                    informant_death_certificate.save()
            
        else:
            if self.status == 'Approved' and self.pk:
                # Update the pensioner's model status from active to stopped
                try:
                    pensioner = Pensioner.objects.get(adhaar_number=self.aadhaar_number)
                    pensioner.pension_status = 'Stopped'
                    print("Pension Status getting updated from active to stop")
                    pensioner.save()
                except Pensioner.DoesNotExist:
                    pass
                super().save(*args, **kwargs)
            
        
class PANCard(models.Model):
    pan_number = models.CharField(max_length=10, unique=True)
    holder_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=100)
    aadhaar_number = models.CharField(max_length=12, unique=True, null=True, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def __str__(self):
        return (str(self.holder_name) + str(self.pan_number))


class Pensioner(models.Model):
    PPO = models.IntegerField(unique=True)
    pensioner_name = models.CharField(max_length=50)
    pensioner_address = models.CharField(max_length=100)
    pension_amount = models.FloatField()
    bank_name = models.CharField(max_length=50)
    bank_account_number = models.CharField(max_length=20)
    BANK_ACCOUNT_TYPES = [
        ('Savings', 'Savings'),
        ('Current', 'Current'),
    ]
    bank_account_type = models.CharField(max_length=10, choices=BANK_ACCOUNT_TYPES)
    ifsc_code = models.CharField(max_length=15)
    PENSION_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Stopped', 'Stopped')
    ]
    pension_status = models.CharField(max_length=15, choices=PENSION_STATUS_CHOICES, default = 'Active')
    adhaar_number = models.CharField(max_length=12,null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (str(self.pensioner_name)+str(self.PPO))
    
    
class DrivingLicense(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    date_expires = models.DateField()
    adhaar_number = models.CharField(max_length=12,null=True, blank=False)
    is_active = models.BooleanField(default=True)
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class VoterID(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    voter_id_number = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    adhaar_number = models.CharField(max_length=12,null=True, blank=False)
    is_active = models.BooleanField(default=True)
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name