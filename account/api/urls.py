from django.urls import path

from account.api.views import api_register_view


app_name='account_api'

urlpatterns = [
        path('register/',api_register_view,name='api_register'),
    

]