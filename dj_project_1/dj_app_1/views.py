from django.shortcuts import render
from django.http import HttpResponse
from dj_app_1.models import AccessRecord, Topic, Webpage, User
from . import forms
from dj_app_1.forms import NewUserForm

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, "dj_app_1/index.html", context=date_dict)
    
    my_dict = {'insert_var': 'Hello, I am from views.py'}
    return render(request, "dj_app_1/index.html", context=my_dict)

""" def Users(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users': users_list}
    return render(request, "dj_app_1/users.html", context=user_dict) """

def Users(request):
    form = forms.NewUserForm()
    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')
    return render(request, 'dj_app_1/users.html', {'form': form})

def form_name_view(request):
    form = forms.NewUserForm()
    if request.method == 'POST':
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print("First Name: " + form.cleaned_data['first_name'])
            print("Last Name: " + form.cleaned_data['last_name'])
            print("Email: " + form.cleaned_data['email'])
    return render(request, 'dj_app_1/form.html', {'form': form})