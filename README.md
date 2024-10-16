# Blog Application with Categories
This project will build on the fundamentals from the first project, focusing on Django's ORM, relationships, and the template system. We'll also introduce more complex model relationships such as Categories and Posts.

## Project Overview
Objective: Create a blog system where users can add blog posts and categorize them. Each post should belong to one or more categories.
Features:
1. Create and manage blog posts.
2. Assign posts to categories.
3. List posts by category.
4. Display post details.
5. Optional: Allow users to filter posts by category.

## Step-by-Step Plan:

### Step 1: Create project and app
pip install django
django-admin startproject django_blog
cd django_blog
python manage.py startapp blog

### Step 2: Update Settings


INSTALLED_APPS = [
    ...,
    'blog',
]

### Step 3: Create Models for Blog and Categories


from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


### Step 4: Create Database Migrations

python manage.py makemigrations
python manage.py migrate


### Step 5: Create a Superuser


python manage.py createsuperuser

### Step *: Run server
python manage.py runserver

### Step 6: Register Models in the Admin

Update admin.py

from django.contrib import admin
from .models import Category, Post

admin.site.register(Category)
admin.site.register(Post)

Now you can manage categories and posts from the Django admin panel.


### Step 7: Set Up Views ,URLS and Templates

#### Views

from django.shortcuts import render, get_object_or_404
from .models import Post, Category

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

#### URLS

Include blog URLs in your main project’s urls.py:

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

Create urls.py inside the blog app:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('category/<int:category_id>/', views.posts_by_category, name='posts_by_category'),
]

#### Templates
1. templates/blog/post_list.html:


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <ul>
        {% for post in posts %}
            <li>
                <a href="{% url 'post_detail' post.id %}">{{ post.title }}</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>

2. templates/blog/post_detail.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <p>Categories: 
        {% for category in post.categories.all %}
            {{ category.name }}{% if not forloop.last %}, {% endif %}
        {% endfor %}
    </p>
</body>
</html>

3. Add category filtering to post_list.html
<h2>Categories</h2>
<ul>
    {% for category in categories %}
        <li><a href="{% url 'posts_by_category' category.id %}">{{ category.name }}</a></li>
    {% endfor %}
</ul>
