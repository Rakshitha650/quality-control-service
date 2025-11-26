from django.urls import path
from .views import (
    ClinicViewset,
    DepartmentViewset,
    EquipmentViewset,
    EquipmentDetailsViewset,
    ParametersViewset
    )

urlpatterns = [
    path('clinic/', ClinicViewset.as_view()),
    path('clinic/<int:id>/', ClinicViewset.as_view()),

    path('department/', DepartmentViewset.as_view()),
    path('department/<int:id>/', DepartmentViewset.as_view()),

    path('equipment/', EquipmentViewset.as_view()),
    path('equipment/<int:id>/', EquipmentViewset.as_view()),

    path('equipment-details/', EquipmentDetailsViewset.as_view()),
    path('equipment-details/<int:id>/', EquipmentDetailsViewset.as_view()),

     path('parameters/', ParametersViewset.as_view()),
    path('parameters/<int:id>/', ParametersViewset.as_view()),
]
