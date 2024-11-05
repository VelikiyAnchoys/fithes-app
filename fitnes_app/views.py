from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Zal, Abonement, Trener, Pitanie, DomTrenirovki, SpecTren
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm 


def home_page(request):
    categories = Category.objects.all()
    zals=Zal.objects.all()
    context={
        'categories':categories,
        'zals':zals
    }

    return render(request, "./home.html", context)
    
def zal_page(request):
    zals=Zal.objects.all()
    context={
        'zals':zals
    }
    return render(request,"./club.html", context)

def categories_page(request):

    categories = Category.objects.all()
    context={
        'categories':categories
    }
    return render(request,"./categories.html", context)

def abonement_page(request):  
    abonements = Abonement.objects.all()
    context={
        'abonements':abonements
    }
    return render(request,"./abonements.html", context)

def zal_detail_page(request, pk):  
    zal= get_object_or_404(Zal, pk=pk)
    context = {
        'zal': zal
    }
    return render(request, "./zal_detail.html", context)

def trener_page(request):
    treners= Trener.objects.all()
    context={
        'treners':treners
    }
    return render(request,"./treners.html", context)    


def trener_detail_page(request, pk):  
    trener= get_object_or_404(Trener, pk=pk)
    context = {
        'trener': trener
    }
    return render(request, "./trener_detail.html", context)

def pitanie_page(request):
    pitanies= Pitanie.objects.all()
    context={
        'pitanies':pitanies
    }
    return render(request,"./pitanies.html", context)

def pitanie_detail_page(request, pk):  
    pitanie= get_object_or_404(Pitanie, pk=pk)
    context = {
        'pitanie': pitanie
    }
    return render(request, "./pitanie_detail.html", context)    


def trendom_page(request):
    trendoms= DomTrenirovki.objects.all()
    context={
        'trendoms': trendoms
    }
    return render(request, "./trendoms.html", context)


def spectren_page(request):
    spectrens=SpecTren.objects.all()
    context={
        'spectrens':spectrens
    }
    return render(request, "./spectrens.html", context)


def zals_by_category_page(request, slug):
    category= get_object_or_404(category, slug=slug)
    zals = Category.filter(category=category)
    context={
        'category': category
    }
    return render(request, "./post-by-category.html", context)

    
def sign_up_page(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
    else:
        form= NewUserForm()
        context={
            'form':form
        }
        return render(request, "./sign-up.html", context)

def login_page(request):
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')  
            user = authenticate( username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
    else:
        form = AuthenticationForm()

        context={
            'form':form
        }    
        return render(request, "./login.html", context)
       


def logout_action(request):
    logout(request)
    return redirect('home_page')



def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = ImageUploadForm()

    images = ImageUpload.objects.all()
    return render(request, 'upload.html', {'form': form, 'images': images})    


def abon_purchase(request):
    return render(request, 'abon_purchase.html')


def spectren_detail_page(request, pk):  
    spectren= get_object_or_404(SpecTren, pk=pk)
    context = {
        'spectren': spectren
    }
    return render(request, "./spectren_detail.html", context)    