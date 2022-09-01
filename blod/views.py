from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from .models import Post


def list_post_view(request):
    # post_list = Post.objects.all()# bra ine ke hame ro biyare
    post_list = Post.objects.filter(status='pub')
    return render(request, 'blog/post_list.html', {'list_post': post_list})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)  # این خط میاد خودش در خودش ترای و اسپت رو انجام میده
    # میگه من میرم داخل جدول پست اگر چیزی با این اطلاعات رو پیدا کردم که حله
    # اما اگر گشتم و پیداش نکردم ارور 404 میدم

    # try:
    #     detail = Post.objects.get(pk=pk)
    # except ObjectDoesNotExist:#جامع تر
    # # except post.DoesNotExist: مخصوص همون مدلی ک ساختیم
    #     detail = None
    #     print('Excepted')

    return render(request, 'blog/post_detail.html', {'post': post})
