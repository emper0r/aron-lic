from django.contrib import admin
from django.conf import settings
from Licenza.models import License
from django.contrib import messages
from django.core import mail
import time
import os
import threading
import datetime


def send_reminder(client, giorni, email_client):
    ctx = 'La licenza per il cliente: %s sta per scadere, mancano %s giorni' % (client, giorni)
    mail.send_mail('Avviso scadenza Licenza Aron Manager.',
                   ctx,
                   settings.DEFAULT_FROM_EMAIL,
                   ['ctime@ctime.it', email_client],
                   fail_silently=True)


def check_license_client():
    threading.Timer(86400.0, check_license_client).start()
    license_client = License.objects.filter(exp_date__gt=datetime.date.today(), active_lic=1)
    for client in range(0, license_client.count()):
        check_days = license_client.values()[client]['exp_date'] - datetime.date.today()
        if check_days.days is 30 or check_days is 15 or check_days is 3:
            send_reminder(license_client.values()[client]['client'],
                          check_days.days,
                          license_client.values()[client]['email'])

check_license_client()


class LicAdmin(admin.ModelAdmin):
    list_display = ('client', 'name', 'email', 'province', 'masq_qty_dev', 'active_date', 'scadenza', 'active_lic', 'pwd_client')
    readonly_fields = ('req', 'lic', 'active_date', 'active_lic', 'pwd_client')
    search_fields = ('client',)
    exclude = ('server_id','pwd_client')

    def save_model(self, request, obj, form, change):
        obj.pwd_client = 'Pending...'
        super(LicAdmin, self).save_model(request, obj, form, change)
        messages.set_level(request, messages.SUCCESS)
        time.sleep(3)
        os.system('sudo service apache2 reload')
        self.send_email(obj.req, obj.lic, obj.email, obj.name, obj.client, obj.province, obj.qty_dev)

    def send_email(self, req, lic, email, name, client, province, qty_dev):
        destination = [email, 'paolo@ctime.it', 'antonio@ctime.it']
        if qty_dev is 0:
            qty_dev = 'Illimitato'
        else:
            qty_dev
        ctx = 'Gentile Cliente,\n\nGrazie per aver scelto il nostro prodotto Aron Proxy, ' \
              'nel seguito inviamo i dati per l\'attivazione della licenza.\n\n' \
              'Cliente: ' + client + '\nNome: ' + name + '\nProvincia: ' + province + \
              '\nCodice: ' + req + '\nLicenza: ' + lic + '\nNumero massimo di dispositivi gestibili: ' + str(qty_dev) + \
              '\n\nComputer Time s.r.l\nVia A. Negri 6, Somma Lombardo, VA\nTelefono: +39 0331-985432\nFax: +39 0331-995627\n'
        mail.send_mail('Licenze per attivazione Aron Manager.',
                       ctx,
                       settings.DEFAULT_FROM_EMAIL,
                       destination,
                       fail_silently=True)

admin.site.register(License, LicAdmin)
