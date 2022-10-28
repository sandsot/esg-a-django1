from django.contrib import messages
from django.shortcuts import render, redirect
from diary.models import Memory
from django.views.generic import CreateView
from diary.forms import DiaryForm

def memory_list(request) :
    posts = Memory.objects.all().order_by('-pk')
    return render(
        request,
        'diary/memory_list.html',
        {
            'posts' : posts,
        }
    )

def memory_detail(request, pk):
    post = Memory.objects.get(pk=pk)
    
    return render(
        request,
        'diary/memory_detail.html',
        {
        'post':post,
        }
    )   



def memory_new(request):

    if request.method == "GET":
        form = DiaryForm()
    else :
        form = DiaryForm(request.POST)
        if form.is_valid() :
            post = form.save()
            messages.success(request,"메모리 생성")
            return redirect(post)
            # return redirect(f"/diary/{post.pk}/")
        
    return render(request, "diary/memory_new.html", {
        "form" : form,
    })


def memory_edit(request,pk):
    memory = Memory.objects.get(pk=pk)

    if request.method == "POST":
        form = DiaryForm(request.POST, instance=memory)
        if form.is_valid():
            # form.cleaned_data
            memory = form.save()
            messages.success(request, "메모리를 저장했습니다.")
            # return redirect(f"/diary/{memory.pk}/")
            # return redirect(memory.get_absolute_url())
            return redirect(memory)
    else:
        form = DiaryForm(instance=memory)
    return render(request, "diary/memory_new.html", {
        "form": form,
    })

def memory_delete(request,pk):
    memory = Memory.objects.get(pk=pk)
    # TODO: delete memory
    # delete memory
    if request.method == "POST":
        memory.delete()
        messages.success(request, "메모리를 삭제했습니다.")
        return redirect("/diary/")

    return render(request, "diary/memory_comfirm_delete.html", {
        'memory' : memory,
    })