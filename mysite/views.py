# -*- coding: utf-8 -*-
from django.shortcuts import render
import re
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext, loader
from django.shortcuts import render, render_to_response
from django.forms import ModelForm
from django.core.context_processors import csrf
import random
from django.template import RequestContext
from django.template import loader
from mysite import socks
import socket
from mysite.models import User, Ip, Film_User_Favrel,Film_User_Ownrel,Promo,Film, Tag, Tag_Film_Rel, Category_Film_Rel, Category, Pic, Vid
# Create your views here.

def get_name_and_balance(request):
    usr = None
    pwd=None
    balance=None
    uid=None
    usr=request.session['username']
    pwd=request.session['password']
    spc_obj=User.objects.all().filter(username=usr).filter(password=pwd)[0]
    balance=spc_obj.balance
    uid=spc_obj.id

    return usr,balance,uid

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def msg(request, retlink,msginf):
    c = {
        'retlink': retlink,
        'msginf':msginf,
    }
    return render_to_response('mysite/msg.html', c,context_instance=RequestContext(request))


def index(request):
    return HttpResponse("ok")


def addfilm(request):
    return render_to_response('mysite/addfilm.html', context_instance=RequestContext(request))

def getfilm(request,id):
    username=request.session.get('username')
    password=request.session.get('password')
    if not username or not password:
        return msg(request,'mysite:login','请先登录！') 
    spc_users = User.objects.all().filter(username=username).filter(password=password)
    if len(spc_users) != 1 :
        return msg(request,'mysite:login','请先登录！')    

    films = Film.objects.all().filter(id=id)
    if not films or len(films)==0:
        return msg(request,"index","读取影片失败")
    film = films[0]
    usr = spc_users[0]
    #已买
    spc_rels = Film_User_Ownrel.objects.all().filter(fid=id).filter(uid=usr.id) 
    if len(spc_rels)==0:
        if usr.balance < film.price: #未买 余额不足
            return msg(request,'mysite:account','余额不足，无法观看！')
        else: #为买 余额足
        #扣钱
            usr.balance -= film.price  
            usr.save()
        #简历拥有关系
            Film_User_Ownrel(fid=id,uid=usr.id).save()
    #film = Film.objects.all().filter(id=id)[0]

    picurls = [pic.picurl for pic in Pic.objects.all().filter(film__id=id)]
    vidurls = [vid.vidurl for vid in Vid.objects.all().filter(film__id=id)]
    tids = [rel.tid for rel in Tag_Film_Rel.objects.all().filter(fid=id)]
    cids = [rel.cid for rel in Category_Film_Rel.objects.all().filter(fid=id)]
    tags = [tag.tagname for tag in Tag.objects.all().filter(id__in=tids)]
    categories = [ cat.categoryname for cat in  Category.objects.all().filter(id__in=cids)]
    c={
        'title':film.title,
        'views':film.views,
        'likes':film.likes,
        'price':film.price,
        'covurl':film.covurl,
        'tags':tags,
        'categories':categories,
        'picurls':picurls,
        'vidurls':vidurls,
    }
    

    film.views+=1
    film.save()
    return render_to_response('mysite/getfilm.html', c,context_instance=RequestContext(request))


def handleaddfilm(request):
    # filmname tags categories  covurl picurls vidurls
    filmname = request.POST['filmname']
    covurl = request.POST['covurl']
    price = request.POST['price']

    tags = request.POST['tags'].split('#')
    categories = request.POST['categories'] .split('#')
    picurls = request.POST['picurls'].split('#')
    vidurls = request.POST['vidurls'].split('#')

    if tags==[] or categories==[] or picurls==[] or vidurls==[] or filmname=="" or covurl=="":
        return msg(request,"mysite:addfilm","所有的项均不能留空！")
    film = Film(title=filmname, covurl=covurl,price=price)
    film.save()  # add film
    fid = film.id
    for tag in tags:  # add tag
        qres = Tag.objects.all().filter(tagname=tag)
        tid = None
        if len(qres) == 0:
            ntag = Tag(tagname=tag)
            ntag.save()
            tid = ntag.id
        else:
            tid = qres[0].id
        Tag_Film_Rel(fid=fid, tid=tid).save()
    for category in categories:
        qres = Category.objects.all().filter(categoryname=category)
        cid = None
        if len(qres) == 0:
            ncategory = Category(categoryname=category)
            ncategory.save()
            cid = ncategory.id
        else:
            cid = qres[0].id
        Category_Film_Rel(fid=fid, cid=cid).save()
    for picurl in picurls:
        Pic(picurl=picurl, film=film).save()
    for vidurl in vidurls:
        Vid(vidurl=vidurl, film=film).save()

    return msg(request,"mysite:addfilm","成功")

def reg(request):
    return render_to_response('mysite/reg.html', context_instance=RequestContext(request))

