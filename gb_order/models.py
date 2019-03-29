# -*-coding: utf-8-*-
from django.db import models
from gb_account.models import Merchants, Users
from gb_merchant.models import Services
# Create your models here.


# 订单基类
class Orders(models.Model):
    def order_qrcode_path(self, filename):
        return "order/{0}/qrcode/{1}/".format(self.orderid, filename)

    STATUS_CHOICES = (
        ('yxd', '用户已下单'),
        ('yzf', '用户已支付'),
        ('yjd', '商家已接单'),
        ('yjs', '订单已结束'),
    )

    orderid = models.CharField(max_length=32, primary_key=True, verbose_name='订单号', help_text='md5加密')
    uuid = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='消费用户号')
    shopid = models.ForeignKey(Merchants, on_delete=models.CASCADE, verbose_name='消费门店号')
    spid = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='服务号')
    # 基本信息
    oPhone = models.DecimalField(max_digits=11, decimal_places=0, verbose_name='联系电话', help_text='11位')
    oPrice = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='价格', help_text='0.00-99999.99元')
    oTime = models.DateTimeField(verbose_name='预约时间')
    oDesc = models.TextField(max_length=50, verbose_name='订单备注', help_text='最大50位')
    qrCode = models.ImageField(upload_to=order_qrcode_path, verbose_name='二维码')
    isDelete = models.BooleanField(default=False, verbose_name='逻辑删除')
    createTime = models.DateTimeField(auto_now_add=True, verbose_name='订单创建时间')
    # 订单状态
    oStatus = models.CharField(max_length=3, verbose_name='订单状态', help_text='yxd-用户已下单 yzf-用户已支付 yjd-商家已接单 yjs-订单已结束', choices=STATUS_CHOICES)

    class Meta:
        abstract = True


# 订单B类
class AOrders(Orders):
    def __str__(self):
        return self.orderid

    class Meta:
        verbose_name = 'A类订单'
        verbose_name_plural = 'A类订单'


# 订单B类
class BOrders(Orders):
    def order_file_path(self, filename):
        return "order/{0}/file/{1}/".format(self.orderid, filename)

    upFile = models.FileField(upload_to=order_file_path, verbose_name='上传文件', help_text='上传文件')

    def __str__(self):
        return self.orderid

    class Meta:
        verbose_name = 'B类订单'
        verbose_name_plural = 'B类订单'

