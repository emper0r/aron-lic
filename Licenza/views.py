from django.http import HttpResponse
from models import License
import key
import datetime
import bf


def activation(request, req, lic, pwd, server_id):
    try:
        check = License.objects.get(req=req, lic=lic, active_lic=0)
        check_lic = key.validate(req, lic)
        if check_lic is 0:
            check.active_lic = True
            check.server_id = server_id
            check.pwd_client = bf.decrypt(pwd)
            check.save()
            content = '0,' + check.client + \
                      ',' + check.name + \
                      ',' + check.province + \
                      ',' + str(check.exp_date) + \
                      ',' + str(check.qty_dev)
            return HttpResponse(content)
        else:
            content = ['2', ]
            return HttpResponse(content)
    except:
        content = ['1', ]
        return HttpResponse(content)


def check_lic(request, server_id):
    try:
        cl = License.objects.get(server_id=server_id)
        if cl.server_id == server_id:
            today = datetime.datetime.today()
            if cl.exp_date >= datetime.date(today.year, today.month, today.day):
                content = '0'
            else:
                content = '1'
            return HttpResponse(content)
        else:
            content = '1'
            return HttpResponse(content)
    except:
        content = '1'
        return HttpResponse(content)
