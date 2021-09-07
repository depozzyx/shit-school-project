from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("category/<int:category_id>/", views.category, name="category"),
    path("order/<int:product_id>/", views.order, name="order"),
]
