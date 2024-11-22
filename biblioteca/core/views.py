from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Livro, Categoria, Autor, Colecao
from .serializers import (
    LivroSerializer,
    AutorSerializer,
    CategoriaSerializer,
    ColecaoSerializer,
)
from rest_framework.reverse import reverse
from rest_framework.response import Response
from core.filters import LivroFilter
from .custom_permissions import IsColecionadorOrReadOnly


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "livros": reverse("livro-list", request=request),
                "autores": reverse("autor-list", request=request),
                "categorias": reverse("categoria-list", request=request),
                "colecoes": reverse("colecao-list", request=request),
            }
        )


class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-list"
    filterset_class = LivroFilter
    ordering_fields = (
        "titulo",
        "autor",
        "categoria",
        "publicado_em",
    )


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = "livro-detail"


class AutorList(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-list"
    search_fields = ("^nome",)
    ordering_fields = ("nome",)


class AutorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    name = "autor-detail"


class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-list"
    search_fields = ("^nome",)
    ordering_fields = ("nome",)


class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    name = "categoria-detail"


class ColecaoListCreate(generics.ListCreateAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = "colecao-list"
    search_fields = ("^nome",)
    ordering_fields = ("nome",)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(colecionador=self.request.user)


class ColecaoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Colecao.objects.all()
    serializer_class = ColecaoSerializer
    name = "colecao-detail"
    search_fields = ("^nome",)
    ordering_fields = ("nome",)
    permission_classes = [IsColecionadorOrReadOnly]
