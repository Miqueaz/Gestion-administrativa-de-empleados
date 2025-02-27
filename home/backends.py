# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import Empleados

# class NombrepilaBackend(ModelBackend):
#     def authenticate(self, request, nombrepila=None, password=None, **kwargs):
#         try:
#             # Obtener el usuario con el nombrepila proporcionado
#             user = Empleados.objects.get(nombrepila=nombrepila)
            
#             # Verificar la contraseña del usuario
#             if user.check_password(password):
#                 return user
#         except Empleados.DoesNotExist:
#             # Si el usuario no existe, o la contraseña es incorrecta, devolver None
#             return None

#     def get_user(self, user_id):
#         try:
#             # Obtener el usuario por su ID
#             return Empleados.objects.get(pk=user_id)
#         except Empleados.DoesNotExist:
#             return None

