from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.models import Group, User
from django.contrib import messages
from .forms import SignUpForm ,SignInForm
from django.contrib.auth.forms import AuthenticationForm
from product.models import Category, Product
from django.contrib.auth import login,authenticate,logout



def home(request):
    context = dict()
    return render(request,'page/home.html',context)


def allProdCat(request, c_slug=None):
    c_page=None
    products_list=None
    if c_slug != None:
        c_page= get_object_or_404(
            Category,
            slug=c_slug
        )
        products_list = Product.objects.filter(
            category=c_page,
            avaible=True
            )
    else:
        products_list = Product.objects.all().filter(avaible=True)

    paginator = Paginator(products_list,6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage):
        products = paginator.page(paginator.num_pages)
    return render(request,'page/category.html', {'category':c_page, 'products':products})




def ProdCatDetail(request, c_slug, product_slug):
	try:
		product = Product.objects.get(category__slug = c_slug, slug=product_slug)
	except Exception as e:
		raise e
	return render(request,'page/product.html', {'product':product})



def signupView(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            messages.success(request, 'Kaydınız başarıyla oluşturuldu. Giriş yapabilirsiniz.')
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html',{'form':form})



def signinView(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home')
                else:
                    messages.info(request,'Hesabınız Engellendi')
            else:
                messages.info(request,'Yanlış kullanıcı adı veya şifre')
    else:
        form = SignInForm()
    return render(request, 'accounts/sigin.html', {'form':form})



def signoutView(request):
    logout(request)
    return redirect('home')

    
    
    


















