"""ttsx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from cart.views import add_cart, show_cart, remove_cart, testcsrf, place_order, submit_order, submit_success, test
from goods.views import index, detail, goods

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 参1是要访问的url地址的正则匹配  参2是要访问的视图的函数名字
    url(r'^index/$', index),  # 首页
    url(r'^detail/$', detail),  # 详情页
    url(r'^cart/add_cart/$', add_cart),  # 添加到购物车
    url(r'^goods/$', goods),  # 商品分类页面
    url(r'^cart/show_cart/$', show_cart),  # 购物车页面
    url(r'^cart/remove_cart/$', remove_cart),  # 购物车删除商品
    url(r'^cart/place_order/$', place_order),  # 提交订单页面
    url(r'^cart/submit_order/$', submit_order),  # 提交订单功能
    url(r'^cart/submit_success/$', submit_success),  # 提交订单成功页面
    url(r'^testcsrf/$', testcsrf),  # csrf详解
    url(r'^test$', test),  # csrf详解
]
