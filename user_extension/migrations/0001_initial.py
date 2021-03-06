# Generated by Django 4.0.4 on 2022-05-26 21:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.PositiveBigIntegerField()),
                ('user_type', models.CharField(choices=[('Dealer', 'Dealer'), ('Personal', 'Personal'), ('Organization', 'Organization')], max_length=20)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='vehicle.location')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
