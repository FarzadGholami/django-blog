# from django.shortcuts import render
# from django.shortcuts import get_object_or_404, redirect, reverse
# from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


# def post_list_view(request):
#     # posts_list = Post.objects.all()
#     posts_list = Post.objects.filter(status='pub').order_by('-datetime_modified')  # kwargs
#     return render(request, 'blog/posts_list.html', {'posts_list': posts_list})


class PostListView(generic.ListView):
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts_list'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-datetime_modified')


# def post_detail_view(request, pk):
#     post_detail = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post_detail})
#

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('posts_list')
#     else: #get request
#         form = PostForm()
#
#     return render(request, 'blog/post_create.html', context={'form': form})

# ImproperlyConfigured at /blog/create/
# No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.


class PostCreateView(generic.CreateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('posts_list')
#     return render(request, 'blog/post_create.html', context={'form': form})


class PostUpdateView(generic.UpdateView):
    form_class = PostForm
    template_name = 'blog/post_create.html'
    model = Post


# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog/post_delete.html', context={'post': post})

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts_list')

