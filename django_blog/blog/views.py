from django.shortcuts import render, get_object_or_404
from .models import Post, Category


# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    categories = Category.objects.all()  # Fetch all categories
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})


def posts_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    posts = category.post_set.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'category': category})

