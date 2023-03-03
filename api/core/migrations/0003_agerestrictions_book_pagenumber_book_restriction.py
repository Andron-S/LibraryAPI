# Generated by Django 4.1.7 on 2023-03-03 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_book_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeRestrictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restriction', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='pageNumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='restriction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.agerestrictions'),
        ),
    ]