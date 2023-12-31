# Generated by Django 4.2.4 on 2023-09-28 09:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('product', models.CharField(max_length=200)),
                ('point', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'award',
            },
        ),
        migrations.CreateModel(
            name='Restraurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('reg_no', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'restraurant',
            },
        ),
        migrations.CreateModel(
            name='Userrestraurant',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_points', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('restraurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restraurant_activities_management.restraurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_restraurant',
            },
        ),
        migrations.CreateModel(
            name='CouponTransaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('point_used', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restraurant_activities_management.award')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'coupon_transaction',
            },
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('end_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('coupon_no', models.CharField(max_length=20)),
                ('point', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('restraurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restraurant_activities_management.restraurant')),
            ],
            options={
                'db_table': 'coupon',
            },
        ),
        migrations.AddField(
            model_name='award',
            name='restraurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restraurant_activities_management.restraurant'),
        ),
    ]
