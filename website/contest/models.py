from django.db import models
from django.contrib.auth.models import User

class Map(models.Model):
    name = models.SlugField()
    data = models.TextField(verbose_name="map data")
    priority = models.FloatField()
    
    def __unicode__(self):
        return self.name


class Language(models.Model):
    """Programming Language"""
    name = models.CharField(max_length=200, verbose_name="name of the programming language")
    
    def __unicode__(self):
        return self.name


class Submission(models.Model):
    language = models.ForeignKey(Language, verbose_name="programming language")
    owner = models.ForeignKey(User)
    time = models.DateTimeField('time submitted at')
    
    def __unicode__(self):
        return "Submission from %s in %s at %s" % (self.owner, self.language, self.time)


class Game(models.Model):
    players = models.ManyToManyField(Submission, verbose_name="participating players")
    time = models.DateTimeField('time played at')
    map = models.ForeignKey(Map)
    
    def __unicode__(self):
        return "Game between %s at %s" % (', '.join([submission.owner.username for submission in self.players.all()]), self.time)