def check_format(request):
    username_str = request.POST["username"]
    password_str = request.POST["password"]
    email_str = request.POST["email"]
    fg = 1
    if len(username_str) > 0 and len(username_str) <= 20:
        for tc in username_str:
            if ((ord(tc) >= ord('a') and ord(tc) <= ord('z')) or (ord(tc) >= ord('A') and ord(tc) <= ord('Z')) or (ord(tc) >= ord('0') and ord(tc) <= ord('9'))):
                pass
            else:
                fg = 0
                break
        if not (fg == 1 and len(password_str) > 0 and len(password_str) <= 20):
            fg = 0

        if fg == 1 and len(email_str) > 0 and len(email_str) <= 74:
            spr_idx = email_str.find('@')
            if spr_idx != -1:
                for i in range(0, spr_idx):
                    tc = email_str[i]
                    if ((ord(tc) >= ord('a') and ord(tc) <= ord('z')) or (ord(tc) >= ord('A') and ord(tc) <= ord('Z')) or (ord(tc) >= ord('0') and ord(tc) <= ord('9'))):
                        pass
                    else:
                        fg = 0
                        break
                if fg == 1:
                    for i in range(spr_idx + 1, len(email_str)):
                        if ((ord(tc) >= ord('a') and ord(tc) <= ord('z')) or (ord(tc) >= ord('A') and ord(tc) <= ord('Z')) or (ord(tc) >= ord('0') and ord(tc) <= ord('9')) or ord(tc) == ord('.')):
                            pass
                        else:
                            fg = 0
                            break

            else:
                fg = 0
        else:
            fg = 0

    else:
        fg = 0

    return fg

def handlereg(request):
    c={}
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    if check_format(request) == 0:
        return msg(request,"mysite:reg","注册格式不对！")
    exist_user_list = User.objects.all().filter(
        username=username
        )
    if len(exist_user_list) != 0:
        return msg(request,"mysite:reg","用户已经存在.")
    exist_user_list = User.objects.all().filter(
        email=email
        )
    if len(exist_user_list) != 0:
        return msg(request,"mysite:reg","邮箱已经存在.")
    user = User(username=username,password=password,email=email)
    user.save()
    promo = Promo(user=user)
    promo.save()
    exist_ip_list = Ip.objects.all().filter(ipaddr=get_client_ip(request))
    if len(exist_ip_list) !=0 and exist_ip_list[0].reged==False:
        theboss = exist_ip_list[0].p_user
        theboss.promo.invites += 1
        theboss.promo.save()
        theboss.balance += 10
        theboss.save()
        exist_ip_list[0].reged=True
        exist_ip_list[0].save()
    request.session['username'] = user.username
    request.session['password'] = user.password
    return msg(request,'mysite:account', "注册成功！")

def handlelogin(request):
    exist_user_list = User.objects.all().filter(
        username=request.POST['username']).filter(password=request.POST['password'])
    if len(exist_user_list) == 0:        
        return msg(request,'mysite:login', '用户名或者密码错误!')
    request.session['username'] = request.POST['username']
    request.session['password'] = request.POST['password']
    return account(request)

def login(request):
    return render_to_response('mysite/login.html', context_instance=RequestContext(request))

def logout(request):
    try:
        request.session.flush()
    except KeyError:
        pass
    return msg(request,'mysite:index', '退出成功！')

def account(request):
    username = request.session['username']
    password = request.session['password']
    exist_user_list=User.objects.all().filter(username=username).filter(password=password)
    if len(exist_user_list) != 1:
        return msg(request,'mysite:login',"异常错误！")
    user = exist_user_list[0]
    c ={
        'user':user,
    }
    usr,balance,uid=get_name_and_balance(request)
    c['usr']=usr
    c['balance']=balance
    c['uid']=uid
    return render_to_response('mysite/account.html',c,context_instance=RequestContext(request))


def handledit(request):
    try:
        exist_user_list = User.objects.all().filter(
            username=request.session['username']).filter(password=request.session['password'])
        if len(exist_user_list) != 1:
            return msg(request,'mysite:account', '异常错误!')
        user = exist_user_list[0]
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.save()
        request.session['password'] = user.password
    except:
        return msg(request,'mysite:account', '修改失败!')
    return account(request)

def edit(request):
    c={}
    try:
        exist_user_list = User.objects.all().filter(
            username=request.session['username']).filter(password=request.session['password'])
        if len(exist_user_list) != 1:
            return msg(request,'mysite:account', '异常错误!')
        user = exist_user_list[0]
        c['email'] = user.email
        c['passwd'] = user.password
    except:        
        return msg(request,'mysite:account', '获取用户信息失败!')
    usr,balance,uid=get_name_and_balance(request)
    c['usr']=usr
    c['balance']=balance
    c['uid']=uid
    return render_to_response('mysite/edit.html', c, context_instance=RequestContext(request))

def regwithid(request,bossid):
    clientip = get_client_ip(request)
    p_user = get_object_or_404(User,id=bossid)
    singleip = Ip(p_user=p_user,ipaddr=clientip,reged=False)
    exist_ip_list = Ip.objects.all().filter(ipaddr=clientip)
    if len(exist_ip_list) == 0: 
        singleip.save()       
        theboss = p_user
        theboss.promo.clicks += 1
        theboss.promo.save()
        theboss.balance += 3
        theboss.save()
        return index(request) 
    else:
        return index(request)

def film_list(request,page):
    spc_vids =  Film.objects.all()
    paginator=Paginator(spc_vids,25)
    try:
        partcontent=paginator.page(page)
    except PageNotAnInteger:
        partcontent=paginator.page(1)
    except EmptyPage:
        partcontent=paginator.page(paginator.num_pages)
    c = {'items':partcontent,}
    usr,balance,uid=get_name_and_balance(request)
    c['usr']=usr
    c['balance']=balance
    c['uid']=uid
    return render_to_response('mysite/film_list.html',c,context_instance=RequestContext(request))

def gopagefilm(request):
    return film_list(request,request.POST['pagenum'])