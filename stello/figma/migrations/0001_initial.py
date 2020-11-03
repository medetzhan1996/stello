# Generated by Django 3.0.8 on 2020-09-21 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
            ],
            options={
                'db_table': 'figma_materials',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('file', models.FileField(upload_to='images')),
                ('file_extra1', models.FileField(blank=True, null=True, upload_to='images')),
                ('file_extra2', models.FileField(blank=True, null=True, upload_to='images')),
                ('file_extra3', models.FileField(blank=True, null=True, upload_to='images')),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('details', tinymce.models.HTMLField(blank=True, null=True)),
                ('shipping_return', tinymce.models.HTMLField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('price_old', models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True)),
                ('is_top', models.BooleanField(default=False)),
                ('kind', models.CharField(choices=[('normal', 'Обычный'), ('text_input', 'Набор текста'), ('image_select', 'Выбор изображения')], default='normal', max_length=12)),
                ('classes', models.CharField(blank=True, max_length=180)),
            ],
            options={
                'db_table': 'figma_products',
            },
        ),
        migrations.CreateModel(
            name='Сategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'figma_categories',
            },
        ),
        migrations.CreateModel(
            name='ProductMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_material', to='figma.Material')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_product', to='figma.Product')),
            ],
            options={
                'db_table': 'figma_products_materials',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_category', to='figma.Сategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='materials',
            field=models.ManyToManyField(blank=True, null=True, related_name='rel_materials', through='figma.ProductMaterial', to='figma.Material'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]