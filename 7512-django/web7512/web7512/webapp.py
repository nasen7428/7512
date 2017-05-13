from django.shortcuts import render

def nodeviewtest(request):
    return render(request, 'nodeviewtest.html')

def nodeviewedit(request):
    return render(request,'nodeedit.html')