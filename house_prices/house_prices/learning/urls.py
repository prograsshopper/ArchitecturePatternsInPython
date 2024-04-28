from django.urls import path

from .views import MLModelViewSet

urlpatterns = [
    path('model', MLModelViewSet.as_view(), name='ml-model'),
]