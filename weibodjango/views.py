from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from weibodjango.models import Headline

def weibo(request):
    return render(request, 'weibo.html')

def weibodetail(request, num):
    list = Headline.objects.all()
    # 实现分页功能
    paginator = Paginator(list, 10)
    if num > 100:
        num = 1
    page = paginator.page(num)

    return render(request, 'weibo.html', {'spotList': page})
