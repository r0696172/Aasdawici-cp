from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import User

# Create your models here.


class UserA(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.TextField()
    allowDigitalTime = models.BooleanField(default=False)
    def __str__(self):
        return '{} {}'.format(self.userID, self.userName)
    

class Activity(models.Model):
    activityID = models.AutoField(primary_key=True)
    activityName = models.CharField(max_length=500)
    startTime = models.DateTimeField(default=timezone.now)
    endTime = models.DateTimeField(default=timezone.now)
    activityImage = models.TextField()
    #activityImage = models.ForeignKey(PecsImage, on_delete=models.SET_NULL, null=True)
    isComplete = models.BooleanField()
    userID = models.ForeignKey(UserA, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{} {}'.format(self.activityID, self.activityName)

    @property
    def toLate(self):
        return self.endTime >= timezone.now()
    
class Group(models.Model):
    GroupID = models.AutoField(primary_key=True)
    groupName = models.TextField()
    groupDescription = models.TextField()
    def __str__(self):
       return '{} {}'.format(self.GroupID, self.groupName)

class UserGroup(models.Model):
    linkID = models.AutoField(primary_key=True)
    groupID = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)
    userID = models.ForeignKey(UserA,on_delete=models.SET_NULL, null=True)
    def __str__(self):
       return 'linkID {}'.format(self.linkID)
    



