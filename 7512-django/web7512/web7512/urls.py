"""web7512 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
    """
# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin
from . import webapp,webapi

urlpatterns = [
url(r'^admin/', admin.site.urls),

	#api
	url(r'^webapi/apitest$',webapi.apitest),
        ##node
        url(r'^webapi/create-node$',webapi.createNode),
        url(r'^webapi/set-node-befor-after$',webapi.setNodeBeforAfter),
        url(r'^webapi/delete-node$',webapi.deleteNode),
        url(r'^webapi/set-node-attr$',webapi.setNodeAttr),
        ##space
        url(r'^webapi/add-child-space$',webapi.addChildSpace),
        url(r'^webapi/add-child-node$',webapi.addChildNode),
        url(r'^webapi/get-child-node$',webapi.getAllChildNode),
        ##user
        url(r'^webapi/create-user$',webapi.createUser),
        url(r'^webapi/set-user-attr$',webapi.setUserAttr),

	#app
	url(r'^testui/nodeview$',webapp.nodeviewtest),
    url(r'^user/setting/(?P<userId>\w+)$',webapp.usersetting),
    url(r'^edit/node/(?P<nodeId>\w+)$',webapp.nodeviewedit),
    url(r'^edit/space/(?P<spaceId>\w+)$',webapp.spaceviewedit),


    ]
