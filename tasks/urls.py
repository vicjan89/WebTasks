from django.urls import path

from .views import index, by_label, TaskCreateView

urlpatterns = [
    path('', index, name='index'),
    path('add/', TaskCreateView.as_view(), name='add'),
    path('<int:label_id>/', by_label, name='by_label'),
]