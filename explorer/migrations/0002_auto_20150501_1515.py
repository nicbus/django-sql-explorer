from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0001_south_to_django_fix'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='querylog',
            name='is_playground',
        ),
        migrations.AlterField(
            model_name='querylog',
            name='sql',
            field=models.TextField(blank=True),
        ),
    ]
