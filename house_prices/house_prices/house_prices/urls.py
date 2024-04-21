from django.contrib import admin
from django.urls import path, include

from .views import MainView

urlpatterns = [
    path('', MainView.as_view()),
    path('admin/', admin.site.urls),

    path('preprocessing/', include('preprocessing.urls')),
]
