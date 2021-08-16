from django.urls import path

from .views import createitem, index, detail, createlist, deletelist, deleteitem, updatelist, updateitem

app_name='todo'
urlpatterns = [
    path('', index, name='index'),
    path('<int:list_id>/', detail, name='list_details'),
    path('createlist/', createlist, name='list_create'),
    path('createitem/', createitem, name='item_create'),
    path('delete/<int:list_id>/', deletelist, name="list_delete" ),
    path('<int:list_id>/delete/<int:item_id>/', deleteitem, name='item_delete'),
    path('update/<int:list_id>/', updatelist, name='list_update'),
    path('<int:List_id>/update/<int:item_id>/', updateitem, name = 'item_update'),
    path('<int:List_id>/createitem/', createitem, name = 'create_item'),
]