from django.http import HttpResponse
from django.template import RequestContext, loader

def login(request):
    login_template = loader.get_template('dashboard/index.html')
    ctx = RequestContext(request, {
        'login': login_template,
    })
    return HttpResponse(login_template.render(ctx))
