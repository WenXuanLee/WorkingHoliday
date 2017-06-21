from django import forms
from .models import User
from .models import MainKey
from .models import Host
from .models import UserComment
from .models import HostComment

class UserStore(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ( 'email', 'phone','brief_intro')
        
class HostStore(forms.ModelForm):
    
    class Meta:
        model = Host
        fields = ('hostname', 'hostarea','hostaddress', 'hostemail', 'hostphone', 'hostintro', 'hostneed', 'hostbrief', 'hostimage1'
        , 'hostimage2', 'hostimage3', 'hostimage4')
        
class userComment(forms.ModelForm):
    
    class Meta:
        model = UserComment
        fields = ('userId','comment',)   
        
class hostComment(forms.ModelForm):
    
    class Meta:
        model = HostComment
        fields = ('hostId','comment',)    