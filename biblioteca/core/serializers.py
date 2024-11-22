from rest_framework import serializers
from .models import Categoria, Autor, Livro, Colecao


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ("id", "nome")


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ("id", "nome")


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ("id", "titulo", "autor", "categoria", "publicado_em")


class ColecaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colecao
        fields = ["id", "nome", "descricao", "colecionador"]
        read_only_fields = ["id", "colecionador"]
