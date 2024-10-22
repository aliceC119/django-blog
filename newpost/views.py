from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import NewPost

@login_required
def create_post(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('home')  # Replace with the URL name for your post list view
        else:
            form = PostForm()
        return render(request, 'newpost/create_post.html', {'form': form})
    else:
        # return redirect('post_list')  # Redirect non-superusers
        return redirect('home')  # Redirect non-superusers

def home(request):
    newposts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})