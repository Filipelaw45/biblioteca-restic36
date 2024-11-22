from django.urls import path
from . import views
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path("livros/", views.LivroList.as_view(), name=views.LivroList.name),
    path("livros/<int:pk>/", views.LivroDetail.as_view(), name=views.LivroDetail.name),
    path("autores/", views.AutorList.as_view(), name=views.AutorList.name),
    path("autores/<int:pk>/", views.AutorDetail.as_view(), name=views.AutorDetail.name),
    path("categorias/", views.CategoriaList.as_view(), name=views.CategoriaList.name),
    path(
        "categorias/<int:pk>/",
        views.CategoriaDetail.as_view(),
        name=views.CategoriaDetail.name,
    ),
    path(
        "colecoes/",
        views.ColecaoListCreate.as_view(),
        name=views.ColecaoListCreate.name,
    ),
    path(
        "colecoes/<int:pk>/",
        views.ColecaoDetail.as_view(),
        name=views.ColecaoDetail.name,
    ),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
