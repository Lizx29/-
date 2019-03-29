# -*-coding: utf-8-*-
from django.db import models
from gb_account.models import Merchants, Users
# Create your models here.


# 门店类型分类
class MerchantClass(models.Model):
    classid = models.CharField(max_length=4, primary_key=True, verbose_name='分类id', help_text="最多4位")
    className = models.CharField(unique=True, max_length=10, verbose_name='分类名', help_text="最多10位")

    def __str__(self):
        return self.className

    class Meta:
        verbose_name = '门店类型分类名'
        verbose_name_plural = '门店类型分类名'


# 门店类型分类项目
class ClassItem(models.Model):
    classid = models.ForeignKey(MerchantClass, verbose_name='分类id', on_delete=models.CASCADE)
    shopid = models.ForeignKey(Merchants, verbose_name='门店id', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.classid) + '-' + str(self.shopid)

    class Meta:
        verbose_name = '门店分类'
        verbose_name_plural = '门店分类'


# 门店图片集
class MerchantImgSet(models.Model):
    def mer_imgset_path(self, filename):
        return "shop/{0}/imgSet/{1}/".format(self.shopid, filename)

    shopid = models.ForeignKey(Merchants, on_delete=models.CASCADE, verbose_name='门店编号')
    imgAddress = models.ImageField(upload_to=mer_imgset_path, verbose_name='图片地址', help_text='图片地址')

    def __str__(self):
        return str(self.shopid) + '图片集'

    class Meta:
        verbose_name = '门店图片集'
        verbose_name_plural = '门店图片集'


# 一级分类 门店服务分类
class ServiceClass(models.Model):
    shopid = models.ForeignKey(Merchants, on_delete=models.CASCADE, verbose_name='门店编号')
    sclassName = models.CharField(max_length=20, verbose_name='服务分类名', help_text='最多20位')
    isDelete = models.BooleanField(default=False, verbose_name='逻辑删除', help_text='逻辑删除')

    def __str__(self):
        return str(self.shopid) + '-' + str(self.sclassName)

    class Meta:
        verbose_name = '门店服务分类名'
        verbose_name_plural = '门店服务分类名'


# 二级分类 服务操作
class Services(models.Model):
    def ser_img_path(self, filename):
        return "shop/{0}/ser_{1}/{2}/".format(self.shopid, self.sName, filename)

    sclassid = models.ForeignKey(ServiceClass, on_delete=models.CASCADE, verbose_name='服务分类编号')
    shopid = models.ForeignKey(Merchants, on_delete=models.CASCADE, verbose_name='门店编号')
    # 基本信息
    sName = models.CharField(max_length=20, verbose_name='服务名', help_text='最大20位')
    sPrice = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='价格', help_text='0.00-99999.99元')
    sImg = models.ImageField(upload_to=ser_img_path, verbose_name='服务图片', help_text='服务图片')
    sDesc = models.TextField(max_length=50, verbose_name='服务描述', help_text='最大50位')
    # 附加信息
    isNeedFile = models.BooleanField(default=False, verbose_name='是否需要上传文件')
    isOnlinePay = models.BooleanField(default=False, verbose_name='是否在线支付')
    isDelete = models.BooleanField(default=False, verbose_name='逻辑删除')

    def __str__(self):
        return str(self.sName) + '-' + str(self.sPrice)

    class Meta:
        verbose_name = '门店服务操作信息'
        verbose_name_plural = '门店服务操作信息'


# 评论
class Comment(models.Model):
    uuid = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='用户id')
    shopid = models.ForeignKey(Merchants, on_delete=models.CASCADE, verbose_name='门店id')
    content = models.TextField(max_length=150, verbose_name='评论内容', help_text='最多150位')

    def __str__(self):
        return str(self.uuid) + '-' + str(self.shopid) + '评论'

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = '评论'


# 广告
class Commercial(models.Model):
    cImg = models.ImageField(upload_to='commercial/', verbose_name='广告图片', help_text='广告图片')
    trackid = models.ForeignKey(Merchants, on_delete=models.CASCADE, verbose_name='门店id')

    def __str__(self):
        return str(self.trackid) + '广告'

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = '广告'
