from django.urls import path
from . import views

app_name = "sample_forms"

urlpatterns = [
    # path("", views.PlanBuyCarsVactionsListView.as_view(), name="plan_by_cars_vactions"),
    path("", views.home, name="home"),
    path("plan_buy_car_vactions_table", views.plan_buy_car_vactions_table, name="plan_buy_car_vactions_table"),
    path("plan_by_cars_vactions_table_data", views.plan_buy_car_vactions_table_data, name="plan_by_cars_vactions_table_data"),
    path('plan_by_cars_vactions_edit/<int:pk>/', views.PlanBuyCarsVactionsEditView.as_view(), name='plan_by_cars_vactions_edit'),
    # path('delete_first_form/<int:pk>/', views.delet_row_first_model, name='delete_first_form'),
    path("plan_buy_car_vactions_form", views.plan_buy_car_vactions_form, name="plan_buy_car_vactions_form"),
    path('plan_by_cars_vactions_delete/<int:pk>/', views.PlanBuyCarsVactionsDeleteView.as_view(), name='plan_by_cars_vactions_delete'),
    
]
