from django.shortcuts import render,redirect
from .forms import UserCreateForm,SignUpForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
# Create your views here.

def signup_view(request):
    #get 요청 시 HTML 응답
    if request.method=='GET':
        form=SignUpForm
        context={'form':form}
        return render(request,'accounts/signup.html',context)
    else:
        #post 요청 시 데이터 확인 후 회원 생성
        form=SignUpForm(request.POST)
        
        if form.is_valid():
            # #회원가입처리
            # form.cleaned_data['username']
            # form.cleaned_data['email']
            # form.cleaned_data['password2']  
            instance=form.save()
            return redirect('index')  
        else:
            return redirect('accounts:signup')
        
        
def login_view(request):
    #get.post divide
    if request.method=='GET':
        return render(request,'accounts/login.html',{'form':AuthenticationForm()})
    else:
        #데이터 유효성 검사
        form=AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            # 비즈니스 로직 처리
            login(request,form.user_cache)
            #응답
            return redirect('index')
            pass
        else:
            
            return redirect(request,'accounts/login.html',{'form':form})
    #data velidation
    #take business logic
    #response
    
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')