import os, django

from django.core.paginator import Paginator

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ttsx.settings")# project_name 项目名称
django.setup()

from django.shortcuts import render
from django.http import HttpResponse
from goods.models import GoodsInfo, GoodsCategory

# Create your views here.

# 视图是一个函数  必须传一个参数request请求对象  里面有用户发送的请求信息 比如URL
def index(request):
    """首页"""
    # 查询商品的分类
    categories = GoodsCategory.objects.all()

    # 从每个分类中，获取4个商品（每一类的最后4个，最新的）
    for cag in categories:
        # GoodsInfo.objects.filter(goods_cag=cag)
        # 一对多关系 查询多的一方 会在一的这一方有一个属性 多的一方的 模型类名小写_set
        # cag.goodsinfo_set.all()
        # order_by是排序 这里是根据id反向排序（大->小） [:4]获取结果里的前面4个 切片
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]

    # 获取购物车里所有的商品  cookie  key:value  商品的id：数量  cookie存到都是字符串
    # 购物车商品的列表
    cart_goods_list = []
    # 购物车的商品总数量
    cart_goods_count = 0

    for goods_id, goods_num in request.COOKIES.items():
        # 商品id都是数值，通过判断来验证当前是不是商品数据 如果不是继续下次的循环
        if not goods_id.isdigit():
            continue
        # 获取当前便利到的商品的对象
        cart_goods = GoodsInfo.objects.get(id = goods_id)
        cart_goods.goods_num = goods_num
        # 把商品存放到列表里
        cart_goods_list.append(cart_goods)
        # 累加所有商品的数量 注意goods_num是字符串 需要强转成数字类型
        cart_goods_count = cart_goods_count + int(goods_num)

    # 购物车的商品总数量

    request.COOKIES

    # 参1是请求的对象request 参2是需要返回的html页面 参3需要传入到模板的数据
    return render(request, 'index.html', {'categories': categories,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count})

def detail(request):
    """商品详情页面"""
    # 商品的分类
    categories = GoodsCategory.objects.all()
    # 购物车数据
    # 所有的购物车商品
    cart_goods_list = []
    # 购物车商品的总数量
    cart_goods_count = 0
    # 去cookie取数据  goods_id:count
    for goods_id,goods_num in request.COOKIES.items():
        # 验证是不是商品数据
        if not goods_id.isdigit():
            continue
        # 根据id查询商品
        cart_goods = GoodsInfo.objects.get(id = goods_id)
        # 把商品数量 存放到商品的对象里
        cart_goods.goods_num = goods_num
        # 把商品添加到列表里
        cart_goods_list.append(cart_goods)
        # 累加所有商品数量，得到总的数量
        cart_goods_count = cart_goods_count + int(goods_num)

    goods_id = request.GET.get('id', 1)
    goods_date = GoodsInfo.objects.get(id=goods_id)
    return render(request, 'detail.html', {'categories': categories,
                                           'cart_goods_list': cart_goods_list,
                                           'cart_goods_count': cart_goods_count,
                                           'goods_date': goods_date})

def goods(request):
    """商品分类页"""
    cag_id =request.GET.get('cag', 1)
    page_id = request.GET.get('page', 1)


    current_cag = GoodsCategory.objects.get(id=cag_id)
    goods_date = GoodsInfo.objects.filter(goods_cag_id=cag_id)

    paginator = Paginator(goods_date, 12)
    page_date = paginator.page(page_id)


    categories = GoodsCategory.objects.all()

    cart_goods_list = []
    cart_goods_count = 0
    for goods_id,goods_num in request.COOKIES.items():
        if not goods_id.isdigit():
            continue
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goods_name = goods_num
        cart_goods_list.append(cart_goods)
        cart_goods_count = cart_goods_count + int(goods_num)

    return render(request, 'goods.html', {'current_cag': current_cag,
                                          'page_date': page_date,
                                          'categories': categories,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count,
                                          'paginator': paginator,
                                          'cag_id': cag_id})