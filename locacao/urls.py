from django.urls import path

from locacao.views import *

urlpatterns = [
    path('', list_locacao, name='list_locacao'),
    path('new', create_locacao, name='create_locacao'),
    path('update/<int:id>/', update_locacao, name='update_locacao'),
    path('delete/<int:id>/', delete_locacao, name='delete_locacao'),
]
