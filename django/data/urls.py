from django.urls import path

from .views import DataRetrieveUpdateDestroyView, DataListPostView

app_name = 'data'

urlpatterns = [
    # Database retrieve,update,partial_update,delete
    path('datas/<int:id>', DataRetrieveUpdateDestroyView.as_view(), name='data-retrieve-update-delete'),
    # Database get,post
    path('datas', DataListPostView.as_view(), name='data-list-post'),
]
