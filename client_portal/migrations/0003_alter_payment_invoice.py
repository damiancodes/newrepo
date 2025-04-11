# Generated by Django 4.2 on 2025-04-10 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client_portal', '0002_client_message_payment_projectfile_projecttask_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='client_portal.invoice'),
        ),
    ]
