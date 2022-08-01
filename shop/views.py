from operator import iconcat
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from datetime import datetime
from .models import plots
from .models import clients
from .models import agents
from .models import blogs
from .models import Contact
from .models import stats
from .forms import agentForm
from .forms import clientForm
from .forms import blogForm
from .forms import plotForm
from .forms import statForm

# Create your views here.
def index(request):
    plots_objects = plots.objects.all()
    agents_objects = agents.objects.all()
    clients_objects = clients.objects.all()
    blogs_objects = blogs.objects.all()    
    return render(request, 'index.html',{'agents_objects':agents_objects, 'plots_objects':plots_objects, 'clients_objects':clients_objects, 'blogs_objects':blogs_objects})

def dashboard(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    plots_objects = plots.objects.all()
    agents_objects = agents.objects.all()
    clients_objects = clients.objects.all()
    blogs_objects = blogs.objects.all()
    stats_objects = stats.objects.all()

    superusers = User.objects.filter(is_superuser=True)
    message= Contact.objects.all()
    plotcount = plots_objects.count()
    agentcount = agents_objects.count()
    blogcount = blogs_objects.count()
    clientcount = clients_objects.count()
    
    return render(request, 'dashboard.html',{'agents_objects':agents_objects, 'plots_objects':plots_objects, 'clients_objects':clients_objects, 'blogs_objects':blogs_objects, 'superusers':superusers, 'plotcount':plotcount, 'clientcount':clientcount, 'blogcount':blogcount, 'agentcount':agentcount, 'message':message, 'stats_objects':stats_objects})

def search(request):
    Product_objects = plots.objects.all()
    item_name=request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        Product_objects=Product_objects.filter(description__icontains=item_name)
    return render(request, 'search.html', {'Products_objects':Product_objects})


def saleAdd(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    if request.method == "POST":
        form = statForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = statForm()
    stats_objects = stats.objects.all()
    return render(request, 'adder/saleAdd.html',{'stats_objects':stats_objects,'form':form})

def appChat(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    message= Contact.objects.all()
    return render(request, 'app-chat.html',{'message':message})



def plotAdd(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    if request.method == "POST":
        form = plotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = plotForm()
    plot = plots.objects.all()
    return render(request, 'adder/plotAdd.html',{'plot':plot,'form':form})

def agentAdd(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    if request.method == "POST":
        form = agentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = agentForm()
    agent = agents.objects.all()
    return render(request, 'adder/agentAdd.html',{'agent':agent,'form':form})

def blogAdd(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    if request.method == "POST":
        form = blogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/blogAdd")
    form = blogForm()
    blog = blogs.objects.all()
    return render(request, 'adder/blogAdd.html',{'blog':blog,'form':form})



def deleteBlog(request, pk):
	blog = blogs.objects.get(id=pk)
	if request.method == "POST":
		blog.delete()
		return redirect('/adder/blogAdd.html')
	context = {'item':blog}
	return render(request, 'deleteBlog.html', context)

def clientAdd(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    if request.method == "POST":
        form = clientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = clientForm()
    client = clients.objects.all()
    return render(request, 'adder/clientAdd.html',{'client':client,'form':form})

#these pages don't require Auth 
def about(request):
    return render(request, 'about.html')
def agent(request):
    agents_objects = agents.objects.all()
    return render(request, 'agent.html',{'agents_objects':agents_objects} )
def properties(request):
    return render(request, 'properties.html')
def blog(request):
    blogs_objects = blogs.objects.all()
    return render(request, 'blog.html', {'blogs_objects':blogs_objects})

def blogSingle(request, obj_id):
    blog_objects = blogs.objects.get(id=obj_id)
    return render(request,'blog-single.html',{'blog_objects':blog_objects})

def contact(request):
    return render(request, 'contact.html')
def contact2(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        contact=Contact(name=name, email=email, subject=subject, message=message, date= datetime.today())
        contact.save()
        messages.success(request, "Your Message Sent Successfully")
    return render(request, 'contact.html')

#These need Auth
def signupUser(request):
    form=CreateUserForm
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account Created Successfully' + user)
            return redirect('login')
    context={'form':form}
    return render(request, 'signup.html', context)

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('usernam')
        password = request.POST.get('password')
        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/dashboard")
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def resetuser(request):
    return redirect("/login")