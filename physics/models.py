import datetime
from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Topic(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000,null=True, blank=True,default='')
    pub_date = models.DateTimeField('date published')
    order = models.IntegerField(default=0)
    
    #Level 0 for both, 1 for experimental, 2 for theoretical
    level_choices = ((0,'Both'),(1,'Experimental'),(2,'Theoretical'))
    level = models.IntegerField(choices=level_choices, default=0)
    
    def __unicode__(self):
        return u'%s' % (self.title)
    def __str__(self):
        return u'%s' % (self.title)
    def sorted_lecture_set(self):
        return self.lecture_set.order_by('order')
    def sorted_pset_set(self):
        return self.pset_set.order_by('order')
    def reverse_sorted_lecture_set(self):
        return self.lecture_set.order_by('-order')
    def reverse_sorted_pset_set(self):
        return self.pset_set.order_by('-order')
    

     
class Lecture(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000,null=True, blank=True,default='')
    lecture_file = models.FileField(upload_to='lectures', null=True, blank=True)
    
    
    #Level 0 for both, 1 for experimental, 2 for theoretical
    level_choices = ((0,'Both'),(1,'Experimental'),(2,'Theoretical'))
    level = models.IntegerField(choices=level_choices, default=0)
    
    pub_date = models.DateTimeField('date published')
    topic=models.ForeignKey(Topic)
    

class PSet(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000,null=True, blank=True,default='')
    solutions_description = models.CharField(max_length=1000,null=True, blank=True,default='')
    problems_file = models.FileField(upload_to='pset/problems', null=True, blank=True)
    solutions_file = models.FileField(upload_to='pset/solutions', null=True, blank=True)

    
    #Level 0 for both, 1 for experimental, 2 for theoretical
    level_choices = ((0,'Both'),(1,'Experimental'),(2,'Theoretical'))
    level = models.IntegerField(choices=level_choices, default=0)
    
    pub_date = models.DateTimeField('date published')
    topic=models.ForeignKey(Topic)
    
    
class Announcement(models.Model):
    order = models.IntegerField(default = 0)
    title = models.CharField(max_length=1000)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')

class News(models.Model):
    order = models.IntegerField(default = 0)
    title = models.CharField(max_length=1000)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    class Meta:
        verbose_name_plural = "News"

class TopicRequest(models.Model):
    order = models.IntegerField(default = 0)
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    response_email = models.EmailField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    
class Suggestion(models.Model):
    order = models.IntegerField(default = 0)
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=True)
    response_email = models.EmailField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    


    



