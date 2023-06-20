from django.db.models import Count
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .models import Post
from .forms import PostForms


# Create your views here.


# Views:
# FeedView - Lista de posts
# PostView
# PostCreate
# PostUpdate - Tempo limite (10 min) - Marcação (edited) - Notificação para profiles que deram like
# PostDelete

def FeedView(request):
    if request.user.is_authenticated:
        form = PostForms(request.POST or None, request.FILES)
        if request.method == 'POST':
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user.profile
                post.edited = False
                post.deleted = False
                post.filed = False
                post.save()
                messages.success(request, ('Your Post Has Been Posted!'))
                return redirect('feed')
    
        posts = Post.objects.filter(post_father=None, deleted=False, filed=False).order_by('-created_at')
        return render(request, 'feed.html', {'posts': posts, 'form': form})
    
    else:
        posts = Post.objects.filter(post_father=None, deleted=False, filed=False).order_by('-created_at')
        return render(request, 'feed.html', {'posts': posts})
    
def PostView(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.deleted or (post.filed and not post.user == request.user.profile):
        # Retorna para página de erro, 404
        return redirect('feed')
    
    if request.user.is_authenticated:
        form = PostForms(request.POST or None, request.FILES)
        if request.method == 'POST':
            post_father = get_object_or_404(Post, id=pk)
            if form.is_valid() and not (post_father.deleted or post_father.filed):
                post = form.save(commit=False)
                post.user = request.user.profile
                post.edited = False
                post.deleted = False
                post.filed = False
                post.post_father = post_father.id
                post.save()
                messages.success(request, ('Your Comment Has Been Posted!'))
                return HttpResponseRedirect(request.path_info)

        posts = Post.objects.filter(post_father=pk, deleted=False, filed=False).annotate(q_count=Count('likes')).order_by('-q_count', '-created_at')
        return render(request, 'feed/post.html', {'post': post, 'posts': posts, 'form': form})
    
    else:
        posts = Post.objects.filter(post_father=pk, deleted=False, filed=False).annotate(q_count=Count('likes')).order_by('-q_count', '-created_at')
        return render(request, 'feed/post.html', {'post': post, 'posts': posts})

    
def PostLike(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.deleted or post.filed:
        # Retorna para página de erro, 404
        return redirect('feed')
    
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id):
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    else:
        messages.success(request, ('Your Must Been Loged In!'))
        # Retornar para página de login
        return redirect('login')
    
def PostDelete(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.deleted:
        # Retorna para página de erro, 404
        return redirect('feed')
    
    if request.user.is_authenticated:
        if request.user.profile == post.user:
            post.deleted = True
            post.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        else:
            messages.success(request, ('What are you doing!?'))
            # Retorna para página de erro, 404
            return redirect('feed')
        
    else:
        messages.success(request, ('Your Must Been Loged In!'))
        # Retornar para página de login
        return redirect('login')

def PostFile(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.deleted:
        # Retorna para página de erro, 404
        return redirect('feed')
    
    if request.user.is_authenticated:
        if request.user.profile == post.user:
            post.filed = not post.filed
            post.save()

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        else:
            messages.success(request, ('What are you doing!?'))
            # Retorna para página de erro, 404
            return redirect('feed')
        
    else:
        messages.success(request, ('Your Must Been Loged In!'))
        # Retornar para página de login
        return redirect('login')
    
class PostUpdate(UpdateView):
    model = Post
    form_class = PostForms
    template_name = template_name = 'feed/update.html'

    def form_valid(self, form):
        form.instance.edited = True
        self.pk = form.instance.id
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post', kwargs={'pk': self.pk})
