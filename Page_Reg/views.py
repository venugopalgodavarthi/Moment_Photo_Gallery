from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import signup_form
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.views.generic import CreateView, DeleteView
from Page_Reg.forms import categoriesform, Imageform, Selectcategoriesform
from Page_Reg.models import imagesmodel
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'r_login/home.html')
    # return HttpResponse("Home Page")


def signup(request):
    if request.method == 'POST':
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = signup_form()
    return render(request, 'r_login/signup.html', {'form': form})


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/images')

        else:
            return redirect('/login')
    else:
        return render(request, 'r_login/login.html')


@login_required(login_url='/login')
def next(request):
    return render(request, 'r_login/next.html')


@login_required(login_url='/login')
def logout(request):
    auth.logout(request)
    return redirect('/home')


class categoriesview(CreateView):
    template_name = "r_login/next.html"
    form_class = categoriesform
    success_url = '/success'


class DeleteImageview(DeleteView):
    template_name = "r_login/delete_confirm.html"
    model = imagesmodel
    success_url = '/gallary'


@login_required(login_url='/login')
def Imagesview(request):
    form = Imageform()
    if request.method == 'POST' and request.FILES:
        form = Imageform(request.POST, request.FILES)
        if form.is_valid():
            print(request.user)
            formsave = form.save(commit=False)
            formsave.userid = request.user
            formsave.save()
            user = request.user
            subj = "WELCOME TO MY SHOW"
            msg = "thank you for uploaded a image"
            send_mail(subj, msg, settings.EMAIL_HOST_USER, [user.email,])
            messages.success(request, "your image is uploaded")
            return redirect('/images')
        else:
            messages.error(request, "images is not uploaded")
    return render(request, "r_login/next.html", {'form': form})


def successview(request):
    return render(request, "r_login/success.html")


@login_required(login_url='/login')
def Gallaryview(request):
    res = None
    form = Selectcategoriesform()
    if request.method == 'POST':
        res = request.POST['ctname']
        res = imagesmodel.objects.filter(ctname_id=res, userid=request.user)
        return render(request, 'r_login/gallary.html', context={'form': form, 'gallarylist': res})
    elif request.method == 'GET':
        return render(request, 'r_login/gallary.html', context={'form': form})
