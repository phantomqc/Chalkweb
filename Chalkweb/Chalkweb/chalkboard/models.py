from django.db import models

# Create your models here.

class equipe(models.Model):
    equipenom = models.CharField(max_length=45)
    equipeage = models.CharField(max_length=6)
    equipesexe = models.CharField(max_length=1)
    equipecat = models.CharField(max_length=3)

class joueur(models.Model):
    joueurnom = models.CharField(max_length=45)
    equipe = models.ForeignKey('equipe')
    joueurno = models.IntegerField(null=True, blank=True)

class partie(models.Model):
    partiedate = models.DateField()
    partieadv = models.CharField(max_length=45)
    equipe = models.ForeignKey('equipe')

class alignement(models.Model):
    joueur = models.ForeignKey('joueur')
    partie = models.ForeignKey('partie')
    joueurno = models.IntegerField()

class action(models.Model):
    actionnom = models.CharField(max_length=45)
    actionacquisition = models.IntegerField()
    actionperte = models.IntegerField()

class event(models.Model):
    joueur = models.ForeignKey('joueur', related_name='joueur')
    action = models.ForeignKey('action')
    partie = models.ForeignKey('partie')
    temps = models.TimeField()
    debutx = models.FloatField()
    debuty = models.FloatField()
    finx = models.FloatField(null=True, blank=True)
    finy = models.FloatField(null=True, blank=True)
    cible = models.ForeignKey('joueur', null=True, blank=True, related_name='cible')