from django.urls import path

from .views import CSVDataView

urlpatterns = [
    path('csv/', CSVDataView.as_view(), name='csv-data'),
]