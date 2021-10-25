from django.urls import path

from leads.views import lead_detail, lead_list, lead_create

urlpatterns = [
    path('', lead_list),
    path('create/', lead_create),
    path('<int:pk>', lead_detail)
]
