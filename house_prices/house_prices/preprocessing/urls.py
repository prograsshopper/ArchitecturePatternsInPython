from django.urls import path

from house_prices.house_prices.preprocessing.views import CSVDataView

main_patterns = [
    path('csv/', CSVDataView.as_view(), name='csv-data'),
]