# Generated by Django 5.0.4 on 2024-04-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("market", "0004_alter_book_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="images/", verbose_name="Image"
            ),
        ),
    ]
