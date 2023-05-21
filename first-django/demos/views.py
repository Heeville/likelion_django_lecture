from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calculator(request):
    #데이터 확인 
    num1=request.GET.get('num1')
    num2=request.GET.get('num2')
    operator=request.GET.get('operator')
    
    #계산
    if operator=='+':
        result=int(num1)+int(num2)
    elif operator=='-':
        result=int(num1)-int(num2)
    elif operator=='*':
        result=int(num1)*int(num2)
    elif operator=='/':
        result=int(num1)/int(num2)
    else:
        result=0; 
    
    #응답
    return render(request, 'calculator.html',{'result':result})
    # return HttpResponse('계산기 기능 구현')
    
