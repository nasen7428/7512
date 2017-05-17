
# -*- coding: utf-8 -*-
from django.shortcuts import render
from WebAPI.models import Node
import json


#节点控件测试
def nodeviewtest(request):
    context={}
    return render(request, 'nodeviewtest.html')

#节点编辑页面
def nodeviewedit(request,nodeId):
    node=Node.objects.get(id=nodeId)
    attrdict=json.loads(node.attribute)
    return render(request,'nodeedit.html',{'nodeId':node.id,'AttrList':attrdict})

#空间编辑界面
def spaceviewedit(request):
    return render(request,'spaceedit.html')

#用户设置页面
def usersetting(request):
    return render(request,'usersetting.html')
