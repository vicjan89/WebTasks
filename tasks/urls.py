from django.urls import path

from .views import index, by_label, TaskCreateView, attachment, TaskDetaiView, TaskUpdateView

urlpatterns = [
    path('', index, name='index'),
    path('attachment/', attachment, name='attachment'),
    path('add/', TaskCreateView.as_view(), name='add'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='edit'),
    path('task/<int:pk>/', TaskDetaiView.as_view(), name='detail'),
    path('<int:label_id>/', by_label, name='by_label'),
]