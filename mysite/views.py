from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    Posts = Post.objects.filter(pub_date__lte = timezone.now()).order_by('-pub_date')
    return render(request, 'mysite/post_list.html', {'posts':Posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'mysite/post_detail.html', {'post':Post})
