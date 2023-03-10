from integrations.models import Informant, DeathCertificate, InformantDeathCertificate
from rest_framework import serializers

class InformantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informant
        fields = "__all__"
        
class DeathCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeathCertificate
        fields = ['id', 'registration_number', 'name', 'date_of_death']

class InformantDeathCertificateSerializer(serializers.ModelSerializer):
    death_certificate = DeathCertificateSerializer()

    class Meta:
        model = InformantDeathCertificate
        fields = ['id', 'informant', 'death_certificate']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['informant'] = instance.informant.phone_number
        return ret