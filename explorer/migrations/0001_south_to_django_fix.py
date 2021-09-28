# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


def migrate_created_by(apps, schema_editor):
    Query = apps.get_model('explorer', 'Query')
    user_model = settings.AUTH_USER_MODEL.split('.')
    User = apps.get_model(user_model[0], user_model[1])
    for query in Query.objects.all():
        email = query.created_by
        user = User.objects.get(email=email)
        query.created_by_user = user
        query.save()
    for query in Query.objects.all():
        if query.created_by != query.created_by_user.email:
            raise RuntimeError('user mismatch detected: %s vs %s' %
                               (query.created_by, query.created_by_user.email))


class Migration(migrations.Migration):

    dependencies = [
        ('explorer', '0001_initial'),
    ]

    operations = [
        # migrate created_by to created_by_user
        migrations.AddField(
            model_name='query',
            name='created_by_user',
            field=models.ForeignKey(blank=True,
                                    to=settings.AUTH_USER_MODEL,
                                    null=True,
                                    on_delete=models.CASCADE),
        ),
        migrations.RunPython(migrate_created_by),
        migrations.RemoveField(
            model_name='query',
            name='created_by',
        ),
        # add querylog
        migrations.CreateModel(
            name='QueryLog',
            fields=[
                ('id',
                 models.AutoField(verbose_name='ID',
                                  serialize=False,
                                  auto_created=True,
                                  primary_key=True)),
                ('sql', models.TextField()),
                ('is_playground', models.BooleanField(default=False)),
                ('run_at', models.DateTimeField(auto_now_add=True)),
                ('query',
                 models.ForeignKey(
                     on_delete=models.deletion.SET_NULL,
                     blank=True,
                     to='explorer.Query',
                     null=True)),
                ('run_by_user',
                 models.ForeignKey(blank=True,
                                   to=settings.AUTH_USER_MODEL,
                                   null=True,
                                   on_delete=models.CASCADE)),
            ],
        ),
    ]
