import time
from django.http import HttpResponse

from django.shortcuts import render, redirect

# Create your views here.
from cart.models import OrderInfo, OrderGoods
from goods.models import GoodsInfo


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

def show_cart(request):
    '''购物车商品详情页面'''
    cart_goods_list = []
    cart_goods_count = 0
    cart_goods_money = 0

    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods.total_money = int(goods_num) * cart_goods.goods_price
        cart_goods_list.append(cart_goods)

        cart_goods_count += int(goods_num)
        cart_goods_money += int(goods_num) * cart_goods.goods_price

    return render(request, 'cart.html', {'cart_goods_list': cart_goods_list,
                                         'cart_goods_count': cart_goods_count,
                                         'cart_goods_money': cart_goods_money})

def remove_cart(request):
    '''删除商品'''
    goods_id = request.GET.get('id', '')
    if goods_id:
        prev_url = request.META['HTTP_REFERER']
        response = redirect(prev_url)
        goods_count = request.COOKIES.get(goods_id, '')
        if goods_count:
            response.delete_cookie(goods_id)

    return response

def place_order(request):
    '''提交订单页面'''
    cart_goods_list = []
    cart_goods_count = 0
    cart_goods_money = 0

    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_num = goods_num
        cart_goods.total_monkey = cart_goods.goods_price * int(goods_num)
        cart_goods_list.append(cart_goods)
        cart_goods_count += int(goods_num)
        cart_goods_money += cart_goods.goods_price * int(goods_num)

    return render(request, 'place_order.html', {'cart_goods_list': cart_goods_list,
                                                'cart_goods_count': cart_goods_count,
                                                'cart_goods_money': cart_goods_money})

def submit_order(request):
    '''提交订单功能'''
    addr = request.POST.get('addr', '')
    recv = request.POST.get('recv', '')
    tele = request.POST.get('tele')
    extra = request.POST.get('extra')

    order_info = OrderInfo()

    order_info.order_addr = addr
    order_info.order_tele = tele
    order_info.order_recv = recv
    order_info.order_extre = extra

    order_info.order_id = str(time.time() * 1000) + str(time.clock() * 1000000)

    order_info.save()

    response = redirect('cart/submit_success/?id=%s' % order_info.order_id)

    for goods_id, goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        order_goods = OrderGoods()
        order_goods.goods_info = cart_goods
        order_goods.goods_num = goods_num
        order_goods.goods_order = order_info
        order_goods.save()

        response.delete_cookie(goods_id)

    return response

def submit_success(request):
    '''订单提交成功 '''
    order_id = request.GET.get('id')
    orderinfo = OrderInfo.objects.get(order_id=order_id)
    order_goods_list = OrderGoods.objects.filter(goods_order=orderinfo)

    total_money = 0
    total_num = 0

    for goods in order_goods_list:
        goods.total_money = goods.goods_info.goods_price * goods.goods_num
        total_money += goods.total_money
        total_num += goods.goods_num


    return render(request, 'success.html', {'orderinfo': orderinfo,
                                            'order_goods_list': order_goods_list,
                                            'total_money': total_money,
                                            'total_num': total_num})

def testcsrf(request):
    return render(request, 'testcsrf.html')

def test(request):
    return HttpResponse('testok')