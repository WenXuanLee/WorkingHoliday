from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from .models import MainKey
from .models import User
from .models import Host
from .models import ApplyManage
from .models import ConfirmManage
from .models import ConfirmUserManage
from .models import UserComment
from .models import HostComment
from .forms import UserStore
from .forms import HostStore
from .forms import userComment
from .forms import hostComment
# Create your views here.
class Views:
    
    def __init__(self):
        self.user_Id = 0
        self.user_name = 0
        self.local_brief = 0
        self.get_area = 0
        self.get_picture = ''
        self.get_user =''
        
    def getuserid(self, request) : 
        if request.method == 'GET':
            self.user_Id=request.GET['userId']
            self.user_name=request.GET['userName']
            self.get_picture = request.GET['userPicture']
            if MainKey.objects.filter(userId = self.user_Id).exists():
                
                print "exists" 
            

            else: 
                MainKey.objects.create(
                    userId = self.user_Id,
                    name = self.user_name,
                    userPicture = self.get_picture,
                )
   
        return HttpResponse(self.user_Id)      
    
    def homepage(self, request) : 
        get_host = Host.objects.all() 
        context = {
            'get_hosts' : get_host,
        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        return render(request, 'workingholiday/homepage.html',context)
       
    def nodata(self, request) : 
        get_host = Host.objects.all() 
        context = {
            'get_hosts' : get_host,
        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        return render(request, 'workingholiday/nodata.html',context)   
        
    def searchpage(self, request, area = None) :
        searcharea = Host.objects.all().filter(hostarea = self.get_area)
        
        count = searcharea.count()

        context = {
            "searchareas" : searcharea,
            "get_area" : self.get_area,
            "count" : count,

        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        return render(request, 'workingholiday/searchpage.html',context)
    
        
    def userpage(self, request,uid=None) : 
        get_user = MainKey.objects.get(userId=uid)
        get_intro = get_object_or_404(User,uId = uid)
        get_comment = UserComment.objects.all().filter(userId = uid)
        count = get_comment.count()
        context= {
            "get_user":get_user,
            "get_intro" : get_intro,
            "get_comments" : get_comment,
            "count" : count,
        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        return render(request, 'workingholiday/userpage.html',context)
     
        
    def useredit(self, request,userid=None) : 
      
        getid = MainKey.objects.get(userId=userid)
        context= {
            "get_id":getid,
           
        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        if request.method == 'POST':
            
            form = UserStore(request.POST or None)
            if form.is_valid():
                           
                
                local_phone = form.data.get('phone')
                local_email = form.data.get('email')
                self.local_brief = form.data.get("brief_intro")
                
                if User.objects.filter(uId = userid).exists():
                    form = UserStore(request.POST, instance = User.objects.get(uId = userid))
                    userData = form.save(commit=False)
                    userData.save()
                    #User.objects.update(
                   # email = local_email,
                   # phone = local_phone,
                   # brief_intro = local_brief,
                   # )
                    
                    return HttpResponseRedirect(getid.get_absolute_url())
                else : 
                    User.objects.create(
                        email = local_email,
                        phone = local_phone,
                        brief_intro = self.local_brief,
                        uId = userid,
                    )
                #userData = form.save(commit=False)
                #userData.save()
                    return HttpResponseRedirect(getid.get_absolute_url()) 
    
            
                
            
        else:
            return render(request, 'workingholiday/useredit.html',context)
        
    def usermanage(self, request, usermanageid = None) :
        #get_id = MainKey.objects.get(MainKey,userId = usermanageid)
        get_apply = ApplyManage.objects.all().filter(applyId = usermanageid)
        get_confirm = ConfirmUserManage.objects.all().filter(confirmId = usermanageid)
        context= {
            #"get_id" : get_id,
            "get_applys" : get_apply,
            "get_confirms" : get_confirm,
        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        if request.method=='POST' and 'cancel' in request.POST:
            local_cancel =  request.POST['cancel']
            get_confirm = ApplyManage.objects.get(applyId = usermanageid, hostId = local_cancel)
            get_confirm.delete()
            
        if request.method=='POST' and 'finish' in request.POST:
            form = hostComment(request.POST)
            local_finish =  request.POST['finish']
            get_finish = MainKey.objects.get(userId = usermanageid, )
            get_confirm = ConfirmUserManage.objects.get(confirmId = usermanageid, hostId = local_finish)
            
            if form.is_valid():
                local_comment = form.data.get('comment')
             
               
                HostComment.objects.create(
                    hostId = local_finish,
                    commentId = get_finish.userId,
                    commentName = get_finish.name,
                    comment = local_comment,
                    commentPicture = get_confirm.confirmPicture,
                )
                commentplus = Host.objects.get(hostId = local_finish)
                commentplus.hostcomment = commentplus.hostcomment  + 1
                commentplus.save()
                get_confirm.delete()
        return render(request, 'workingholiday/usermanage.html', context)
        
    def hostpage(self, request, pageid=None) : 
        get_id = MainKey.objects.get(userId=pageid)
        if Host.objects.filter(hostId = pageid).exists():
            get_host = Host.objects.get(hostId=pageid)
        else:
            return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/nodata")
        get_comment = HostComment.objects.all().filter(hostId = pageid)
        count = get_comment.count()
       
        context= {
            "get_id":get_id,
            "get_host":get_host,
            'get_comments':get_comment,
            'count':count,
        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        if request.method == 'POST':
            local_try = request.POST['field']
            local_userId = self.user_Id
            get_apply = User.objects.get(uId = local_userId)
            get_applyname = MainKey.objects.get(userId = local_userId)
            get_host = Host.objects.get(hostId = pageid)
           
            
            ApplyManage.objects.create(
                hostId = pageid,
                applyId = get_apply.uId,
                applyEmail = get_apply.email,
                applyMonth = local_try,
                applyName = get_applyname.name,
                applyIntro = get_apply.brief_intro,
                applyHostName = get_host.hostname,
                applyHostIntro = get_host.hostintro,
                applyPicture = get_applyname.userPicture,
                applyhostemail = get_host.hostemail,
                hostPicture = get_host.hostpicture,
                
            )
            
            return HttpResponseRedirect(get_applyname.get_usermanage_url())
        return render(request, 'workingholiday/hostpage.html',context)
 
        
    def hostedit(self, request, hostid = None) : 
        getid = MainKey.objects.get(userId=hostid)
        context= {
            "get_id":getid,
           
        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        if request.method == 'POST':
            
            form = HostStore(request.POST or None, request.FILES or None)
            if form.is_valid():
                get_picture = MainKey.objects.get(userId = hostid)
                local_name = form.data.get('hostname')
                local_area = form.data.get('hostarea')
                local_address = form.data.get('hostaddress')
                local_email = form.data.get('hostemail')
                local_phone = form.data.get('hostphone')
                local_intro = form.data.get("hostintro")
                local_need = form.data.get('hostneed')
                local_welfare = form.data.get("hostbrief")
                local_image1 = request.FILES['hostimage1']
                local_image2 = request.FILES['hostimage2'] 
                local_image3 = request.FILES['hostimage3']
                local_image4 = request.FILES['hostimage4']

                
                if Host.objects.filter(hostId = hostid).exists():
            
                    form = HostStore(request.POST,request.FILES, instance = Host.objects.get(hostId = hostid))
                    #host = Host.objects.get(hostId = hostid)
                    #host.hostpicture = get_picture.userPicture
                    #host.hostname = local_name,
                    #host.hostarea = local_area,
                    #host.hostaddress = local_address,
                    #host.hostemail = local_email,
                    #host.hostphone = local_phone,
                    #host.hostintro = local_intro,
                    #host.hostneed = local_need,
                    #host.hostbrief = local_welfare,
                    #host.hostimage2 = local_image2,
                    #host.hostimage3 = local_image3,
                    #host.hostimage4 = local_image4,
                    hostData = form.save(commit=False)
                    hostData.save()
               
                    return HttpResponseRedirect(getid.get_hostpage_url())
                else:
                    Host.objects.create(
                        hostId = hostid,
                        hostname = local_name,
                        hostarea = local_area,
                        hostaddress = local_address,
                        hostemail = local_email,
                        hostphone = local_phone,
                        hostintro = local_intro,
                        hostneed = local_need,
                        hostbrief = local_welfare,
                        hostimage1 = local_image1,
                        hostimage2 = local_image2,
                        hostimage3 = local_image3,
                        hostimage4 = local_image4,
                        hostpicture = get_picture.userPicture,
                    )
                #userData = form.save(hostId=self.user_Id, commit=False)
                #userData.save()
                return HttpResponseRedirect(getid.get_hostpage_url())
    
            return render(request, 'workingholiday/hostpage.html') 
                
            
        else:
            return render(request, 'workingholiday/hostedit.html',context)
        
    def hostmanage(self, request, hostmanageid = None) : 
        #get_id = get_object_or_404(MainKey,userId = hostmanageid)
        get_host = ApplyManage.objects.all().filter(hostId = hostmanageid)
        get_confirm = ConfirmManage.objects.all().filter(hostId = hostmanageid)
        context= {
            #"get_id" : get_id,
            "get_hosts" : get_host,
            "get_confirms" : get_confirm,
            
        }
        if 'searcharea' in request.GET:
             self.get_area = request.GET['searcharea']
             
             return HttpResponseRedirect("https://workingholiday-v2-wenxuanlee.c9users.io/search/self.get_area")
        if request.method=='POST' and 'confirm' in request.POST:
            local_confirm =  request.POST['confirm']
            get_confirm = ApplyManage.objects.get(applyId = local_confirm, hostId = hostmanageid)
            get_host = Host.objects.get(hostId = hostmanageid)
          
            ConfirmManage.objects.create(
                hostId = get_confirm.hostId,
                confirmId = get_confirm.applyId,
                confirmMonth = get_confirm.applyMonth,
                confirmName = get_confirm.applyName,
                confirmEmail = get_confirm.applyEmail,
                confirmIntro = get_confirm.applyIntro,
                confirmPicture = get_confirm.applyPicture,
            )
            ConfirmUserManage.objects.create(
                hostId = get_confirm.hostId,
                confirmId = get_confirm.applyId,
                confirmMonth = get_confirm.applyMonth,
                confirmHostName = get_confirm.applyHostName,
                confirmHostIntro = get_confirm.applyHostIntro,
                confirmHostEmail = get_confirm.applyhostemail,
                confirmPicture = get_confirm.applyPicture,
                hostPicture = get_host.hostpicture,
            )
            get_confirm.delete()
            
        elif request.method=='POST' and 'delete' in request.POST:
            local_delete =  request.POST['delete']
            get_confirm = ApplyManage.objects.get(applyId = local_delete, hostId = hostmanageid)
            get_confirm.delete()
            
        if request.method=='POST' and 'complete' in request.POST:
            form = userComment(request.POST)
            local_complete =  request.POST['complete']
            get_complete = Host.objects.get(hostId = hostmanageid)
            get_confirm = ConfirmManage.objects.get(confirmId = local_complete, hostId = hostmanageid)
            get_commentuser = MainKey.objects.get(userId = hostmanageid)
            if form.is_valid():
                local_comment = form.data.get('comment')
             
               
                UserComment.objects.create(
                    userId = local_complete,
                    commentId = get_complete.hostId,
                    commentName = get_commentuser.name,
                    commentHostName = get_complete.hostname,
                    commentarea = get_complete.hostarea,
                    comment = local_comment,
                    commentPicture = get_commentuser.userPicture,
                )
                
                get_confirm.delete()
              
            
     
        return render(request, 'workingholiday/hostmanage.html',context)
        
   
        