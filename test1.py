import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ttsx.settings")# project_name 项目名称
django.setup()
from goods.models import *

# # 商品分类表插入数据
# categories = [('时令水果', 'fruit', 1),
#               ('海鲜水产', 'seafood', 2),
#               ('全品肉类', 'meet', 3),
#               ('美味蛋品', 'egg', 4),
#               ('新鲜蔬菜', 'vegetables', 5),
#               ('低温奶制品', 'ice', 6)]
#
# for cag in categories:
#     c = GoodsCategory()
#     c.cag_name = cag[0]
#     c.cag_css = cag[1]
#     c.cag_img = 'images/banner0%d.jpg'%cag[2]
#     c.save()

# # 商品详情表插入数据
# goods = GoodsInfo()
# goods.goods_name = '新疆库尔勒香梨5斤'
# goods.goods_price = 79
# goods.goods_img = 'xiangli'
# goods.goods_desc = '库尔勒香梨果面光滑，香气浓郁，酥脆爽口'
# goods.goods_cag_id = 1
# goods.save()


# 数据库查询
goods = GoodsInfo.objects.get(goods_name='新疆库尔勒香梨5斤')
print(goods.goods_name, goods.goods_desc, goods.goods_price)
