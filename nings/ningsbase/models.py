from django.db import models

class Company (models.Model):
  name = models.CharField(max_length=256)
  size = models.CharField(max_length=256)
  address = models.CharField(max_length=256)
  ipo_status = models.CharField(max_length=256)
  funding_round = models.CharField(max_length=256)

class Acquisition (models.Model):
  acquirer = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_acquirer')
  acquiree = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_acquiree')
  amount = models.IntegerField()
  
class InvestingEntity(models.Model):
  name = models.CharField(max_length=256)
  investing_type = models.CharField(max_length=256)

class Funding (models.Model):
  funding_date = models.DateTimeField()
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  investing_entity = models.ForeignKey(InvestingEntity, on_delete=models.CASCADE)
  amount = models.IntegerField()
  stage = models.CharField(max_length=128)