from django.urls import path
from . import views

# Nombre del espacio de nombres de la app
app_name = 'app_videojuegos'

urlpatterns = [
    # Ruta para la lista de sucursales (página principal)
    path('', views.SucursalListView.as_view(), name='listar_sucursales'),
    
    # Ruta para el detalle de una sucursal
    path('sucursal/<int:pk>/', views.SucursalDetailView.as_view(), name='detalle_sucursal'),
    
    # Ruta para crear una nueva sucursal
    path('sucursal/nueva/', views.SucursalCreateView.as_view(), name='crear_sucursal'),
    
    # Ruta para editar una sucursal existente
    path('sucursal/<int:pk>/editar/', views.SucursalUpdateView.as_view(), name='editar_sucursal'),
    
    # Ruta para borrar una sucursal
    path('sucursal/<int:pk>/borrar/', views.SucursalDeleteView.as_view(), name='borrar_sucursal'),
]