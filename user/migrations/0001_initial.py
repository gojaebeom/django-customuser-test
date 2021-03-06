# Generated by Django 3.1.4 on 2020-12-09 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화 여부')),
                ('is_staff', models.BooleanField(default=False, verbose_name='관리자 여부')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
