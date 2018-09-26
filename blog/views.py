from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Post

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'blog_list'
    
    def get_queryset(self):
        """Return the all Posts"""
        return Post.objects.all()

class DetailView(generic.DetailView):
    template_name = 'blog/detail.html'
    context_object_name = "blog_detail"

    def get_object(self):
        _id = self.kwargs.get("id")
        return get_object_or_404(Post, id=_id)
    