from django.contrib import admin

# Register your models here.
from goods.models import GoodsInfo, GoodsCategory

class GoodsInfoAdmin(admin.ModelAdmin):
    # 后台需要显示的字段
    list_display = ['id', 'goods_name', 'goods_price', 'goods_desc']
    # 后台需要显示的数量
    list_per_page = 20
    # 添加搜索框
    search_fields = ['id', 'goods_name', 'goods_price']

admin.site.register(GoodsInfo, GoodsInfoAdmin)


admin.site.register(GoodsCategory)
