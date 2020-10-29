from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from .models import Profile, Comment, Image, Follow
from .forms import SignUpForm, StoryForm, CommentForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 


# Create your views here.
def registerPage(request):
     if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'Account has been created Successfully for ' + user)
            return redirect('feeds.html')
     else:
        form = SignUpForm()
        return render(request, 'registration/registration_form.html', {'form': form})



@login_required(login_url='/accounts/login/')
def feeds(request):
    images = Image.get_images()
    comments = Comment.get_comment()
    profile = Profile.get_profile()

    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('feeds')

    else:
        form = CommentForm()

    return render(request,"feeds.html",{"images":images, "comments":comments,"form": form,"profile":profile})
@login_required
def profile(request,profile_id):

    profile = Profile.objects.get(user=request.user)
    images = Image.objects.filter(profile_id=profile).all()

    return render(request,"instaflex/profile.html",{"profile":profile,"images":images})

@login_required(login_url='/accounts/login/')
def search_results(request):
    
    if 'insta' in request.GET and request.GET["insta"]:
        search_term = request.GET.get("insta")
        searched_instas = Insta.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"instas": searched_instas})

    else:
     message = "Connect with people from all over the wolrd"
     return render(request, 'instaflex/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def get_post_by_id(request,image_id):

    image = Image.objects.get(id = image_id)
    comment = Image.objects.filter(id = image_id).all()

    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.posted_by = current_user
            image.save()
        return redirect('feeds')

    else:
        form = CommentForm()

    return render(request,"instaflex/post.html", {"image":image,"comment":comment,"form": form})


@login_required(login_url='/accounts/login/')
def comment(request,pk):
    image = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.poster = current_user
            comment.save()
            return redirect('feeds')
    else:
        form = CommentForm()
        return render(request,'instaflex/comment.html',{"user":current_user,"comment_form":form})

@login_required(login_url='/accounts/login/')
def story(request):
    current_user = request.user
    profiles = Profile.get_profile()
    profile = request.user.profile
    if request.method == 'POST':
        form = StoryForm(request.POST,request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.posted_by = current_user
            upload.profile = profile
            upload.save()
            return redirect('feeds')

    else:
        form = StoryForm()
    return render(request,'instaflex/story.html',{"user":current_user,"form":form})


def follow(request,operation,id):
    current_user=User.objects.get(id=id)
    if operation=='follow':
        Follow.follow(request.user,current_user)
        return redirect('feeds')
    elif operation=='unfollow':
        Follow.unfollow(request.user,current_user)
        return redirect('feeds')

#def unfollow(request,operation,id):
#    current_user=User.objects.get(id=id)
#    if operation=='unfollow':
#        Follow.follow(request.user,current_user)
#        return redirect('feeds')
#    elif operation=='follow':
#        Follow.unfollow(request.user,current_user)
#        return redirect('feeds')

@login_required(login_url='/accounts/login/')
def pillow(request, pk):
    profile = Profile.objects.get(user=request.user)
    images = Image.objects.all().filter(posted_by_id=pk)
    content = {
        "profile": profile,
        'images': images,
    }
    return render(request, 'instaflex/pillow.html', content)

#@login_required(login_url='/accounts/login/')
#def feeds_section(request, section):
#   images = Image.filter_by_section(section)
#    print(images)
#    return render(request, 'instaflex/section.html', {'section_images': images})


@login_required(login_url="/accounts/login/")
def like(request,operation,pk):
    image = get_object_or_404(Image,pk=pk)

    if operation == 'like':
        image.likes += 1
        image.save()
    elif operation =='unlike':
        image.likes -= 1
        image.save()
    return redirect('feeds')
