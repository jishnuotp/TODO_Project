from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:task_id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('cbvlist',views.Tasklistview.as_view(),name='cbvlist'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate')
]
