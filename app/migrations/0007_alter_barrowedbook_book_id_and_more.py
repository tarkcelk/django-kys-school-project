# Generated by Django 4.2 on 2023-04-20 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_barrowedbook_book_id_barrowedbook_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrowedbook',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.book'),
        ),
        migrations.AlterField(
            model_name='barrowedbook',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='barrowedbook',
            name='member_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.member'),
        ),
    ]