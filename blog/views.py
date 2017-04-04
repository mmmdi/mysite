#coding:utf-8
from django.shortcuts import render,render_to_response,redirect
# from django.contrib.auth.decorators import login_required 
from django import forms  
import json
from blog.models import User, Case, Plan
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.

class UserForm(forms.Form):  
    username = forms.CharField()  
    password = forms.CharField()  
    email = forms.EmailField()  
    tel = forms.CharField()  
  
class LoginForm(forms.Form):  
    username = forms.CharField()  
    password = forms.CharField()  
  
class Information(forms.Form):  
    name = forms.CharField()  
    sex = forms.CharField()  
    age = forms.IntegerField()  
    email = forms.EmailField()  
    tel = forms.CharField()  

class CaseForm(forms.Form):
    casename = forms.CharField()
    location = forms.CharField()
    hours = forms.DecimalField()
    description = forms.CharField()
    casetype = forms.CharField()

def home(req):
    username = req.session.get('username')  
    return render_to_response('home.html',{'username':username})

def register(req):  
    if req.method == 'POST':  
        uf = UserForm(req.POST)  
        err = '该用户名已存在'  
        if uf.is_valid():  
            username = uf.cleaned_data['username']  
            password = uf.cleaned_data['password']  
            email = uf.cleaned_data['email']  
            tel = uf.cleaned_data['tel']
            nickname = req.POST.get('nickname')
            if User.objects.filter(username__exact=username):  
                return render_to_response('register.html',{'uf':uf,'err':err})  
            User.objects.create(username = username, password = password,
                email = email, tel = tel, nickname = nickname)
            req.session['username'] = username  
            return HttpResponseRedirect('/')
        else: 
            err = uf.errors
            return render_to_response('register.html', {'uf':uf,'err':err})  
    else:  
        uf = UserForm()  
    return render_to_response('register.html', {'uf':uf})  

def login(req):
    next = req.POST.get('next', req.GET.get('next', ''))
    if req.method == 'POST':  
        uf = LoginForm(req.POST)  
        if uf.is_valid():  
            username = uf.cleaned_data['username']  
            password = uf.cleaned_data['password']  
            user = User.objects.filter(username__exact = username,password__exact = password)  
            if user:  
                req.session['username'] = username
                if next:
                    return HttpResponseRedirect(next)
                return HttpResponseRedirect('/')
            else:  
                err = '用户名或密码错误，请重新输入'  
                return render_to_response('login.html', {'err':err})  
    else:  
        uf = UserForm()
        err=''
    err=''
    return render_to_response('login.html', {'uf':uf, 'err':err})     

def logout(req):  
    del req.session['username']  
    return HttpResponseRedirect('/')

def share(req):
    if req.method=="POST":
        i = 0
        planname=req.POST.get("planname")
        days=req.POST.get("days")
        username=req.session.get('username')
        description=req.POST.get("description")
        plan = Plan(planname=planname, days=days, plantype='article',
            author=username,description=description)
        # locations?
        plan.save()
        item = len(req.POST)/5
        print item
        for i in range(0,item):
        # while i <= item-1:
            casename=req.POST.get("casename"+str(i))
            location=req.POST.get("location"+str(i))
            day=req.POST.get("day"+str(i))
            hours=req.POST.get("hours"+str(i))
            description=req.POST.get("description"+str(i))
            casetype=req.POST.get("casetype"+str(i))
            # i = i+1
            # print casename,location,hours,description,casetype
            cf=CaseForm({'casename':casename,
                'location':location,
                'hours':hours,
                'description':description,
                'casetype':casetype
                })
            err='有问题'
            if cf.is_valid():
                case=Case(casename=casename,location=location,day=day,
                    hours=hours,description=description,casetype=casetype)
                case.save()
                plan.cases.add(case)
                plan.save()
                print "successfully save case to article"
            else:
                err=cf.errors
                break
                return render_to_response('share.html', {'uf':uf,'err':'case'+str(i)+err,'username':username})
        user=User.objects.get(username=username)
        user.myarticle.add(plan)
        user.save()
        print 'successfully save article to user'
    else:
        cf=CaseForm()
        username = req.session.get('username')
        if username:
            return render_to_response('share.html',{'username':username})
        else:
            err='请先登录'
            return redirect('/login/?next=/share/')
    return render_to_response('share.html',{'username':username})

