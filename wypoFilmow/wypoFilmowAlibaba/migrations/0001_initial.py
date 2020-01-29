# Generated by Django 2.0.13 on 2020-01-29 22:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Filmy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tytul_PL', models.CharField(max_length=45)),
                ('Tytul_ENG', models.CharField(max_length=45)),
                ('Rok_premiery', models.DateTimeField(verbose_name='data publikacji')),
                ('Czas_trwania', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gatunek', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=45)),
                ('Nazwisko', models.CharField(max_length=45)),
                ('PESEL', models.CharField(max_length=11)),
                ('Ulica', models.CharField(max_length=45)),
                ('Miasto', models.CharField(max_length=45)),
                ('Telefon', models.CharField(max_length=15)),
                ('Tworca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Klient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Platnosci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Zaliczka', models.CharField(max_length=45)),
                ('Doplata', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Pracownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=45)),
                ('Nazwisko', models.CharField(max_length=45)),
                ('PESEL', models.CharField(max_length=11)),
                ('Wiek', models.CharField(max_length=2)),
                ('Tworca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pracownik', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rejestr_wypozyczen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_wypozyczenia', models.DateTimeField(verbose_name='data wypozyczenia')),
                ('Data_zwrotu', models.DateTimeField(verbose_name='data zwrotu')),
                ('filmy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypoFilmowAlibaba.Filmy')),
                ('klient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypoFilmowAlibaba.Klient')),
                ('platnosci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypoFilmowAlibaba.Platnosci')),
                ('pracownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypoFilmowAlibaba.Pracownik')),
            ],
        ),
        migrations.CreateModel(
            name='Rezyser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Imie', models.CharField(max_length=45)),
                ('Nazwisko', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='filmy',
            name='gatunek',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypoFilmowAlibaba.Gatunek'),
        ),
        migrations.AddField(
            model_name='filmy',
            name='rezyser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wypoFilmowAlibaba.Rezyser'),
        ),
    ]