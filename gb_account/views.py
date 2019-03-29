from django.shortcuts import render
from gb_merchant.models import MerchantClass
# Create your views here.


# 首页数据
def index(request):
    meishilist = MerchantClass.objects.filter(classid__startswith="01")
    xiuxianlist = MerchantClass.objects.filter(classid__startswith="02")
    shenghuolist = MerchantClass.objects.filter(classid__startswith="03")
    meironglist = MerchantClass.objects.filter(classid__startswith="04")
    hunqinglist = MerchantClass.objects.filter(classid__startswith="05")
    qinzilist = MerchantClass.objects.filter(classid__startswith="06")
    jianshenglist = MerchantClass.objects.filter(classid__startswith="07")
    return render(request, 'index.html', {"meishilist": meishilist, "xiuxianlist": xiuxianlist, "shenghuolist": shenghuolist, "meironglist": meironglist, "hunqinglist": hunqinglist, "qinzilist": qinzilist, "jianshenglist": jianshenglist})
