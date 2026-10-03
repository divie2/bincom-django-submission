from django.contrib import admin
from django.urls import path
from bincom_app import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("polling-unit/", views.polling_unit_result, name="polling_unit_result"),
    path("lga-results/", views.lga_results, name="lga_results"),
    path("polling-unit/new/", views.create_polling_unit, name="create_polling_unit"),
]
