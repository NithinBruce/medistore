from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import ProductForm
from .models import Medicine

def home(request):
     return render(request,'home.html')

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text=None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

#Function for signup
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('login')
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


#Function for login
def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

            user = form.get_user()
            login(request,user)
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

#Function For logout
@login_required(login_url='/login/')
def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')

    context = {
        'user': request.user
    }

    return render(request, 'logout.html', context)



#function for add and list 
def welcome(request):
     return render(request,'welcome.html')


#Function for adding medicine
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form =ProductForm()
    return render(request, 'add.html', {'form': form})


#Function for listing medicine
def product_read(request):
    medicine_list=Medicine.objects.all()
    return render(request,'list.html',{'medicine_list':medicine_list})

    

#Function for updating medicine
def product_update(request, pk):
    product = Medicine.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form =ProductForm(instance=product)           
    return render(request, 'update.html', {'form': form})


#Function for delete medicine
def product_delete(request,pk):
    product=Medicine.objects.get(pk=pk)  
    if request.method == 'POST':
        product.delete()
        return redirect('list')
    
    return render(request,'delete.html',{'product':product})


#Function for searching medicine
def search(request):
    if request.method == "GET":
        query = request.GET.get('query')
        if query:
            medicines = Medicine.objects.filter(name__istartswith=query)
            if medicines:
                return render(request, 'searchbar.html', {'medicines': medicines})
        return render(request, 'noresult.html')
         