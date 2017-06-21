from django.contrib import admin
from .models import MainKey
from .models import User
from .models import Host
from .models import ApplyManage
from .models import ConfirmManage
from .models import ConfirmUserManage
from .models import UserComment
from .models import HostComment
# Register your models here.
class mainKey(admin.ModelAdmin) :
    list_display = ['userId','userPicture','name']
    class Meta : 
        model = MainKey
        
admin.site.register(MainKey,mainKey)

class UserAdmin(admin.ModelAdmin) :
    list_display = ['uId','email','phone','brief_intro','timestamp']
    class Meta : 
        model = User

admin.site.register(User,UserAdmin)

class host(admin.ModelAdmin) :
    list_display = ['hostId','hostname','hostcomment', 'hostarea','hostaddress', 'hostemail', 'hostphone', 'hostintro', 'hostneed', 'hostbrief', 'hostimage1'
    , 'hostimage2', 'hostimage3', 'hostimage4','hostpicture']
    class Meta : 
        model = Host
        
admin.site.register(Host,host)

class applyManage(admin.ModelAdmin) :
    list_display = ['hostId','applyId','applyEmail','applyMonth','applyName','applyIntro','applyHostName','applyhostemail', 'applyHostIntro','applyPicture','hostPicture']
    class Meta : 
        model = ApplyManage
        
admin.site.register(ApplyManage,applyManage)

class confirmManage(admin.ModelAdmin) :
    list_display = ['hostId','confirmId','confirmMonth','confirmName','confirmEmail','confirmIntro','confirmPicture']
    class Meta : 
        model = ConfirmManage
        
admin.site.register(ConfirmManage,confirmManage)

class confirmUserManage(admin.ModelAdmin) :
    list_display = ['hostId','confirmId','confirmMonth','confirmHostName','confirmHostEmail','confirmHostIntro','confirmPicture','hostPicture']
    class Meta : 
        model = ConfirmUserManage
        
admin.site.register(ConfirmUserManage,confirmUserManage)

class userComment(admin.ModelAdmin) :
    list_display = ['userId','commentId','commentName','commentarea','commentHostName','comment','commentPicture']
    class Meta : 
        model = UserComment
        
admin.site.register(UserComment,userComment)

class hostComment(admin.ModelAdmin) :
    list_display = ['hostId','commentId','commentName','comment','commentPicture']
    class Meta : 
        model = HostComment
        
admin.site.register(HostComment,hostComment)