from django.shortcuts import redirect, render
from .models import Post
# Create your views here.
def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts': posts})


def post_like(request):
    if request.method == 'POST':
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
    return redirect('post_like')