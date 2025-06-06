# Generated by Django 5.2.1 on 2025-05-30 20:25

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empIdentificacion', models.CharField(max_length=10, unique=True)),
                ('empNombres', models.CharField(max_length=50)),
                ('empApellidos', models.CharField(max_length=50)),
                ('empCorreo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ofiNombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('usuEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPqrs.empleados')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='empleados',
            name='empOficina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPqrs.oficina'),
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solCodigo', models.CharField(max_length=20, unique=True)),
                ('solForma', models.CharField(choices=[('Anonimo', 'Anonimo'), ('Correo Electronico', 'Correo Electronico')], default='Correo Electronico', max_length=20)),
                ('solTipo', models.CharField(choices=[('Peticion', 'Peticion'), ('Queja', 'Queja'), ('Reclamo', 'Reclamo')], default='Peticion', max_length=10)),
                ('solBarrio', models.CharField(blank=True, max_length=50)),
                ('solNombreCiudadano', models.CharField(blank=True, max_length=50, null=True)),
                ('solCorreoElectronico', models.CharField(blank=True, max_length=50, null=True)),
                ('solDescripcion', models.TextField()),
                ('solFecha', models.DateField(auto_now_add=True)),
                ('solEstado', models.CharField(choices=[('Solicitada', 'Solicitada'), ('Atendidad', 'Atendida')], default='Solicitada', max_length=20)),
                ('solOficina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPqrs.oficina')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestSolicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resDescripcion', models.TextField()),
                ('resUrlAnexo', models.FileField(upload_to='Anexossolicitudes/')),
                ('resFecha', models.DateField(auto_now_add=True)),
                ('resEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPqrs.empleados')),
                ('resSolicitud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPqrs.solicitud')),
            ],
        ),
        migrations.CreateModel(
            name='AnexoSolicitudes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aneUrl', models.FileField(blank=True, null=True, upload_to='anexos/')),
                ('aneSolicitud', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appPqrs.solicitud')),
            ],
        ),
    ]
