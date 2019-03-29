# -*-coding: utf-8-*-
from django.contrib import admin
from .models import Users, Merchants
from gb_merchant.models import MerchantImgSet, ClassItem
from django.utils.html import format_html
# Register your models here.
# gbadmin gbadmin123456

# 页面
admin.site.site_header = "gobooking后台管理系统"
admin.site.site_title = "gobooking后台"
admin.site.index_title = "欢迎登录"


# 用户信息注册
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    def img_show(self, obj):
        return format_html(
            '<img src="/{}" width="50px"/>',
            obj.userImg.url,
        )
    img_show.short_description = '用户头像'
    img_show.allow_tags = True

    list_display_links = ["uuid", "userName", "userPhone"]
    list_display = ["uuid", "userName", "userPhone", "trueName", "userGender", "img_show", "lastLoginTime", "createTime"]
    list_filter = ["userGender", "createTime", "lastLoginTime"]
    search_fields = ["userName", "userPhone"]

    fieldsets = [
        ("", {"fields": ["uuid", "userName", "userPhone", "userPassWd"]}),
        ("基本信息", {"fields": ["trueName", "userGender", 'userImg', "lastLoginTime"]}),
        ("验证号", {"fields": ["userToken"]})
    ]

    readonly_fields = ["uuid", "lastLoginTime", "userToken"]
    list_per_page = 20
    empty_value_display = '-empty-'


# 门店图片集
class MerImgSet(admin.TabularInline):
    model = MerchantImgSet
    extra = 2


# 门店分类
class MerClass(admin.TabularInline):
    model = ClassItem
    extra = 1


# 门店信息注册
@admin.register(Merchants)
class MerchantsAdmin(admin.ModelAdmin):
    def colored_status(self):
        info = '初始中'
        color_code = 'white'
        if self.shopStatus == '202':
            info = '正常'
            color_code = 'green'
        elif self.shopStatus == '404':
            info = '审核中'
            color_code = 'red'
        elif self.shopStatus == '202':
            info = '信息修改'
            color_code = 'yellow'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            info,
        )
    colored_status.short_description = '门店状态'
    # 门店信息中可以添加对应的图片集、门店类型
    inlines = [MerImgSet, MerClass]

    list_display_links = ["shopid", "shopAPhone"]
    list_display = ["shopid", "shopAPhone", "shopName", colored_status, "shopToken", "lastLoginTime", "createTime"]
    list_filter = ["shopStatus", "createTime", "lastLoginTime"]
    search_fields = ["shopid", "shopAPhone", "shopName"]

    fieldsets = [
        ("", {"fields": ["shopid", "shopAPhone", "shopPassWd"]}),
        ("基本信息", {"fields": ["shopName", "shopAddress", "shopCoordinate", "shopCPhone", "shopHours", "lastLoginTime"]}),
        ("头像及执照", {"fields": ["shopImg", "shopLicense"]}),
        ("门店状态", {"fields": ["shopStatus"]}),
        ("验证号", {"fields": ["shopToken"]})
    ]

    readonly_fields = ["shopToken", "lastLoginTime"]
    list_per_page = 20
    empty_value_display = '-empty-'

