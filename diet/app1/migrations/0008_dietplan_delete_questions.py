# Generated by Django 4.1.7 on 2023-05-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Snack', 'Snack'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner')], max_length=50)),
                ('food', models.CharField(max_length=200)),
                ('portion_size', models.CharField(max_length=50)),
                ('calories', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('carbs', models.IntegerField()),
                ('fat', models.IntegerField()),
                ('desired_weight', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
