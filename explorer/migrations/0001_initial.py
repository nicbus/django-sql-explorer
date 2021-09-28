from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('sql', models.TextField(blank=True)),
				('description', models.TextField(verbose_name='Description', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_run_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.CharField(max_length=255)),
                ('agg_filters', models.TextField(blank=True, null=True)),
                ('aggregations', models.TextField(blank=True, null=True)),
                ('columns', models.TextField(blank=True, null=True)),
                ('filters', models.TextField(blank=True, null=True)),
                ('include_code', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('not_agg_selection_value', models.TextField(blank=True, null=True)),
                ('not_sel_aggregations', models.TextField(blank=True, null=True)),
                ('obs_values', models.TextField(blank=True, null=True)),
                ('open_data', models.BooleanField(default=False)),
				('query_editor', models.BooleanField(default=False)),
				('range', models.BooleanField(default=False)),
				('rows', models.TextField(blank=True, null=True)),
				('table', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
