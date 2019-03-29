from django.contrib import admin
from .models import Orders, AOrders, BOrders
from django.utils.html import format_html
# Register your models here.


# A类订单注册
@admin.register(AOrders)
class AOrderAdmin(admin.ModelAdmin):
    def colored_status(self):
        info = '订单初始中'
        color_code = 'white'
        if self.oStatus == 'yxd':
            info = '用户已下单'
            color_code = 'blue'
        elif self.oStatus == 'yzf':
            info = '用户已支付'
            color_code = 'green'
        elif self.oStatus == 'yjd':
            info = '商家已接单'
            color_code = 'yellow'
        elif self.oStatus == 'yjs':
            info = '订单已结束'
            color_code = 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            info,
        )
    colored_status.short_description = "订单状态"

    list_display = ["orderid", "uuid", "shopid", "spid", "oPrice", colored_status, "createTime", "isDelete"]
    list_filter = ["oStatus", "isDelete"]
    search_fields = ["orderid", "uuid", "shopid"]

    fieldsets = [
        ("", {"fields": ["orderid", "uuid", "shopid", "spid"]}),
        ("基本信息", {"fields": ["oPhone", "oPrice", "oTime", "oDesc", "qrCode", "isDelete"]}),
        ("验证号", {"fields": ["oStatus"]})
    ]

    readonly_fields = ["orderid", "uuid", "shopid", "spid"]
    list_per_page = 20
    empty_value_display = '-empty-'


# B类订单注册
@admin.register(BOrders)
class BOrderAdmin(admin.ModelAdmin):
    def colored_status(self):
        info = '订单初始中'
        color_code = 'white'
        if self.oStatus == 'yxd':
            info = '用户已下单'
            color_code = 'blue'
        elif self.oStatus == 'yzf':
            info = '用户已支付'
            color_code = 'green'
        elif self.oStatus == 'yjd':
            info = '商家已接单'
            color_code = 'yellow'
        elif self.oStatus == 'yjs':
            info = '订单已结束'
            color_code = 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            info,
        )
    colored_status.short_description = "订单状态"

    list_display = ["orderid", "uuid", "shopid", "spid", "oPrice", colored_status, "createTime", "isDelete"]
    list_filter = ["oStatus", "isDelete"]
    search_fields = ["orderid", "uuid", "shopid"]

    fieldsets = [
        ("", {"fields": ["orderid", "uuid", "shopid", "spid"]}),
        ("基本信息", {"fields": ["oPhone", "oPrice", "oTime", "upFile", "oDesc", "qrCode", "isDelete"]}),
        ("验证号", {"fields": ["oStatus"]})
    ]

    readonly_fields = ["orderid", "uuid", "shopid", "spid"]
    list_per_page = 20
    empty_value_display = '-empty-'
