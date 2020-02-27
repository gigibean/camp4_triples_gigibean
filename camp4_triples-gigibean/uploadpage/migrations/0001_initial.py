# Generated by Django 3.0.2 on 2020-02-27 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.CharField(max_length=225)),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
            ],
            options={
                'db_table': 'comments',
                'ordering': ['-created_dt'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
            ],
            options={
                'db_table': 'friends',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
            ],
            options={
                'db_table': 'likes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.TextField()),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
            ],
            options={
                'db_table': 'messages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.CharField(max_length=225)),
                ('url', models.CharField(max_length=225)),
                ('flag', models.IntegerField()),
                ('created_dt', models.DateTimeField()),
            ],
            options={
                'db_table': 'notifications',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('contents', models.CharField(max_length=500)),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
                ('tags', models.CharField(blank=True, max_length=255, null=True)),
                ('comments_count', models.IntegerField(blank=True, null=True)),
                ('likes_count', models.IntegerField(blank=True, null=True)),
                ('updated_dt', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'posts',
                'ordering': ['-created_dt'],
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('last_message', models.TextField()),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
                ('updated_dt', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rooms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrackGenres',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'track_genres',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('track_source', models.CharField(max_length=80)),
                ('image', models.CharField(blank=True, max_length=225, null=True)),
                ('flag', models.IntegerField(blank=True, null=True)),
                ('users_idx', models.CharField(max_length=255)),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
                ('played_count', models.IntegerField(blank=True, null=True)),
                ('moods', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'tracks',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrackTypes',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'track_types',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=45, unique=True)),
                ('pw', models.CharField(max_length=80)),
                ('nickname', models.CharField(blank=True, max_length=45, null=True)),
                ('email', models.CharField(max_length=45)),
                ('profile', models.CharField(blank=True, max_length=500, null=True)),
                ('salt', models.CharField(max_length=64)),
                ('follower_count', models.IntegerField(blank=True, null=True)),
                ('following_count', models.IntegerField(blank=True, null=True)),
                ('tracks_count', models.IntegerField(blank=True, null=True)),
                ('grade', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
                ('access_dt', models.DateTimeField(blank=True, null=True)),
                ('updated_dt', models.DateTimeField(blank=True, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=225, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsersHasTracks',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('created_dt', models.DateTimeField(default=datetime.datetime(2020, 2, 27, 8, 57, 32, 148586))),
            ],
            options={
                'db_table': 'users_has_tracks',
                'managed': False,
            },
        ),
    ]
