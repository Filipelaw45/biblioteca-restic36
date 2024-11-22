import factory
from django.contrib.auth.models import User
from core.models import Autor, Categoria, Livro, Colecao


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")


class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria

    nome = factory.Faker("word")


class AutorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Autor

    nome = factory.Faker("name")


class LivroFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Livro

    titulo = factory.Faker("sentence", nb_words=3)
    autor = factory.SubFactory(AutorFactory)
    categoria = factory.SubFactory(CategoriaFactory)
    publicado_em = factory.Faker("date")


class ColecaoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Colecao

    nome = factory.Faker("word")
    descricao = factory.Faker("text")
    colecionador = factory.SubFactory(UserFactory)
