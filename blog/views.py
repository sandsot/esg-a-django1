from django.shortcuts import render, redirect
from django.views.generic import CreateView
from blog.forms import PostForm
from blog.models import Post, Restaurant
from blog.rest_form import RestaurantForm


# Create your views here.
def index(request):
    post_qs = Post.objects.all().order_by('-pk')
    return render(request, "blog/index.html",
    {'post_list':post_qs,
    })

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/single_post_page.html",{
        "post": post,
        })

# post_new = CreateView.as_view(
#     form_class=PostForm,
#     model=Post,
#     success_url="/blog/",)

def post_new(request):
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            # 유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect("/blog/")
            # return redirect(f'/blog/{post.pk}/")
            # return redirect(post.get_absolute_url())
            return redirect(post)


    return render(request, "blog/post_form.html",{
        "form": form
        })

def restaurant_index(request):
    rest = Restaurant.objects.all().order_by('-pk')
    return render(request, "blog/restaurant_index.html",
    {'rest_qs':rest,
    })

def res_new(request):
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == 'GET':
        form = RestaurantForm()
    else:
        form = RestaurantForm(request.POST)
        if form.is_valid():
            # 유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect("/blog/")
            # return redirect(f'/blog/{post.pk}/")
            # return redirect(post.get_absolute_url())
            return redirect(post)
    return render(request, "blog/res_form.html",{
        "form": form
        })

def res_post_page(request, pk):
    rest = Restaurant.objects.get(pk=pk)

    if request.method == 'POST':
        memory.delete()
        return redirect("/diary/")

    return render(request, "blog/res_post_page.html",{
        "rest_qs": rest,
        })