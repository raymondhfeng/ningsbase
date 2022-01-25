# Generated by Django 4.0.1 on 2022-01-25 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('size', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('ipo_status', models.CharField(max_length=256)),
                ('funding_round', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='InvestingEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('investing_type', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Funding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funding_date', models.DateTimeField()),
                ('amount', models.IntegerField()),
                ('stage', models.CharField(max_length=128)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ningsbase.company')),
                ('investing_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ningsbase.investingentity')),
            ],
        ),
        migrations.CreateModel(
            name='Acquisition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('acquiree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_acquiree', to='ningsbase.company')),
                ('acquirer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_acquirer', to='ningsbase.company')),
            ],
        ),
    ]