from django.urls import path

from . import views

app_name = 'request'

urlpatterns = [
    path('train/', views.train_view, name='train-view'),
    path('predict/<text>', views.predict_view),
]