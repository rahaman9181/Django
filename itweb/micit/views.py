# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password,is_password_usable,get_hasher,check_password
from .forms import PostForm,LoginForm
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
li=[]
# c="17H71A"
#b=1200
d=""
for i in range(1201,1261):
    b=0
    b=b+i
    d="17H71A"+str(b)
    #print(d)
    li.append(d)
    d=""



def login_form(request):
    form=LoginForm(request.POST or None)
    return render(request,'login.html',{'form':form})


def register(request):
    if request.method=="POST":
        first_name=request.POST["first_name"]
        last_name=request.POST['last_name']
        username=request.POST['username'].upper()
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if username not in li:
                messages.info(request,"User Name Should be Your Roll No")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name,password=password1)
                user.save()
                messages.info(request,"User Created")
                return redirect('login')
        else:
            messages.info(request,"Password not matching...")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username'].upper()
        password=request.POST['password']
        # print(password)
        # print(b)
        # print(make_password('password'))
        user=auth.authenticate(username=username,password=password)
        # print(user.check_password('password','pbkdf2_sha256$150000$DKfi7HUY18En$r1WxGKerV5W6BF5wXi/hAhSt5Kx+oGhLN7C+fX+gm7U='))
        if user is not None:
            auth.login(request,user)
            # print(is_password_usable(password))
            v=make_password('password')
            print (user.check_password(password))
            # pritnt(user.get_hasher())
            return redirect("/")
        else:
            messages.info(request,"Inavlid Credentials")
            return redirect("login")
    else:
        return render(request,"login.html")


@login_required()
def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request,'home.html')

@login_required()
def password_change(request):
     if request.method=='POST':
        # return render(request,'change_password.html')
        username=request.POST['username'].upper()
        password=request.POST['password']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            # if request.user:
            user=auth.authenticate(username=username,password=password)
                # print("Hello")
            if user is not None and check_password(request.POST['password'], user.password):

                  #?? ???? ??
                messages.info(request,'Password Changed')
                user.set_password(request.POST['password1'])  # ??? ???? ??.
                user.save()
                return render(request,"login.html")
            elif user is None:
                messages.info(request,'Enter Valid Credentials')
                return render(request,"password_change.html")
        else:
            messages.info(request,'Failed to change password') # message? ?? ?? ??
            return render(request,"password_change.html")
        return render(request,'home.html')
     else:
         return render(request,'password_change.html')

def password(request):
    return render(request,'password_change.html')

# @login_required()
def post_list(request):
    # posts = IT_Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    pdfs=IT_Posts.objects.all().order_by('-date')
    paginator = Paginator(pdfs, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'pdfs': paged_listings
    }

    return render(request, 'post_list.html', context)

    # def listing(request, listing_id):
    #   listing = get_object_or_404(Listing, pk=listing_id)
    #
    #   context = {
    #     'pdfs': listing
    #   }




    # return render(request,'post_list.html', {'pdfs':pdfs})

@login_required()
def upload_post(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.posted=request.user
            # form.posted=request.user.username
            instance.save()
            return redirect('post_list')
    else:
        form=PostForm()
    return render(request,'upload_post.html',{'form':form})

def delete_post(request,pk):
    if request.method=='POST':
        pdf=IT_Posts.objects.get(pk=pk)
        print(pdf)
        pdf.delete()
    return redirect('post_list')
