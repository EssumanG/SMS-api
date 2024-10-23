from django.db import models

# Create your models here.
import uuid
import datetime

# Create your models here.
PM = 'Plant Maintenance'
SM = 'Surface Maintenance'
PMC = 'Property Maintenance and Construction'
UG_MAINTENACE = 'Underground Maintenance'
UG_E = 'Underground Electricals'
FINANCE = 'Finance'
GEOlOGY = 'Geology'
EXPLORATION = 'Exploration'
GSSOP = 'GSSOP'
COMMUNITY = 'Community'
HR = 'Human Resource'
PS = 'Purchasing and Supply'
SECURITY = 'Security'
SAFETY = 'Safety'
ENVIRONMENT = 'Environment'
UG_MINING ='Underground Mining'
TS = 'Technical Service'
UG_SERVICE = 'Underground Service'
IT = 'Information Technology'
METALLURGY = 'Metallurgy'



DEPARTMENR_CHOICES = [
    (PM, 'Plant Maintenance'),
    (SM, 'Surface Maintenance'),
    (PMC, 'Property Maintenance and Construction'),
    (UG_MAINTENACE, 'Underground Maintenance'),
    (UG_E, 'Underground Electricals'),
    (FINANCE, 'Finance'),
    (GEOlOGY, 'Geology'),
    (EXPLORATION, 'Exploration'),
    (GSSOP, 'GSSOP'),
    (COMMUNITY, 'Community'),
    (HR, 'Human Resource'),
    (PS, 'Purchasing and Supply'),
    (SECURITY, 'Security'),
    (SAFETY, 'Safety'),
    (ENVIRONMENT, 'Environment'),
    (UG_MINING, 'Underground Mining'),
    (TS, 'Technical Service'),
    (UG_SERVICE, 'Underground Service'),
    (IT, 'Information Technology'),
    (METALLURGY, 'Metallurgy')
]

GENDER = [
    ('Male', 'Male'),
    ('Female', 'Female')
]
class Employee (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    employee_number = models.CharField(max_length=100, null=False)
    name =  models.CharField(max_length=100, null=False)
    department = models.CharField(max_length=50, null=False, choices=DEPARTMENR_CHOICES)
    email = models.EmailField(max_length=50, null=False, unique=True)
    gender = models.CharField(max_length=10, null=False, choices = GENDER)
    telephone_number = models.CharField(max_length=20)

    def __repr__(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']