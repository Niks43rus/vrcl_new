# Generated by Django 3.2.19 on 2024-01-25 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_graph_mg_graph_ms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graph_mg',
            name='Admin_four',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='graph_mg',
            name='Admin_one',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='graph_mg',
            name='Admin_three',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='graph_mg',
            name='Admin_two',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='graph_mg',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='graph_ms',
            name='Admin_four',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='graph_ms',
            name='Admin_one',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='graph_ms',
            name='Admin_three',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='graph_ms',
            name='Admin_two',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='graph_ms',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
