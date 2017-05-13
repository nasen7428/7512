# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json

# Create your models here.


class Node(models.Model):
	afterlist=models.TextField()
	attribute=models.TextField()
	childlist=models.TextField()

	def setAttr(self,attrName,attrValue):
		try:
			attrdict=json.loads(self.attribute)
		except:
			attrdict={}
		attrdict[attrName]=attrValue
		self.attribute=json.dumps(attrdict)

	def addAfterNode(self,nodeId):
		try:
			afternodelist=json.loads(self.afterlist)
		except:
			afternodelist=[]
		afternodelist.append(nodeId)
		self.afterlist=json.dumps(afternodelist)

	def addChildNode(self,nodeId):
		try:
			childnodelist=json.loads(self.childlist)
		except:
			childnodelist=[]
		childnodelist.append(nodeId)
		self.childlist=json.dumps(childnodelist)






class User(models.Model):
	attribute=models.TextField()

	def setAttr(self,attrName,attrValue):
		try:
			attrdict=json.loads(self.attribute)
		except:
			attrdict={}
		attrdict[attrName]=attrValue
		self.attribute=json.dumps(attrdict)

