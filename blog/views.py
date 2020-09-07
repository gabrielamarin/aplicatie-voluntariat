from django.shortcuts import render,get_object_or_404
from blog.models import Post, Comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views import generic

class Blog(generic.CreateView):
    # form_class = UserCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'blog_index.html'

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_categories.html", context)

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_details.html", context)