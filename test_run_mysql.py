from goods.models import *

categories = [('时令水果', 'fruit', 1),
              ('海鲜水产', 'seafood', 2),
              ('全品肉类', 'meet', 3),
              ('美味蛋品', 'egg', 4),
              ('新鲜蔬菜', 'vegetables', 5),
              ('低温奶制品', 'ice', 6)]

for cag in categories:
    c = GoodsCategory()
    c.cag_name = cag[0]
    c.cag_css = cag[1]
    c.cag_img = 'images/banner0%d.jpg'%cag[2]
    c.save()

