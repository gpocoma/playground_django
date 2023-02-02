from django.urls import path
from app.views import *

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('estudiante_list_view', EstudianteListView.as_view(), name='estudiante_list_view'),
    path('estudiante_create_view', EstudianteCreateView.as_view(), name='estudiante_create_view'),
    path('estudiante_update_view/<pk>', EstudianteUpdateView.as_view(), name='estudiante_update_view'),
    path('estudiante_delete_view/<pk>', EstudianteDeleteView.as_view(), name='estudiante_delete_view'),
    path('estudiante_detail_view/<pk>', EstudianteDetailView.as_view(), name='estudiante_detail_view')
]
