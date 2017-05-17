# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

# Create your models here.

#节点
class Node(models.Model):
    #后继节点ID列表
    afterlist=models.TextField()
    #属性列表
    attribute=models.TextField()
    #节点空间列表
    spacelist=models.TextField()

    #设置属性
    def setAttr(self,attrName,attrValue):
        try:
            attrdict=json.loads(self.attribute)
        except:
            attrdict={}
        attrdict[attrName]=attrValue
        self.attribute=json.dumps(attrdict)

    #添加后继节点
    def addAfterNode(self,nodeId):
        try:
            afternodelist=json.loads(self.afterlist)
        except:
            afternodelist=[]
        afternodelist.append(nodeId)
        self.afterlist=json.dumps(afternodelist)

    #添加节点子空间
    def addSpace(self,spaceId):
        try:
            nodespacelist=json.loads(self.spacelist)
        except:
            nodespacelist=[]
        nodespacelist.append(spaceId)
        self.spacelist=json.dumps(nodespacelist)

#节点空间
class Space(models.Model):
    #空间起始节点
    childlist=models.TextField()
    #添加空间起始节点
    def addChildNode(self,nodeId):
        try:
            childnodelist=json.loads(self.childlist)
        except:
            childnodelist=[]
        childnodelist.append(nodeId)
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

