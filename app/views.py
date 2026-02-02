from django.shortcuts import render,redirect
from .models import Employee


# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    return render(req,'register.html')

def register1(req):
    print(req.POST)
    print(req.FILES)
    # print(req.META)
    # print(req.Settings)
    n=req.POST.get('name')
    g=req.POST.get('gender')
    q=req.POST.getlist('qualification')
    ag=req.POST.get('age_group')
    s=req.POST.get('state')
    e=req.POST.get('email')
    c=req.POST.get('contact')
    p=req.POST.get('password')
    pp=req.FILES.get('profile_picture')
    m=req.FILES.get('music')
    v=req.FILES.get('video')
    r=req.FILES.get('resume')
    print(n,g,q,ag,e,c,p,pp,m,v,r,sep=",")
    response=render(req,'login.html')
    response.set_cookie('name',n)
    response.set_cookie('gender',g)
    response.set_cookie('qualification',q)
    response.set_cookie('age_group',ag)
    response.set_cookie('state',s)
    response.set_cookie('email',e)
    response.set_cookie('contact',c)
    response.set_cookie('password',p)
    response.set_cookie('profile_picture',pp)
    response.set_cookie('music',m)
    response.set_cookie('video',v)
    response.set_cookie('resume',r)
    return response

def login(req):
    return render(req,'login.html')

def get_cookie(req):
    print(req.COOKIES)
    n=req.COOKIES.get('name')
    g=req.COOKIES.get('gender')
    q=req.COOKIES.get('qualification')
    ag=req.COOKIES.get('age_group')
    s=req.COOKIES.get('state')
    e=req.COOKIES.get('email')
    c=req.COOKIES.get('contact')
    p=req.COOKIES.get('password')
    pp=req.COOKIES.get('profile_picture')
    m=req.COOKIES.get('music')
    v=req.COOKIES.get('video')
    r=req.COOKIES.get('resume')
    data={'name':n,'gender':g,'qualification':q,'age_group':ag,'state':s,'email':e,'contact':c,'password':p,'profile_picture':pp,
          'music':m,'video':v,'resume':r}
    return render(req,'login.html',{'data':data})

def delete_cookie(req):
    response=render(req,'login.html',{'msg':'Data deleted'})
    response.delete_cookie('name')
    response.delete_cookie('email')
    response.delete_cookie('gender')
    response.delete_cookie('state')
    return response

def sqlitedata(req):
    if req.method=='POST':
      n=req.POST.get('name')
      g=req.POST.get('gender')
      q=req.POST.getlist('qualification')
      ag=req.POST.get('age_group')
      s=req.POST.get('state')
      e=req.POST.get('email')
      c=req.POST.get('contact')
      p=req.POST.get('password')
      pp=req.FILES.get('profile_picture')
      m=req.FILES.get('music')
      v=req.FILES.get('video')
      r=req.FILES.get('resume')

      Employee.objects.create(
        Name=n,
        Gender=g,
        Qualification=q,
        Email=e,
        State=s,
        Contact=c,
        Password=p,
        Profile_picture=pp,
        Music=m,
        Video=v,
        Resume=r
        )
      return redirect('login')
