# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AtModelos(models.Model):
    area = models.ForeignKey('Areasdetrabajo', models.DO_NOTHING, db_column='Area', blank=True, null=True)  # Field name made lowercase.
    modelo = models.ForeignKey('Modelos', models.DO_NOTHING, db_column='Modelo', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AT_Modelos'


class AtPiezas(models.Model):
    area = models.OneToOneField('Areasdetrabajo', models.DO_NOTHING, db_column='Area', primary_key=True)  # Field name made lowercase. The composite primary key (Area, Pieza) found, that is not supported. The first column is selected.
    pieza = models.ForeignKey('Piezas', models.DO_NOTHING, db_column='Pieza')  # Field name made lowercase.
    cantidadpieza = models.IntegerField(db_column='CantidadPieza')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AT_Piezas'
        unique_together = (('area', 'pieza'),)


class Actividades(models.Model):
    numero = models.AutoField(primary_key=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    tarea = models.ForeignKey('Tareas', models.DO_NOTHING, db_column='Tarea', blank=True, null=True)  # Field name made lowercase.
    estado = models.ForeignKey('Estados', models.DO_NOTHING, db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Actividades'


class Areasdetrabajo(models.Model):
    numero = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AreasDeTrabajo'
        
    def __str__(self):
        return self.nombre


class BitAct(models.Model):
    bitacora = models.ForeignKey('Bitacoras', models.DO_NOTHING, db_column='Bitacora', blank=True, null=True)  # Field name made lowercase.
    actividad = models.ForeignKey(Actividades, models.DO_NOTHING, db_column='Actividad', blank=True, null=True)  # Field name made lowercase.
    tiempo = models.TimeField(db_column='Tiempo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bit_Act'


class BitTarea(models.Model):
    bitacora = models.ForeignKey('Bitacoras', models.DO_NOTHING, db_column='Bitacora', blank=True, null=True)  # Field name made lowercase.
    tarea = models.ForeignKey('Tareas', models.DO_NOTHING, db_column='Tarea', blank=True, null=True)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='FechaFinal', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.TimeField(db_column='HoraInicio')  # Field name made lowercase.
    horafinal = models.TimeField(db_column='HoraFinal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bit_Tarea'


class Bitacoras(models.Model):
    numero = models.AutoField(primary_key=True)
    titulo = models.CharField(db_column='Titulo', max_length=30)  # Field name made lowercase.
    empleado = models.ForeignKey('Empleados', models.DO_NOTHING, db_column='Empleado', blank=True, null=True)  # Field name made lowercase.
    metas = models.ForeignKey('Metas', models.DO_NOTHING, db_column='metas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Bitacoras'


class Empleados(models.Model):
    numero = models.AutoField(primary_key=True)
    usuario = models.CharField(db_column='Usuario', unique=True, max_length=30)  # Field name made lowercase.
    contrasena = models.CharField(db_column='Contrasena', max_length=15)  # Field name made lowercase.
    nombrepila = models.CharField(db_column='NombrePila', max_length=30)  # Field name made lowercase.
    primerapellido = models.CharField(db_column='PrimerApellido', max_length=30, blank=True, null=True)  # Field name made lowercase.
    segundoapellido = models.CharField(db_column='SegundoApellido', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dircalle = models.CharField(db_column='DirCalle', max_length=30)  # Field name made lowercase.
    dirnumero = models.CharField(db_column='DirNumero', max_length=30)  # Field name made lowercase.
    dircolonia = models.CharField(db_column='DirColonia', max_length=30)  # Field name made lowercase.
    numtel = models.CharField(db_column='NumTel', max_length=15)  # Field name made lowercase.
    horario = models.CharField(db_column='Horario', max_length=30)  # Field name made lowercase.
    jefearea = models.ForeignKey('self', models.DO_NOTHING, db_column='JefeArea', blank=True, null=True)  # Field name made lowercase.
    areatrabajo = models.ForeignKey(Areasdetrabajo, models.DO_NOTHING, db_column='AreaTrabajo', blank=True, null=True)  # Field name made lowercase.
    puesto = models.ForeignKey('Puestos', models.DO_NOTHING, db_column='Puesto', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Empleados'
    
    


class Errores(models.Model):
    numero = models.AutoField(primary_key=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    bitacora = models.ForeignKey(Bitacoras, models.DO_NOTHING, db_column='Bitacora', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Errores'


class Estados(models.Model):
    numero = models.AutoField(primary_key=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estados'


class Materiales(models.Model):
    numero = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Materiales'


class Metas(models.Model):
    numero = models.AutoField(primary_key=True)
    meta = models.CharField(db_column='Meta', max_length=100)  # Field name made lowercase.
    fechainicio = models.DateField(db_column='FechaInicio')  # Field name made lowercase.
    fechafinal = models.DateField(db_column='FechaFinal')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Metas'


class ModeloPiezas(models.Model):
    modelo = models.ForeignKey('Modelos', models.DO_NOTHING, db_column='Modelo', blank=True, null=True)  # Field name made lowercase.
    pieza = models.ForeignKey('Piezas', models.DO_NOTHING, db_column='Pieza', blank=True, null=True)  # Field name made lowercase.
    totalpiezas = models.IntegerField(db_column='TotalPiezas')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modelo_Piezas'


class Modelos(models.Model):
    numero = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Modelos'


class Piezas(models.Model):
    numero = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Piezas'


class PiezasMaterial(models.Model):
    pieza = models.ForeignKey(Piezas, models.DO_NOTHING, db_column='Pieza', blank=True, null=True)  # Field name made lowercase.
    material = models.ForeignKey(Materiales, models.DO_NOTHING, db_column='Material', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Piezas_Material'


class Puestos(models.Model):
    numero = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Puestos'
    
    def __str__(self):
        return self.nombre


class Soluciones(models.Model):
    numero = models.AutoField(primary_key=True)
    descripcion = models.CharField(db_column='Descripcion', max_length=100)  # Field name made lowercase.
    bitacora = models.ForeignKey(Bitacoras, models.DO_NOTHING, db_column='Bitacora', blank=True, null=True)  # Field name made lowercase.
    error = models.ForeignKey(Errores, models.DO_NOTHING, db_column='Error', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Soluciones'


class Tareas(models.Model):
    numero = models.AutoField(primary_key=True)
    orden = models.CharField(db_column='Orden', max_length=100)  # Field name made lowercase.
    areatrabajo = models.ForeignKey(Areasdetrabajo, models.DO_NOTHING, db_column='AreaTrabajo', blank=True, null=True)  # Field name made lowercase.
    estado = models.ForeignKey(Estados, models.DO_NOTHING, db_column='Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tareas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
