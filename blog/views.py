from http.client import HTTPResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    post_qs = Post.objects.all().order_by('-pk')

    return render(request, 'blog/index.html',{'post_list':post_qs,})

def post_detail(request):

    post = Post.objects.get(pk=pk)
    return 
