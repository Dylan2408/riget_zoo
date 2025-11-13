from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, Zoo_Booking_Form
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate


# Create your views here.

#def home(request):
    #return render(request, 'pages/index.html')

from django.http import HttpResponse

def home(request):
    return render(request, 'pages/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}

    return render(request,'pages/register.html', context=context)

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')

            user = authenticate(request, username=username, password=password, email=email)

            if user is not None:
                auth.login(request, user)
                return redirect('home')

    context = {'login_form':form}
    return render(request,'pages/login.html', context=context)

def user_logout(request):

    auth.logout(request)
    return redirect("login")

#@login_required(login_url='login')
def zoo(request):

    form = Zoo_Booking_Form()

    if request.method == "POST":
        obj = form.save(commit=False) # return an object without saving to the DB

        updated_request = request.POST.copy()
        updated_request.update({'hotel_user_id_id': request.user})

        form = Zoo_Booking_Form(updated_request)

    if form.is_valid():

        zoo_total_cost = int(obj.zoo_booking_adults) * 40 \
                              + int(obj.zoo_booking_children) * 20 \
                              + int(obj.zoo_booking_oap) * 25 \
        
        zoo_total_cost *= int(zoo_total_cost)

        obj.zoo_total_cost = zoo_total_cost
        obj.zoo_user_id = request.user

        obj.save()

        message.success(request, "Ticket booked successfully")
        return redirect('zoo')
    else:
        print("There was a problem with your purchase, try again.")
        print(form.errors)
        #return redirect('zoo')

    context = {'form': form}

    return render(request, 'pages/zoo.html', context=context)