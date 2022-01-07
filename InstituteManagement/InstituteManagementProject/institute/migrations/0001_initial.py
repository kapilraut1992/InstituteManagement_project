# Generated by Django 4.0 on 2022-01-06 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
                ('intake', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
                ('dept', models.ManyToManyField(related_name='department_pro', to='institute.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=50)),
                ('stud_roll', models.IntegerField()),
                ('stud_marks', models.FloatField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='department_stud', to='institute.department')),
            ],
        ),
    ]
