# Generated by Django 3.2 on 2021-04-27 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0002_onlineshopuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_shop.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_shop.onlineshopuser')),
            ],
        ),
    ]