def share_form(req):
    num = req.POST.get('num')
    return render_to_response('newform.html',{'num':num})
    # a = {'aa':'aa','bb':'bb'}
    # return JsonResponse(a)

def plan_form(req):
    num = req.POST.get('num')
    return render_to_response('newform-plan.html',{'num':num})

def make(req):
    if req.method=="POST":
        i = 0
        planname=req.POST.get("planname")
        days=req.POST.get("days")
        date=req.POST.get("date")
        username=req.session.get('username')
        plan = Plan(planname=planname, days=days,
            author=username, date=date, plantype='plan')
        # # locations?
        plan.save()
        item = len(req.POST)/5
        print item
        for i in range(0,item):
        # while i <= item-1:
            print '???'
            casename=req.POST.get("casename"+str(i))
            location=req.POST.get("location"+str(i))
            day=req.POST.get("day"+str(i))
            hours=req.POST.get("hours"+str(i))
            casetype=req.POST.get("casetype"+str(i))
            description=req.POST.get("description"+str(i))
            # i = i+1
            # print casename,location,hours,description,casetype
            cf=CaseForm({'casename':casename,
                'location':location,
                'hours':hours,
                'casetype':casetype,
                'description':description
                })
            err='有问题'
            if cf.is_valid():
                case=Case(casename=casename,location=location,
                    day=day,hours=hours,casetype=casetype,description=description)
                case.save()
                plan.cases.add(case)
                plan.save()
                print "successfully save case to plan"
            else:
                err=cf.errors
                print err
                break
                return render_to_response('make.html', {'uf':uf,'err':'case'+str(i)+err,'username':username})
        user=User.objects.get(username=username)
        user.myplan.add(plan)
        user.save()
        print 'successfully save plan to user'
    else:
        cf=CaseForm()
        username = req.session.get('username')
        if username:
            return render_to_response('make.html',{'username':username})
        else:
            err='请先登录'
            return redirect('/login/?next=/make/')
    # return render_to_response('make.html',{'username':username})
    username = req.session.get('username')
    return render_to_response('make.html',{'username':username})

def userhome(req,userid):
    if userid:
        user = User.objects.get(id=userid)
    else:
        username=req.session.get('username')
        if username:
            user = User.objects.get(username=username)
        else:
            return redirect('/login/?next=/u/')
        # userid=user.id
        # return HttpResponseRedirect('/u/'+str(userid))
    articles=user.myarticle.all()
    plans = user.myplan.all()
    currentusername = req.session.get('username')
    if currentusername:
        currentuser = User.objects.get(username=currentusername)
        fvplans = currentuser.favoriteplan.all()
        fvarticles = currentuser.favoritearticle.all()
    else:
        currentuser = User()
        fvplans = Plan()
        fvarticles = Plan()
    # print user.username
    return render_to_response('userhome.html',{'articles':articles,
        'plans':plans,'user':user,'currentuser':currentuser,
        'username':currentusername,'fvplans':fvplans,
        'fvarticles':fvarticles})

def article(req,articleid):
    if req.method=="POST":
        username=req.session.get('username')
        user=User.objects.get(username=username)
        article = Plan.objects.get(id=articleid)
        cases= article.cases.all().order_by('day')

        newplan=req.POST.get("myplan")
        a,b = newplan.split(',')
        newcase=Case.objects.get(id=a)
        oldplan=Plan.objects.get(id=b)
        oldplan.cases.add(newcase)

        return render_to_response('article.html',{'username':username,
                'article':article, 'cases':cases,'user':user,
                'author':User.objects.get(username=article.author)})
    else:
        username=req.session.get('username')
        article = Plan.objects.get(id=articleid)
        cases= article.cases.all().order_by('day')
        if username:
            user=User.objects.get(username=username)
            return render_to_response('article.html',{'username':username,
                'article':article, 'cases':cases,'user':user,
                'author':User.objects.get(username=article.author)})
        else:
            return render_to_response('article.html',{'article':article,
                'cases':cases,'author':User.objects.get(username=article.author)})

