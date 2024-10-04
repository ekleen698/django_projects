from django.urls import path

from .views import (CatList, CatCreate, CatUpdate, CatDelete,
                    BreedList, BreedCreate, BreedUpdate, BreedDelete)

app_name = 'cats'
urlpatterns = [
    path('', CatList.as_view(), name='cat_all'),
    path('main/create/', CatCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', CatUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', CatDelete.as_view(), name='cat_delete'),
    path('lookup/', BreedList.as_view(), name='breed_list'),
    path('lookup/create/', BreedCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', BreedUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', BreedDelete.as_view(), name='breed_delete'),
]