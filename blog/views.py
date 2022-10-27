from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import CreateView

# Create your views here.
def index(request):
    post_qs = Post.objects.all().order_by('-pk')

    return render(request, 'blog/index.html',{'post_list':post_qs,})

def post_detail(request):

    post = Post.objects.get(pk=pk)
    return 

post_new = CreateView.as_view(
    form_class=PostForm,
    model=Post,
    success_url="/blog/",)