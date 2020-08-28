from django.shortcuts import render
import datetime
import json
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from backendapp.models import Business,Address,Owners,ApplicationData
from datetime import datetime

from backendapp.models import RequestHeader

# Create your views here.
def about(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

# def requestheader(request):
#
@csrf_exempt
def loanapp(request):
   html = "<h1>welcome to loan app !</h1>"
   jsonData = request.read()
   try:
      data = json.loads(jsonData)
   except:
      response = JsonResponse({'error': 'Error'}, status=400)
      return response
   if(len(data)==0):
      response = JsonResponse({'error': 'Data not sent'}, status=400)
      return response
   print(data)
   result = CreateModel(data)
   if(result==0):
      response = JsonResponse({'Message': 'Model Updated Succesfully'}, status=200)
      return response
   else:
      response = JsonResponse({'Message': 'Model Created Succesfully'}, status=200)
      return response


@csrf_exempt
def status(request):
   filterId =  request.GET.get('filterId');
   if(filterId==''):
      response = JsonResponse({'error': 'ID not entered'},status=400)
      return response

   if ApplicationData.objects.filter(filterId=filterId).exists():
      application = ApplicationData.objects.get(filterId = filterId)
      business = application.business
      response = JsonResponse({'name': business.name, 'is Application updated?': business.updated, 'LoanId': filterId,
                               'Loan Amount': str(application.loanAmount),'Status':str(application.status)},status=200)
      return response
   else:
      response = JsonResponse({'error': 'Application with ID not found'},status=400)
      return response

def CreateModel(data):
   businessName = data['Business']['Name'];
   if Business.objects.filter(name=businessName).exists():
      print('Business has already applied')
      business = Business.objects.get(name=businessName)
      address = business.address
      address.address1 = data['Business']['Address']['Address1']
      address.address2 = data['Business']['Address']['Address2']
      address.city = data['Business']['Address']['City']
      address.state = data['Business']['Address']['State']
      address.zip = int(data['Business']['Address']['Zip'])
      address.save()
      business.name = data['Business']['Name']
      business.annualRevenue = data['Business']['SelfReportedCashFlow']['AnnualRevenue']
      business.averageBankBalance= data['Business']['SelfReportedCashFlow']['MonthlyAverageBankBalance']
      business.averageCreditCardVolume = data['Business']['SelfReportedCashFlow']['MonthlyAverageCreditCardVolume']
      business.taxId = int(data['Business']['TaxID'])
      business.phone = int(data['Business']['Phone'])
      business.naics = int(data['Business']['NAICS'])
      business.profitable = data['Business']['HasBeenProfitable']
      business.bankrupted = data['Business']['HasBankruptedInLast7Years']
      business.inceptionDate = datetime.strptime(data['Business']['InceptionDate'][:-7], '%Y-%m-%dT%H:%M:%S.%f')
      business.updated = True
      business.save()
      return 0
   else:
      print('New Application')
      owners = []
      for x in data['Owners']:
         name = x['Name']
         firstName = x['FirstName']
         lastName = x['LastName']
         email = x['Email']
         address1 = x['HomeAddress']['Address1']
         address2 = x['HomeAddress']['Address2']
         city = x['HomeAddress']['City']
         state = x['HomeAddress']['State']
         zip = int(x['HomeAddress']['Zip'])
         address = Address(address1=address1, address2=address2, city=city, state=state, zip=zip)
         dob = datetime.fromisoformat(x['DateOfBirth'])
         phone = x['HomePhone']
         ssn = int(x['SSN'])
         percent = float(x['PercentageOfOwnership'])
         address.save()
         o = Owners(name=name, firstName=firstName, lastName=lastName, email=email, dateOfBirth=dob, homePhone=phone, ssn=ssn,
                    percentageOfOwnership=percent, address=address)
         o.save()
         owners = owners + [o]

      address1 = data['Business']['Address']['Address1']
      address2 = data['Business']['Address']['Address2']
      city = data['Business']['Address']['City']
      state = data['Business']['Address']['State']
      zip = int(data['Business']['Address']['Zip'])
      officeAddress= Address(address1=address1, address2=address2, city=city, state=state, zip=zip)
      officeAddress.save()

      name = data['Business']['Name']
      annualRevenue = data['Business']['SelfReportedCashFlow']['AnnualRevenue']
      averageBankBalance = data['Business']['SelfReportedCashFlow']['MonthlyAverageBankBalance']
      averageCreditCardVolume = data['Business']['SelfReportedCashFlow']['MonthlyAverageCreditCardVolume']
      taxId = int(data['Business']['TaxID'])
      phone = data['Business']['Phone']
      naics = int(data['Business']['NAICS'])
      profitable = data['Business']['HasBeenProfitable']
      bankrupted = data['Business']['HasBankruptedInLast7Years']
      inceptionDate = datetime.strptime(data['Business']['InceptionDate'][:-7], '%Y-%m-%dT%H:%M:%S.%f')
      updated = False
      business = Business(name=name,annualRevenue = annualRevenue,averageBankBalance = averageBankBalance,
                   averageCreditCardVolume = averageCreditCardVolume,taxId = taxId,phone = phone,
                   naics = naics,profitable = profitable,bankrupted = bankrupted,inceptionDate = inceptionDate,
                   updated = updated,address=officeAddress)
      business.save()
      business.owners.set(owners)

      loanAmount = float(data['CFApplicationData']['RequestedLoanAmount'])
      creditHistory = int(data['CFApplicationData']['StatedCreditHistory'])
      entityType = data['CFApplicationData']['LegalEntityType']
      filterId = int(data['CFApplicationData']['FilterID'])
      status= 'In Progress'

      loanApplication = ApplicationData(loanAmount=loanAmount, creditHistory=creditHistory, entityType=entityType, filterId=filterId,status=status,business=business)
      loanApplication.save()
      return 1