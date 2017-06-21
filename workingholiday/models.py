from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class MainKey(models.Model) :
    userId = models.CharField(max_length=200,null = True,blank = True )
    userPicture = models.URLField(max_length=200,null = True,blank = True)
    name = models.CharField(max_length=200,null=True,blank=True)
    
    def key(self):
        return "MainKey"
    def get_absolute_url(self):
        return reverse("user", kwargs={"uid": self.userId})
    def get_hostpage_url(self):
        return reverse("pageid", kwargs={"pageid": self.userId})
    def get_usermanage_url(self):
        return reverse("usermanageid", kwargs={"usermanageid": self.userId})
        
class User(models.Model) :
    uId = models.CharField(max_length=200,null = True,blank = True)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    brief_intro = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add = True,auto_now = False)
    update = models.DateTimeField(auto_now_add = False,auto_now = True)
    
    def User(self):
        return "User"

class Host(models.Model) :
    hostId = models.CharField(max_length=200,null = True,blank = True)
    hostname = models.CharField(max_length=50,null=True,blank=True)
    hostcomment = models.IntegerField(default=0)
    hostarea =  models.CharField(max_length=50,null=True,blank=True)
    hostaddress =  models.CharField(max_length=50)
    hostemail = models.EmailField(null=True,blank=True)
    hostphone = models.CharField(max_length=50)
    hostintro = models.CharField(max_length=500)
    hostneed = models.CharField(max_length=200)
    hostbrief = models.CharField(max_length=200)
    hostimage1 = models.ImageField(upload_to='image/', null = True,blank = True)
    hostimage2 = models.ImageField(upload_to='image/', null = True,blank = True)
    hostimage3 = models.ImageField(upload_to='image/', null = True,blank = True)
    hostimage4 = models.ImageField(upload_to='image/', null = True,blank = True)
    hostpicture = models.URLField(max_length=200,null = True,blank = True)
    
    def host(self):
        return "Host"

    def get_area_url(self):
        return reverse("area", kwargs={"area": self.hostarea})
        
class ApplyManage(models.Model) :
    hostId = models.CharField(max_length=200,null = True,blank = True)
    applyId = models.CharField(max_length=200,null=True,blank=True)
    applyEmail = models.EmailField(null=True,blank=True)
    applyMonth = models.CharField(max_length=200,null=True,blank=True)
    applyName = models.CharField(max_length=200,null=True,blank=True) 
    applyIntro = models.CharField(max_length=500,null=True,blank=True) 
    applyHostName = models.CharField(max_length=200,null=True,blank=True) 
    applyHostIntro = models.CharField(max_length=500,null=True,blank=True) 
    applyPicture = models.URLField(max_length=200,null = True,blank = True)
    applyhostemail = models.EmailField(null=True,blank=True)
    hostPicture = models.URLField(max_length=200,null = True,blank = True)
    
    def ApplyManage(self):
        return "ApplyManage"
        
class ConfirmManage(models.Model) :
    hostId = models.CharField(max_length=200,null = True,blank = True)
    confirmId = models.CharField(max_length=200,null=True,blank=True)
    confirmMonth = models.CharField(max_length=200,null=True,blank=True)
    confirmName = models.CharField(max_length=200,null=True,blank=True) 
    confirmEmail = models.EmailField(null=True,blank=True)
    confirmIntro = models.CharField(max_length=500,null=True,blank=True) 
    confirmPicture = models.URLField(max_length=200,null = True,blank = True)
    #confirmHostName = models.CharField(max_length=200,null=True,blank=True) 
    #confirmHostIntro = models.CharField(max_length=500,null=True,blank=True) 
    
    def ConfirmManage(self):
        return "ConfirmManage"

class ConfirmUserManage(models.Model) :
    hostId = models.CharField(max_length=200,null = True,blank = True)
    confirmId = models.CharField(max_length=200,null=True,blank=True)
    confirmMonth = models.CharField(max_length=200,null=True,blank=True)
    confirmHostName = models.CharField(max_length=200,null=True,blank=True) 
    confirmHostEmail = models.EmailField(null=True,blank=True)
    confirmHostIntro = models.CharField(max_length=500,null=True,blank=True) 
    confirmPicture = models.URLField(max_length=200,null = True,blank = True)
    hostPicture = models.URLField(max_length=200,null = True,blank = True)
    def ConfirmUserManage(self):
        return "ConfirmUserManage"


class UserComment(models.Model) :
    userId = models.CharField(max_length=200,null = True,blank = True) 
    commentId = models.CharField(max_length=200,null = True,blank = True)
    commentName = models.CharField(max_length=200,null = True,blank = True)
    commentHostName = models.CharField(max_length=200,null = True,blank = True)
    commentarea =  models.CharField(max_length=50,null=True,blank=True)
    comment = models.CharField(max_length=500,null=True,blank=True) 
    commentPicture = models.URLField(max_length=200,null = True,blank = True)
   
    def UserComment(self):
        return "UserComment"
        
class HostComment(models.Model) :
    hostId = models.CharField(max_length=200,null = True,blank = True) 
    commentId = models.CharField(max_length=200,null = True,blank = True)
    commentName = models.CharField(max_length=200,null = True,blank = True)
    comment = models.CharField(max_length=500,null=True,blank=True) 
    commentPicture = models.URLField(max_length=200,null = True,blank = True)
    def HostComment(self):
        return "HostComment"