# Generated by Django 5.0.1 on 2024-01-24 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_ownerprofile_owner_remove_userprofile_barber_and_more'),
        ('contact', '0004_galleryitem_user_alter_appointment_barber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryitem',
            name='user',
        ),
        migrations.AddField(
            model_name='galleryitem',
            name='name',
            field=models.CharField(default='Galerie Element', max_length=255, verbose_name='Element'),
        ),
        migrations.AddField(
            model_name='owner',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='owner_user', to='accounts.ownerprofile', verbose_name='Eigentümer'),
        ),
    ]