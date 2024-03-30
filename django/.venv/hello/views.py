from django.http import HttpResponse
from hello.chatgpt import *
from django.template import loader
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

#default home page for testing
def home(request):
    if(request.method == "GET"):
        print("get")
    elif(request.method == "POST"):
        print("post")
    print(request)
    return HttpResponse("Why hello there")

#static hello html page that has a basic webform
def babel(request):
    if(request.method == "GET"):
        print("get babel")
    elif(request.method == "POST"):
        print("post babel")
    template = loader.get_template('Babel.html')
    #make use of render so that csrf applies.  When you do this you can see that
    # the csrfmiddlewaretoken shows in the payload of the form data
    return render(request, 'Babel.html', {}) 

#post which will thread the arguments to openai to get a response.
#no error checking at this point, jost proving all this out for the first time
#in python and django which I had never used before.
@csrf_protect
def translate(request):
    if(request.method == "GET"):
        return HttpResponse("Get won't do anything here friend")
    elif(request.method == "POST"):
        print("post babel")
    sentence = request.POST.get('input')
    language = request.POST.get('language')
    return HttpResponse("wee")
    #return HttpResponse(chat(language=language, content=sentence))
    