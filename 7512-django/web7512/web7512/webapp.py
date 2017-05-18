
# -*- coding: utf-8 -*-
from django.shortcuts import render
from WebAPI.models import Node,User,Space
import json


#节点控件测试
def nodeviewtest(request):
    context={}
    return render(request, 'nodeviewtest.html')

#节点编辑页面
def nodeviewedit(request,nodeId):
    return render(request,'nodeedit.html',{'nodeId':nodeId})

#空间编辑界面
def spaceviewedit(request,spaceId):
	return render(request,'spaceedit.html',{'spaceId':spaceId})

#用户设置页面
def usersetting(request,userId):
    user=User.objects.get(id=userId)
    attrdict=json.loads(user.attribute)
    return render(request,'usersetting.html',{'userId':user.id,'AttrList':attrdict})
