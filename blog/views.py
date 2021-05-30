from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
  # get all posts
  data = Post.objects.all()

  # render the template by passing those "posts"
  return render(request, "index.html", {"posts":data})