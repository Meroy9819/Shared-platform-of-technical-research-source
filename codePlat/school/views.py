from django.shortcuts import render
from django.shortcuts import render_to_response

def schools(request):
    data = [
        {"id": 1, "name": "中原工学院", "address": "河南省郑州市"},
        {"id": 2, "name": "山西大学", "address": "山西省太原市"},
        {"id": 3, "name": "太原理工大学", "address": "山西省太原市"},
        {"id": 4, "name": "北京邮电大学", "address": "北京市"},
        {"id": 5, "name": "西北农林科技大学", "address": "陕西省"},
        {"id": 6, "name": "长春工业大学", "address": "吉林省长春市"},

    ]
    return render_to_response("title.html", locals())

def school(request,id):
    data={
        "1":{"name": "中原工学院", "address": "河南省郑州市","img":"https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=81966663b651f819f125044ce28f2dd0/ae51f3deb48f8c542c6a25673c292df5e0fe7f39.jpg"},
        "2":{"name": "山西大学", "address": "山西省太原市","img":"https://gss2.bdstatic.com/-fo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=43b9a1201d3853438ccf8027ab28d743/0e2442a7d933c895a7d0ca37dc1373f0830200cb.jpg"},
        "3":{"name": "太原理工大学", "address": "山西省太原市","img":"https://gss0.bdstatic.com/-4o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=26c247796963f6241c5d3e05bf7f8cc5/fd039245d688d43f53495db27f1ed21b0ff43b8a.jpg"},
        "4":{"name": "北京邮电大学", "address": "北京市","img":"https://gss3.bdstatic.com/7Po3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=ff0cc6d833adcbef01347900949449e0/aec379310a55b319c46a7d6941a98226cffc171e.jpg"},
        "5":{"name": "西北农林科技大学", "address": "陕西省","img":"https://gss0.bdstatic.com/94o3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=2ae38e877bf40ad115e4c0e56f1776e2/cdbf6c81800a19d89ca63dba33fa828ba71e46e3.jpg"},
        "6":{"name": "长春工业大学", "address": "吉林省长春市","img":"https://gss3.bdstatic.com/-Po3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=6ab3b6c555fbb2fb342b5f1477714799/c8177f3e6709c93d4392b06f9f3df8dcd00054c1.jpg"},
    }.get(id)
    return render_to_response("detail.html",locals())

