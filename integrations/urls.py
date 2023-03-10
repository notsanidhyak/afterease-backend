from .views import *
from django.urls import path

urlpatterns = [
    path('dissolve-doc/', DissolveDocuments.as_view(), name = 'dissolve-doc'),
    path('informant-death-certificate/', InformantDeathCertificateList.as_view(), name = 'informant-death-certificate'),
    path('pension-status/', PensionStatus.as_view(), name = 'pension-status'),
]
