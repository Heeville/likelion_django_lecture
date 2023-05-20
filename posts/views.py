from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse,Http404
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from.forms import PostBaseForm,PostCreateForm
from .models import Post
# Create your views here.
def index(request):
    post_list=Post.objects.all().order_by('-create_at')
    context={
        'post_list':post_list,
    }
    return render(request,'index.html',context)

def post_list_view(request):
    post_list=Post.objects.all()
    #post_list=Post.objects.filter(writer=request.user)
    context={
        'post_list':post_list,
    }
    return render(request,'posts/post_list.html',context)

def post_detail_view(request,id):
    try:
        post=Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')
    context={
        'post':post,
    }
    return render(request,'posts/post_detail.html',context)

@login_required
def post_create_view(request):
    if request.method=='GET':
        return render(request,'posts/post_form.html')
    else:
        image=request.FILES.get('image')
        content=request.POST.get('content')
        print(image)
        Post.objects.create(
            image=image,
            content=content,
           writer=request.user
        )
        return redirect('index')
    
def post_create_form_view(request):
    if request.method=='GET':
        #form=PostBaseForm()
        form=PostCreateForm()
        context={'form':form}
        return render(request,'posts/post_form2.html',context)
    else:
        form=PostBaseForm(request.POST,request.FILES)
        if form.is_valid():
            Post.objects.create(
                image=form.cleaned_data['image'],
                content=form.cleaned_data['content'],
                writer=request.user
            )
        else:
            return redirect('posts:create')
        return redirect('index')
    
    

def post_update_view(request,id):
    #post=Post.objects.get(id=id)
    post=get_object_or_404(Post,id=id,writer=request.user)
    if request.method=='GET':
        context={'post':post}
        return render(request,'posts/post_form.html',context)
    elif request.method=='POST':
        nimage=request.FILES.get('image')
        content=request.POST.get('content')
        
        if nimage:
            post.image.delete()
            post.image=nimage
            
        post.content=content
        post.save()
        return redirect('posts:detail',post.id)

@login_required
def post_delete_view(request,id):
    post=get_object_or_404(Post,id=id)
    if request.user!=post.writer:
        raise Http404('잘못된 접근')
    
    if request.method=='GET':
        context={'post':post}
        return render(request,'posts/post_confirm_delete.html',context)
    else:
        post.delete()
        return redirect('index')


def url_view(request):
    data={'code':'001','msg':'ok'}
    return HttpResponse('<h1>url_view</h1>')
    #return JsonResponse(data)
    

def url_parameter_view(request,username):
    print(f'username:{username}')
    print(request.GET)
    return HttpResponse(username)

def function_view(request):
    print(f'request.method:{request.method}')
    if request.method=='GET':    
        print(f'request.GET:{request.GET}')
    elif request.method=='POST':
        print(f'request.POST:{request.POST}')
    return render(request,'view.html')

class class_view(ListView):
    model=Post
    template_name='cbv_view.html'
    