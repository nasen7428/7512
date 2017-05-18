
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
    node=Node.objects.get(id=nodeId)
    attrdict=json.loads(node.attribute)
    spacelist=json.loads(node.spacelist)
    return render(request,'nodeedit.html',{'nodeId':node.id,'AttrList':attrdict,'SpaceList':spacelist})

#空间编辑界面
def spaceviewedit(request,spaceId):
	space=Space.objects.get(id=spaceId)
	return render(request,'spaceedit.html',{'spaceId':space.id,'spaceNodes':space.getAllNode()})

#用户设置页面
def usersetting(request,userId):
    user=User.objects.get(id=userId)
    attrdict=json.loads(user.attribute)
    return render(request,'usersetting.html',{'userId':user.id,'AttrList':attrdict})
