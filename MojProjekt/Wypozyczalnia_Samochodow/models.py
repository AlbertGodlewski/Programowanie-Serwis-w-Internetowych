from django.db import models

# Create your models here.

class klienci(models.Model):
     idklienta = models.AutoField(primary_key=True)
     imie = models.CharField(max_length=45)
     nazwisko = models.CharField(max_length=45)
     nr_telefonu = models.CharField(max_length=12)
     miasto = models.CharField(max_length=45)
     ulica = models.CharField(max_length=45)
     numer_mieszkania = models.CharField(max_length=45)
     kod_pocztowy = models.CharField(max_length=45)

class marka_i_model(models.Model):
    nr_marka_model = models.AutoField(primary_key=True)
    marka = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    data_prod = models.DateField('data produkcji')

class samochody(models.Model):
    idsamochodu = models.AutoField(primary_key=True)
    marka = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    data_prod = models.DateField('data produkcji')
    kolor = models.CharField(max_length=45)
    nr_marka_model = models.ForeignKey(marka_i_model, on_delete=models.CASCADE)

class pracownicy(models.Model):
    idpracownika = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=45)
    nazwisko = models.CharField(max_length=45)
    data_zat = models.DateTimeField('data zatrudnienia')
    stanowisko = models.CharField(max_length=45)
    nr_telefonu = models.CharField(max_length=12)


class zamowienia(models.Model):
    idzamowienia = models.AutoField(primary_key=True)
    idklienta = models.ForeignKey(klienci, on_delete=models.CASCADE)
    idsamochodu = models.ForeignKey(samochody, on_delete=models.CASCADE)
    idpracownika = models.ForeignKey(pracownicy, on_delete=models.CASCADE)
    data_wyp = models.DateTimeField('data wypozyczenia')
    data_oddania = models.DateTimeField('data_oddania')
    kaucja = models.FloatField()
    cena_zam = models.FloatField()

