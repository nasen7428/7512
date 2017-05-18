# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json,logging

logger=logging.getLogger(__name__)

# Create your models here.

#节点
class Node(models.Model):
    #后继节点ID列表
    afterlist=models.TextField()
    #属性列表
    attribute=models.TextField()
    #节点空间列表
    spacelist=models.TextField()

    #获取属性
    def getAttrs(self):
        try:
            return json.loads(self.attribute)
        except:
            return {}

    #设置属性
    def setAttr(self,attrName,attrValue):
        attrdict=self.getAttrs()
        attrdict[attrName]=attrValue
        self.attribute=json.dumps(attrdict)


    #获取后继节点列表
    def getAfterNodes(self):
        try:
            return json.loads(self.afterlist)
        except:
            return []

    #添加后继节点
    def addAfterNode(self,nodeId):
        afternodelist=self.getAfterNodes()
        afternodelist.append(int(nodeId))
        self.afterlist=json.dumps(afternodelist)

    #删除后继节点
    def removeAfterNode(self,nodeId):
        afternodelist=self.getAfterNodes()
        try:
            afternodelist.remove(nodeId)
        except:
            pass
        try:
            afternodelist.remove(str(nodeId))
        except:
            pass
        self.afterlist=json.dumps(afternodelist)

    #获取子空间
    def getSpaces(self):
        try:
            return json.loads(self.spacelist)
        except:
            return []

    #添加节点子空间
    def addSpace(self,spaceId):
        nodespacelist=self.getSpaces()
        nodespacelist.append(int(spaceId))
        self.spacelist=json.dumps(nodespacelist)

    #删除子空间
    def removeSpace(self,spaceId):
        nodespacelist=self.getSpaces()
        try:
            nodespacelist.remove(spaceId)
        except:
            pass
        try:
            nodespacelist.remove(str(spaceId))
        except:
            pass
        self.spacelist=json.dumps(nodespacelist)

    #清理无效链接
    def clearUnuselessLink(self):
        afternodelist=self.getAfterNodes()
        for anode in afternodelist:
            anode=int(anode)
            try:
                Node.objects.get(id=anode)
            except:
                self.removeAfterNode(anode)
        nodespacelist=self.getSpaces()
        for space in nodespacelist:
            space=int(space)
            try:
                Space.objects.get(id=space)
            except:
                self.removeSpace(space)
        self.save()



#节点空间
class Space(models.Model):
    #空间起始节点
    childlist=models.TextField()

    #获取空间的起始节点
    def getStartNodes(self):
        try:
            return json.loads(self.childlist)
        except:
            return []

    #添加空间起始节点
    def addChildNode(self,nodeId):
        childnodelist=self.getStartNodes()
        childnodelist.append(int(nodeId))
        self.childlist=json.dumps(childnodelist)

#用户
class User(models.Model):
    #用户属性
    attribute=models.TextField()
    #设置用户属性
    def setAttr(self,attrName,attrValue):
        try:
            attrdict=json.loads(self.attribute)
        except:
            attrdict={}
        attrdict[attrName]=attrValue
        self.attribute=json.dumps(attrdict)

