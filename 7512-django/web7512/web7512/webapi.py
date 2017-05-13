from django.http import HttpResponse
from WebAPI.models import Node, User
from django.shortcuts import render


def apitest(request):
    return render(request, "webapitest.html")

def Checkfunc(func,request):
    # try:
        func(request)
        return HttpResponse('success')
    # except:
    #     return HttpResponse('server have error')

def POST(func):
    def isPOST(request):
        if not request.POST:
            return HttpResponse('it should be post')
        return Checkfunc(func,request)
    return isPOST

def GET(func):
    def isGET(request):
        if not request.GET:
            return HttpResponse('it should be get')
        return Checkfunc(func,request)
    return isGET


@POST
def createNode(request):
    node = Node()
    node.setAttr(request.POST['AttrName'], request.POST['AttrValue'])
    node.save()

@POST
def setNodeBeforAfter(request):
    node=Node.objects.get(id=request.POST['ID1'])
    node.addAfterNode(request.POST['ID2'])
    node.save()

@POST
def deleteNode(request):
    Node.objects.get(id=request.POST['ID']).delete()

@POST
def setNodeAttr(request):
    node = Node.objects.get(id=request.POST['ID'])
    node.setAttr(request.POST['AttrName'], request.POST['AttrValue'])
    node.save()

@POST
def addChildNode(request):
    supernode = Node.objects.get(id=request.POST['ID1'])
    supernode.addChildNode(request.POST['ID2'])
    supernode.save()

@POST
def createUser(request):
    user=User()
    user.setAttr(request.POST['AttrName'], request.POST['AttrValue'])
    user.save()

@POST
def setUserAttr(request):
    user = User.objects.get(id=request.POST['ID'])
    user.setAttr(request.POST['AttrName'], request.POST['AttrValue'])
    user.save()