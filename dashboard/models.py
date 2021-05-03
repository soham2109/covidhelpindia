from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class resource_entry(models.Model):
    
    class resource_type(models.TextChoices):
        Hospital = 'Hospital', _('Hospital')
        Oxygen = 'Oxygen', _('Oxygen')
        Remedesvir = 'Remedesvir', _('Remedesvir')
        Ambulance= 'Ambulance', _('Ambulance')
        Plasma  = 'Plasma', _('Plasma')
        Other_Medicines ='Other_meds',_('Other_meds')
        Others = 'Others',_('Others')


    resource = models.CharField(
        max_length=20,
        choices=resource_type.choices,
        default=resource_type.Others,
    )
    
    city=models.CharField(max_length=100) #to be fetched from SSO login
    description=models.CharField(max_length=400) #to be fetched from SSO login

    image=models.ImageField(upload_to ='uploads/',blank=True) 
    links=models.CharField(max_length=100,blank=True    )
    #resource=models.CharField(max_length=100) #will be uploaded by office
    contact = models.CharField(max_length=100,blank=True) #will be uploaded by office
    added_on=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(max_length=100,default=0)
    source =models.CharField(max_length=100,blank=True)


    class Meta:

        db_table = "resource_entry"