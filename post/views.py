from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def all_posts(request):
    posts = Post.objects.order_by('-date')#[2:]
    return render(request,'post/all_posts.html', {'posts':posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request,'post/detail.html', {'post':post})
