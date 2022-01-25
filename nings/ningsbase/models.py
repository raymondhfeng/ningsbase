from django.db import models

class Company (models.model):
  name = models.CharField(max_length=256)
  size = models.CharField(max_length=256)
  location = models.CharField(max_length=256)
  ipo_status = models.CharField(max_length=256)
  funding_round = models.CharField(max_length=256)


class Acquisition (models.model):
  acquirer = models.ForeignKey(Company)
  acquiree = models.ForeignKey(Company)
  amount = models.IntegerField()

class Funding (models.model)