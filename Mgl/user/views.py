from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login
from .models import Profile
from .forms import UserForm, ProfileForm
from feed.models import Post

# Create your views here.

def UserCreate(request):
    if request.user.is_authenticated:
        messages.success(request, ('You already loged in!'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
    else:
        form = UserForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Profile has been created!'))
            return redirect('login')
        
        return render(request, 'register.html', {'form':form})


# def LoginView(request):
#     if request.user.is_authenticated:
#         messages.success(request, ('You already loged in!'))
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
#     else:
#         if request.method == 'POST':
#             #form = LoginForm(request.POST or None)
#             form = AuthenticationForm(request, data=request.POST)
#             if form.is_valid():
#                 login(request, user=form.get_user())
#                 messages.success(request, ('You Profile has been created!'))
#                 return redirect('home')
        
#         return render(request, 'user_form.html', {'form':form})


class UserDelete(DeleteView):
    model = User
    template_name = 'user_delete_form.html'
    success_url = reverse_lazy('home')


def ProfileUpdate(request):
    if request.user.is_authenticated:
        current_profile = get_object_or_404(Profile, user_id=request.user.id)
        form = ProfileForm(request.POST or None, request.FILES or None, instance=current_profile)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Profile has been updated!'))
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        return render(request, 'profile_update.html', {'form':form})
    else:
        messages.success(request, ('You must be Logged In to view this page!'))
        return redirect('login')

# ProfilePage
def ProfileView(request, pk):
    profile = get_object_or_404(Profile, id=pk)

    if request.method == 'POST':
        user_profile = request.user.profile
        action = request.POST.get('follow')
        if action == 'follow':
            user_profile.follow.add(profile)
        elif action == 'unfollow':
            user_profile.follow.remove(profile)
        user_profile.save()
    # Action Follow
    posts = Post.objects.filter(user=profile, deleted=False, filed=False).order_by('-created_at')
    # following = profile.follow.exclude(id=pk)
    # followers = profile.followed_by.exclude(id=pk)

    return render(request, 'profile_page.html', {'profile':profile, 'posts':posts})

# Views:
# ProfileView
# ProfileCreate 
# ProfileUpdate
# ProfileDelete

#ReviewCreate
#ReviewUpdate
#ReviewDelete <->

# ConfigView
# ConfigUpdate
