from django.db import models
from django.utils.html import format_html
import datetime
import key

pk, sk = key.generate_keypair()


class License(models.Model):
    PROVINCE = (('Agrigento', 'Agrigento'),
                ('Alessandria', 'Alessandria'),
                ('Ancona', 'Ancona'),
                ('Aosta', 'Aosta'),
                ('Arezzo', 'Arezzo'),
                ('Ascoli Piceno', 'Ascoli Piceno'),
                ('Asti', 'Asti'),
                ('Avellino', 'Avellino'),
                ('Bari', 'Bari'),
                ('Barletta-Andria-Trani', 'Barletta-Andria-Trani'),
                ('Belluno', 'Belluno'),
                ('Benevento', 'Benevento'),
                ('Bergamo', 'Bergamo'),
                ('Biella', 'Biella'),
                ('Bologna', 'Bologna'),
                ('Bolzano', 'Bolzano'),
                ('Brescia', 'Brescia'),
                ('Brindisi', 'Brindisi'),
                ('Cagliari', 'Cagliari'),
                ('Caltanissetta', 'Caltanissetta'),
                ('Campobasso', 'Campobasso'),
                ('Carbonia-Iglesias', 'Carbonia-Iglesias'),
                ('Caserta', 'Caserta'),
                ('Catania', 'Catania'),
                ('Catanzaro', 'Catanzaro'),
                ('Chieti', 'Chieti'),
                ('Como', 'Como'),
                ('Cosenza', 'Cosenza'),
                ('Cremona', 'Cremona'),
                ('Crotone', 'Crotone'),
                ('Cuneo', 'Cuneo'),
                ('Enna', 'Enna'),
                ('FermoM', 'Fermo'),
                ('Ferrara', 'Ferrara'),
                ('Firenze', 'Firenze'),
                ('Foggia', 'Foggia'),
                ('Forli-Cesena', 'Forli-Cesena'),
                ('Frosinone', 'Frosinone'),
                ('Genova', 'Genova'),
                ('Gorizia', 'Gorizia'),
                ('Grosseto', 'Grosseto'),
                ('Imperia', 'Imperia'),
                ('Isernia', 'Isernia'),
                ('La Spezia', 'La Spezia'),
                ('L\'Aquila', 'L\'Aquila'),
                ('Latina', 'Latina'),
                ('Lecce', 'Lecce'),
                ('Lecco', 'Lecco'),
                ('Livorno', 'Livorno'),
                ('Lodi', 'Lodi'),
                ('Lucca', 'Lucca'),
                ('Macerata', 'Macerata'),
                ('Mantova', 'Mantova'),
                ('Massa-Carrara', 'Massa-Carrara'),
                ('Matera', 'Matera'),
                ('Medio Campidano', 'Medio Campidano'),
                ('Messina', 'Messina'),
                ('Milano', 'Milano'),
                ('Modena', 'Modena'),
                ('Monza e della Brianza', 'Monza e della Brianza'),
                ('Napoli', 'Napoli'),
                ('Novara', 'Novara'),
                ('Nuoro', 'Nuoro'),
                ('Olbia-Tempio', 'Olbia-Tempio'),
                ('Oristano', 'Oristano'),
                ('Padova', 'Padova'),
                ('Palermo', 'Palermo'),
                ('Parma', 'Parma'),
                ('Pavia', 'Pavia'),
                ('Perugia', 'Perugia'),
                ('Pesaro e Urbino', 'Pesaro e Urbino'),
                ('Pescara', 'Pescara'),
                ('Piacenza', 'Piacenza'),
                ('PPisaI', 'Pisa'),
                ('Pistoia', 'Pistoia'),
                ('Pordenone', 'Pordenone'),
                ('Potenza', 'Potenza'),
                ('Prato', 'Prato'),
                ('Ragusa', 'Ragusa'),
                ('Ravenna', 'Ravenna'),
                ('Reggio Calabria', 'Reggio Calabria'),
                ('Reggio Emilia', 'Reggio Emilia'),
                ('Rieti', 'Rieti'),
                ('Rimini', 'Rimini'),
                ('Roma', 'Roma'),
                ('Rovigo', 'Rovigo'),
                ('Salerno', 'Salerno'),
                ('Sassari', 'Sassari'),
                ('Savona', 'Savona'),
                ('Siena', 'Siena'),
                ('Siracusa', 'Siracusa'),
                ('Sondrio', 'Sondrio'),
                ('Taranto', 'Taranto'),
                ('Teramo', 'Teramo'),
                ('Terni', 'Terni'),
                ('Torino', 'Torino'),
                ('Ogliastra', 'Ogliastra'),
                ('Trapani', 'Trapani'),
                ('Trento', 'Trento'),
                ('Treviso', 'Treviso'),
                ('Trieste', 'Trieste'),
                ('Udine', 'Udine'),
                ('Varese', 'Varese'),
                ('Venezia', 'Venezia'),
                ('Verbano-Cusio-Ossola', 'Verbano-Cusio-Ossola'),
                ('Vercelli', 'Vercelli'),
                ('Verona', 'Verona'),
                ('Vibo Valentina', 'Vibo Valentina'),
                ('Vicenza', 'Vicenza'),
                ('Viterbo', 'Viterbo'))
    client = models.CharField('Cliente',
                              max_length=64,
                              null=False,
                              blank=False)
    province = models.CharField('Provincia', max_length=16, choices=PROVINCE, help_text="Seleziona la provincia")
    name = models.CharField('Nominativo',
                            max_length=32,
                            null=False)
    email = models.EmailField('Email',
                              help_text='Posta del cliente per consegna delle licenze')
    active_date = models.DateField('Data creazione', auto_now_add=True)
    exp_date = models.DateField('Data scadenza', auto_now_add=False)
    active_lic = models.BooleanField('Licenza attiva', default=False)
    pwd_client = models.CharField('Password Client', max_length=32, null=True, blank=True, help_text="Password admin per collegarsi da remoto")
    pk_a = key.key_to_string(pk)
    sk_b = key.secret_to_string(sk)
    req = models.CharField('Codice',
                           max_length=64,
                           default=unicode(pk_a),
                           help_text='Codice di richiesta che sara\' inviata al cliente')
    lic = models.CharField('Licenza',
                           default=unicode(sk_b),
                           max_length=64,
                           help_text='Licenza che sara\' inviata al cliente')
    server_id = models.CharField('ID Hardware', max_length=32, null=True)
    qty_dev = models.IntegerField('Devices', max_length=100, blank=False, help_text='Numero di dispositivi massimo gestibili.')

    class Meta:
        verbose_name_plural = 'Licenze clienti'

    def __str__(self):
        return unicode(self.client)

    def scadenza(self):
        license_client = License.objects.filter(exp_date__gt=datetime.date.today(), client=self.client, active_lic=1)
        try:
            check_days = license_client.values()[0]['exp_date'] - datetime.date.today()
            if check_days.days < 30 and license_client.values()[0]['active_lic'] == 1:
                return format_html('<span style="color: #FF0000;">%s ( %s gg )</span>'
                                   % (self.exp_date, check_days.days))
            else:
                return "%s" % self.exp_date
        except:
            return "%s" % self.exp_date

    def masq_qty_dev(self):
        if int(self.qty_dev) is 0:
            self.qty_dev = 'Illimitato'
        else:
            self.qty_dev
        return self.qty_dev

    masq_qty_dev.short_description = 'Dispositivi'

    scadenza.short_decription = 'Scandenza'
    scadenza.allow_tags = True
