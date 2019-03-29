# -*-coding: utf-8-*-
from django.contrib import admin
from .models import MerchantClass, ClassItem, MerchantImgSet, ServiceClass, Services, Comment, Commercial
# Register your models here.


# 门店类型分类注册
@admin.register(MerchantClass)
class MerClassAdmin(admin.ModelAdmin):
    list_display_links = ["classid", "className"]
    list_display = ["classid", "className"]
    search_fields = ["classid", "className"]

    fields = ["classid", "className"]

    list_per_page = 20
    empty_value_display = '-empty-'


# 分类门店列表注册
@admin.register(ClassItem)
class ClassItemAdmin(admin.ModelAdmin):
    list_display_links = ["pk", "classid"]
    list_display = ["pk", "classid", "shopid"]
    search_fields = ["classid", "shopid"]

    fields = ["classid", "shopid"]

    list_per_page = 20
    empty_value_display = '-empty-'


# 门店图片集注册
@admin.register(MerchantImgSet)
class MerImgSetAdmin(admin.ModelAdmin):
    list_display_links = ["pk", "shopid"]
    list_display = ["pk", "shopid", "imgAddress"]
    search_fields = ["shopid"]

    fields = ["shopid", "imgAddress"]

    list_per_page = 20
    empty_value_display = '-empty-'


# 服务操作
class Service(admin.TabularInline):
    model = Services
    extra = 1


# 门店服务分类注册
@admin.register(ServiceClass)
class SerClassAdmin(admin.ModelAdmin):
    # 服务分类中可以添加对应的服务操作
    inlines = [Service]
    list_display_links = ["pk", "shopid"]
    list_display = ["pk", "shopid", "sclassName", "isDelete"]
    list_filter = ["isDelete"]
    search_fields = ["shopid", "sclassName"]

    fields = ["shopid", "sclassName", "isDelete"]

    list_per_page = 20
    empty_value_display = '-empty-'


# 门店服务操作注册
@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display_links = ["pk"]
    list_display = ["pk", "sclassid", "shopid", "sName", "sPrice", "isNeedFile", "isOnlinePay", "isDelete"]
    list_filter = ["isNeedFile", "isOnlinePay", "isDelete"]
    search_fields = ["sName", "sclassid", "shopid"]

    fieldsets = [
        ("", {"fields": ["sclassid", "shopid"]}),
        ("基本信息", {"fields": ["sName", "sPrice", "sImg", "sDesc"]}),
        ("附加信息", {"fields": ["isNeedFile", "isOnlinePay", "isDelete"]}),
    ]

    list_per_page = 20
    empty_value_display = '-empty-'


# 评论注册
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display_links = ["pk"]
    list_display = ["pk", "uuid", "shopid", "content"]
    search_fields = ["uuid", "shopid", "content"]

    fields = ["uuid", "shopid", "content"]

    list_per_page = 20
    empty_value_display = '-empty-'


# 广告注册
@admin.register(Commercial)
class CommercialAdmin(admin.ModelAdmin):
    list_display_links = ["pk"]
    list_display = ["pk", "cImg", "trackid"]
    search_fields = ["trackid"]

    fields = ["cImg", "trackid"]

    list_per_page = 20
    empty_value_display = '-empty-'
