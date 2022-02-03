from django.urls import path

from .views import DataRetrieveUpdateDestroyView, DataListPostView

app_name = 'data'

urlpatterns = [
    path('datas/<int:id>', DataRetrieveUpdateDestroyView.as_view(), name='data-retrieve-update-delete'),
    path('datas', DataListPostView.as_view(), name='data-list-post'),
]
