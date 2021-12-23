from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createtask', views.createtask, name='createtask'),
    path('alltask', views.alltask, name='alltask'),
    path('deletetask/<int:id>', views.deletetask, name='deletetask'),
    path('edittask/<int:id>', views.edittask, name='edittask'),  
]
