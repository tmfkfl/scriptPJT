from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def index(request):
    print(">>>>>>>>debug client path 127.0.0.1:8000/script/main index() call render /script/index.html")
    return render(request, 'script/index.html')

def basic(request):
    print(">>>>>>>>debug client path 127.0.0.1:8000/script/basic index() call render /script/basic.html")
    return render(request, 'script/basic.html')

def dom(request):
    print(">>>>>>>>debug client path 127.0.0.1:8000/script/dom index() call render /script/dom.html")
    return render(request, 'script/dom.html')

def ajax(request):
    print(">>>>>>>>debug client path 127.0.0.1:8000/script/ajax index() call render /script/ajax.html")
    return render(request, 'script/ajax.html')

def maker(request):
    print(">>>>>>>>debug client path /script/maker index() call JsonResponse")
    maker = request.POST['maker']
    print(">>> param = ", maker)

    response_json = []
    response_json.append({'maker': maker, 'data' : ['A3','A4','A5','A6','A8','RS8']})

    return JsonResponse(response_json, safe=False)