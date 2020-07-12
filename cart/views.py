from django.shortcuts import render, redirect

# Create your views here.

def add_cart(request):
    """添加购物车"""
    goods_id = request.GET.get('id', '')
    if goods_id:
        prev_url = request.META['HTTP_REFERER']
        response = redirect(prev_url)
        goods_conut = request.COOKIES.get(goods_id)
        if goods_conut:
            goods_conut = int(goods_conut) + 1
        else:
            goods_conut = 1
        response.set_cookie(goods_id, goods_conut)

    return response
