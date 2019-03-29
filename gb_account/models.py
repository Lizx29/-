# -*-coding: utf-8-*-
from django.db import models
import uuid
import django.utils.timezone as timezone
# Create your models here.


# 用户信息
class Users(models.Model):
    def user_img_path(self, filename):
        return 'user/{0}/{1}/'.format(self.userName, filename)

    GENDER_CHOICES = (
        ('男', '男'),
        ('女', '女'),
    )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='用户号', help_text='uuid')
    userName = models.CharField(max_length=20, unique=True, verbose_name='用户名', help_text='6-20位且唯一不可变')
    userPhone = models.DecimalField(unique=True, max_digits=11, decimal_places=0, verbose_name='手机号', help_text='11位且唯一')
    userPassWd = models.CharField(max_length=32, verbose_name='用户密码', help_text='6-20位及md5加密')
    # 基本信息
    trueName = models.CharField(max_length=15, verbose_name='姓名', help_text='最多15位')
    userGender = models.CharField(max_length=1, default='男', verbose_name='性别', choices=GENDER_CHOICES)
    userImg = models.ImageField(upload_to=user_img_path, verbose_name='用户头像', help_text='用户头像')
    # 时间
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建账户时间')
    lastLoginTime = models.DateTimeField(default=timezone.now, verbose_name='最后登录时间')
    # 验证号
    userToken = models.CharField(default='初始化', max_length=32, verbose_name='用户验证号', help_text='登录验证号及md5加密')

    def __str__(self):
        return self.userName

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'


# 门店信息
class Merchants(models.Model):
    def mer_img_path(self, filename):
        return 'shop/{0}/headImg/{1}/'.format(self.shopid, filename)

    def mer_license_path(self, filename):
        return 'shop/{0}/license/{1}/'.format(self.shopid, filename)

    STATUS_CHOICES = (
        ('200', '状态正常'),
        ('404', '审核中'),
        ('202', '信息已修改'),
    )

    shopid = models.CharField(max_length=26, primary_key=True, verbose_name='门店编号', help_text='26位及邮编加时间戳')
    shopAPhone = models.DecimalField(unique=True, max_digits=11, decimal_places=0, verbose_name='手机号', help_text='11位且唯一')
    shopPassWd = models.CharField(max_length=32, verbose_name='门店密码', help_text='6-20位及md5加密')
    # 基本信息
    shopName = models.CharField(max_length=30, verbose_name='门店名称', help_text='最多30位')
    shopAddress = models.CharField(max_length=50, verbose_name='门店地址', help_text='最多50位')
    shopCoordinate = models.CharField(max_length=20, verbose_name='门店坐标', help_text='百度地图api坐标')
    shopCPhone = models.CharField(max_length=35, verbose_name='门店联系电话', help_text='可填多个且最多35位')
    shopHours = models.CharField(max_length=50, verbose_name='门店营业时间', help_text='最多50位')
    # 头像及执照
    shopImg = models.ImageField(upload_to=mer_img_path, verbose_name='门店头像', help_text='门店头像')
    shopLicense = models.ImageField(upload_to=mer_license_path, verbose_name='门店执照', help_text='门店执照')
    # 时间
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='创建账户时间')
    lastLoginTime = models.DateTimeField(default=timezone.now, verbose_name='最后登录时间')
    # 门店状态
    shopStatus = models.CharField(default='404', max_length=3, verbose_name='门店状态', help_text='200正常 404审核中 202信息已修改', choices=STATUS_CHOICES)
    # 门店验证号
    shopToken = models.CharField(default='初始化', max_length=32, verbose_name='门店验证号', help_text='门店验证号及md5加密')

    def __str__(self):
        return self.shopid

    class Meta:
        verbose_name = '门店'
        verbose_name_plural = '门店'
