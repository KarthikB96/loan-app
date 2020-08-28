from django.db import models

# Create your models here.
class RequestHeader(models.Model):
   CFRequestId = models.IntegerField()
   requestDate = models.DateTimeField()
   CFApiUserId = models.CharField(max_length = 50)
   CFApiPassword = models.CharField(max_length = 50)
   isTestLead = models.BooleanField()

class Address(models.Model):
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200,blank=True,null=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField(max_length=5)

    class Meta:
        db_table = "address"

class Owners(models.Model):
    name = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    dateOfBirth = models.DateTimeField()
    homePhone = models.CharField(max_length=200)
    ssn = models.CharField(max_length=200)
    percentageOfOwnership = models.FloatField()
    class Meta:
        db_table = "owners"

class Business(models.Model):
    name = models.CharField(max_length=200)
    annualRevenue = models.FloatField()
    averageBankBalance = models.FloatField()
    averageCreditCardVolume = models.FloatField()
    taxId = models.IntegerField(blank=True)
    phone = models.CharField(max_length=200)
    naics = models.IntegerField(blank=True)
    profitable = models.BooleanField()
    bankrupted = models.BooleanField()
    inceptionDate = models.DateField()
    owners = models.ManyToManyField(Owners)
    updated = models.BooleanField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    class Meta:
        db_table = "business"

class ApplicationData(models.Model):
    loanAmount = models.FloatField()
    creditHistory = models.IntegerField()
    entityType = models.CharField(max_length=200)
    filterId = models.IntegerField()
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    status = models.CharField(max_length=200,default='In Progress')
    class Meta:
        db_table = "applicationdata"
