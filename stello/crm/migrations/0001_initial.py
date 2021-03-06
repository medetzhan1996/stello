# Generated by Django 3.0.8 on 2020-09-21 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyLeadStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Integration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('type', models.CharField(choices=[('instagramV2', 'Instagram direct'), ('instagramVOff', 'комментарии Instagram'), ('whatsapp', 'Whatsapp'), ('whatsapp2', 'Whatsapp Enterprise')], max_length=80)),
                ('login', models.CharField(max_length=180)),
                ('avatar', models.URLField(blank=True, max_length=220, null=True)),
                ('externalId', models.CharField(max_length=180, null=True)),
                ('api_id', models.IntegerField(blank=True, null=True)),
                ('api_token', models.CharField(max_length=180, null=True)),
                ('status', models.CharField(choices=[('active', 'Активный'), ('blocked', 'Блокированный')], default='active', max_length=12)),
            ],
            options={
                'db_table': 'integrations',
            },
        ),
        migrations.CreateModel(
            name='Сompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
            ],
            options={
                'db_table': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Сustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=180)),
                ('login', models.CharField(max_length=180)),
                ('type', models.CharField(choices=[('instagramV2', 'Instagram direct'), ('instagramVOff', 'комментарии Instagram'), ('whatsapp', 'Whatsapp'), ('whatsapp2', 'Whatsapp Enterprise')], max_length=80, null=True)),
                ('avatar', models.URLField(max_length=220, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=18)),
                ('backup_phone_number', models.CharField(blank=True, max_length=18)),
                ('customer_id', models.IntegerField(null=True)),
                ('social_id', models.CharField(blank=True, max_length=180)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers_company', to='crm.Сompany')),
            ],
            options={
                'db_table': 'customers',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('type', models.IntegerField(choices=[(1, 'Управляющий компанией'), (2, 'Главный менеджер'), (3, 'Менеджер'), (4, 'Бухгалтер'), (5, 'Курьер')], default=1, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=18)),
                ('address', models.CharField(blank=True, max_length=280)),
                ('is_blocked', models.BooleanField(default=False)),
                ('last_lead', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles_company', to='crm.Сompany')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, max_digits=19)),
                ('product', models.CharField(max_length=180)),
                ('count', models.IntegerField(default=1)),
                ('deadline_date', models.DateField(null=True)),
                ('payment', models.IntegerField(choices=[(1, 'Полная оплата'), (2, 'Предварительная оплата'), (3, 'Оплата при доставке')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_company', to='crm.Сompany')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_customers', to='crm.Сustomer')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='LeadStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('companies', models.ManyToManyField(through='crm.CompanyLeadStatus', to='crm.Сompany')),
            ],
            options={
                'db_table': 'lead_status',
            },
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_id', models.IntegerField(null=True)),
                ('read', models.BooleanField(default=False)),
                ('message_unread', models.IntegerField(default=1)),
                ('real_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads_company', to='crm.Сompany')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads_customer', to='crm.Сustomer')),
                ('integration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leads_integration', to='crm.Integration')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leads_status', to='crm.LeadStatus')),
            ],
            options={
                'db_table': 'leads',
            },
        ),
        migrations.AddField(
            model_name='integration',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='integration_companies', to='crm.Сompany'),
        ),
        migrations.AddField(
            model_name='integration',
            name='customers',
            field=models.ManyToManyField(blank=True, null=True, related_name='integrations_customers', to='crm.Сustomer'),
        ),
        migrations.AddField(
            model_name='integration',
            name='managers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companyleadstatus',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_rel', to='crm.Сompany'),
        ),
        migrations.AddField(
            model_name='companyleadstatus',
            name='lead_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lead_status_rel', to='crm.LeadStatus'),
        ),
    ]