def plan(req,planid):
    if req.method=="POST":
        username=req.session.get('username')
        user=User.objects.get(username=username)
        plan = Plan.objects.get(id=planid)
        cases= plan.cases.all().order_by('day')

        newplan=req.POST.get("myplan")
        a,b = newplan.split(',')
        newcase=Case.objects.get(id=a)
        oldplan=Plan.objects.get(id=b)
        oldplan.cases.add(newcase)

        return render_to_response('plan.html',{'username':username,
                'plan':plan, 'cases':cases,'user':user,
                'author':User.objects.get(username=plan.author)})
    else:
        username=req.session.get('username')
        plan = Plan.objects.get(id=planid)
        cases= plan.cases.all().order_by('day')
        if username:
            user=User.objects.get(username=username)
            # print user.myplan.all()
            return render_to_response('plan.html',{'username':username,
                'plan':plan, 'cases':cases,'user':user,
                'author':User.objects.get(username=plan.author)})
        else:
            return render_to_response('plan.html',{'plan':plan,
             'cases':cases,'author':User.objects.get(username=plan.author)})

def edit(req):
    caseid = req.POST.get('caseid')
    planid = req.POST.get('planid')
    case = Case.objects.get(id=caseid)
    plan = Plan.objects.get(id=planid)
    return render_to_response('edit.html',{'case':case,'plan':plan})

def editsubmit(req,planid,caseid):
    case = Case.objects.get(id=caseid)
    cf=CaseForm({'casename':req.POST.get("casename"),
                'location':req.POST.get("location"),
                'hours':req.POST.get("day"),
                'casetype':req.POST.get("casetype"),
                'description':req.POST.get("description")
                })
    if cf.is_valid():
        case.casename=req.POST.get("casename")
        case.location=req.POST.get("location")
        case.day=req.POST.get("day")
        case.hours=req.POST.get("hours")
        case.casetype=req.POST.get("casetype")
        case.description=req.POST.get("description")
        case.save()
    return HttpResponseRedirect('/plan/'+planid)

def fvplan(req,userid,planid):
    print 'chufafvplan'
    user=User.objects.get(id=userid)
    plan=Plan.objects.get(id=planid)
    user.favoriteplan.add(plan)
    return render_to_response('blank.html')

def fvarticle(req,userid,articleid):
    print 'chufafvarticle'
    user=User.objects.get(id=userid)
    article=Plan.objects.get(id=articleid)
    user.favoritearticle.add(article)
    return render_to_response('blank.html')

def fvcase(req,userid,caseid):
    print 'chufafvcase'
    user=User.objects.get(id=userid)
    case=Case.objects.get(id=caseid)
    user.favoritecase.add(case)
    return render_to_response('blank.html')

def search(req):
    key=req.POST.get("searchkey")
    # print key
    resultp = []
    resulta = []
    plans=Plan.objects.filter(
        Q(plantype='plan'),
        Q(planname__contains=key)|Q(description__contains=key)
    )
    for plan in plans:
        resultp.append(plan)

    articles=Plan.objects.filter(
        Q(planname__contains=key)|Q(description__contains=key),
        Q(plantype='articles')
    )
    for article in articles:
        resulta.append(article)

    cases=Case.objects.filter(
        Q(location__contains=key)|Q(casename__contains=key)
        )
    for case in cases:
        case_plans = case.plan_set.all()
        for p in case_plans:
            if p.plantype == 'plan':
                resultp.append(p)
            elif p.plantype == 'article':
                resulta.append(p)
    return render_to_response('search.html',{'articles':set(resulta),
        'plans':set(resultp),'lena':len(resulta),'lenp':len(resultp)})
    # return render_to_response('home.html')