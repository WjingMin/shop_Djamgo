# Generated by Django 3.0.4 on 2020-11-10 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_wxuser_cateid'),
    ]

    operations = [
        migrations.AddField(
            model_name='wxuser',
            name='phone',
            field=models.CharField(max_length=500, null=True, verbose_name='用户手机'),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(default=1, verbose_name='商品状态.1-在售 2-店长推荐 3-限时抢购'),
        ),
        migrations.AlterField(
            model_name='wxuser',
            name='WXpassword',
            field=models.CharField(max_length=300, verbose_name='密码'),
        ),
    ]
