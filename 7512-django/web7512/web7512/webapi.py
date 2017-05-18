# -*- coding: utf-8 -*-
from django.http import HttpResponse
from WebAPI.models import Node, User,Space
from django.shortcuts import render
import json


#测试api的页面
def apitest(request):
    return render(request, "webapitest.html")

#检测请求方式
def Checkfunc(func,request):
    # try:
        ret=func(request)
        if ret:
            return ret
        return HttpResponse('success')
    # except:
    #     return HttpResponse('server have error')

#检测POST亲求
def POST(func):
    def isPOST(request):
        if not request.POST:
            return HttpResponse('it should be post')
        return Checkfunc(func,request)
    return isPOST

#检测GET请求
def GET(func):
    def isGET(request):
        if not request.GET:
            return HttpResponse('it should be get')
        return Checkfunc(func,request)
    return isGET

##################################################核心api#######################################

#创建一个节点
@POST
def createNode(request):
    node = Node()
    node.setAttr(request.POST['AttrName'], request.POST['AttrValue'])
    node.save()

#设置ID1节点的后继节点为ID2
@POST
def setNodeBeforAfter(request):
    node=Node.objects.get(id=request.POST['ID1'])
    node.addAfterNode(request.POST['ID2'])
    node.save()

#删除ID节点
@POST
def deleteNode(request):
    Node.objects.get(id=request.POST['ID']).delete()

#设置ID节点的名为AttrName的节点属性为AttrValue
@POST
def setNodeAttr(request):
    node = Node.objects.get(id=request.POST['ID'])
    node.setAttr(request.POST['AttrName'], request.POST['AttrValue'])
    node.save()

#################################空间###################################

#向NID的子节点添加一个子空间
@POST
def addChildSpace(request):
    node=Node.objects.get(id=request.POST['ID'])
    space=Space()
    space.save()
    node.addSpace(space.id)
    node.save()

#向SID的空间添加一个NID的起始子节点
@POST
def addChildNode(request):
    space=Space.objects.get(id=request.POST['ID'])
    node=Node()
    node.save()
    space.addChildNode(node.id)
    space.save()

#获取ID空间的所有子节点
@GET
def getAllChildNode(request):
    # for node in Node.objects.all():
    #     node.clearUnuselessLink()
    space=Space.objects.get(id=request.GET['ID'])
    childnodelist=space.getStartNodes()
    rentlist={}
    for childId in childnodelist:#获取起始节点
        node=Node.objects.get(id=childId)
        rentlist[childId]={'isFirst':True,'afterlist':node.getAfterNodes()}
    while True:
        addidlist=[]
        for rentnode in rentlist.values():#递归获取所有节点
            for rnalid in rentnode['afterlist']:
                rnalid=int(rnalid)
                if not rnalid in rentlist:
                    addidlist.append(int(rnalid))
        for addid in addidlist:
            node=Node.objects.get(id=addid)
            rentlist[addid]={'isFirst':False,'afterlist':node.getAfterNodes()}
        else:
            break
    jsonspacenode=json.dumps(rentlist)
    return HttpResponse(jsonspacenode)

######################################用户####################

#创建一个属性AttrName的值为AttrValue的用户
@POST
def createUser(request):
    user=User()
    user.setAttr(request.POST['AttrName'], request.POST['AttrValue'])
    user.save()

#设置用户属性
@POST
def setUserAttr(request):
    user = User.objects.get(id=request.POST['ID'])
    user.setAttr(request.POST['AttrName'], request.POST['AttrValue'])
    user.save()
