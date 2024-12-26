from django.urls import path
from . import views

app_name = 'tracks'

urlpatterns = [
    path('list/', views.track_list, name='list'),
    path('create/', views.track_create, name='create'),
    path('detail/<int:detail_id>', views.track_detail, name='detail'),
    path('update/<int:update_id>/', views.music_update, name='update'),
    path('delete/<int:del_id>/', views.music_delete, name='delete'),
]