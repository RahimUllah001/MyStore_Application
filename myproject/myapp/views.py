from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Feature
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def index(request):

    # After ceating this objects in database from model we have no need to write tis here
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.detail = 'Our service is very Fast '
    # feature1.is_true = True

    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Realiable'
    # feature2.detail = 'Our service is very Relaible'
    # feature2.is_true = False


    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Affordable'
    # feature3.detail = 'Our service is very affordable'
    # feature3.is_true = False

    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'easy to use'
    # feature4.detail = 'Our service is very easy to use '
    # feature4.is_true = True
 
    # features  =[feature1,feature2,feature3,feature4]

    features = Feature.objects.all()



    return render(request,'index.html',{'features':features})



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email already exist")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username already used")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request, "password doesnot match")
            return redirect("register")
    else:
        return render(request, 'register.html')
    

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Credential Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')
# ////////////////////////////////counter/////////

def counter(request):                                   #for the comment it was used as a word counter for text area 
                                                        # text = request.POST['text']
                                                        # amount = len(text.split())

                                                        # return render(request,'counter.html', {'amount':amount})
                                                        # now i use this post function 

    posts = [1,2,3,4,5,'tim','tom','tam']
    
    return render(request,'counter.html',{'posts':posts})


def post(request,pk):
    return render(request,'post.html',{'pk':pk})