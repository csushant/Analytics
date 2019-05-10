from django.urls import path
from . import views

app_name = 'numapp'
urlpatterns = [
                path('housingdata', views.HousingDataCreateView,
                            name='housingdata'),
                path('', views.MlModelsView, name='ml'),
                path('sendhousingdata', views.HousingDataCreateView, name='sendhousingdata'),
]