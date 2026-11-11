from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),         # ← Esta é a rota que estava faltando!
    path("sobre/", views.sobre, name="sobre"),
]