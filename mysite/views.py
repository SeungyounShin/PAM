from django.shortcuts import render, get_object_or_404,redirect,render_to_response
from django.utils import timezone
from .models import Post
from .forms import PostForm, UserForm, UserProfileForm
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login

# Create your views here.

def post_list(request):
    Posts = Post.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')
    return render(request, 'mysite/post_list.html', {'posts':Posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mysite/post_detail.html', {'post':Post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.seller = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('mysite.views.post_detail',pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'mysite/post_edit.html',{'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.seller = request.user
            post.pub_date= timezone.now()
            post.save()
            return redirect('mysite/views.post_detail',pk=post.pk)
    else:
       form = PostForm(instance = post)
    return render(request, 'mysite/post_edit.html',{'form':form})

def register(request):
    context = RequestContext(request)
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfile(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()
            registered = True
        
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'mysite/register.html',
            {'user_form':user_form, 'profile_form':profile_form, 'registered': registered}, context)

def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('')
            else:
                return HttpResponse("Your PAM account is disalbed.")
        else:
             print("Invalid login details : {0}, {1}", format(username,password))
             return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('mysite/login.html',{},context)


 
