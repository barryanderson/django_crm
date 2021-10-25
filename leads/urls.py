from django.urls import path

from leads.views import lead_detail, lead_list, lead_create, lead_update, lead_delete

urlpatterns = [
    path('', lead_list),
    path('create/', lead_create),
    path('<int:pk>/update/', lead_update),
    path('<int:pk>/delete/', lead_delete),
    path('<int:pk>', lead_detail)
]
