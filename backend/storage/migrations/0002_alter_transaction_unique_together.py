# Generated by Django 5.0.6 on 2024-06-22 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='transaction',
            unique_together={('posting_date', 'description', 'amount', 'transaction_type')},
        ),
    ]