from django.core.management.base import BaseCommand
from core.models import Categoria, Autor, Livro


class Command(BaseCommand):
    help = "Cria registros de exemplo no banco de dados"

    def handle(self, *args, **options):
        categoria_fantasia = Categoria.objects.create(nome="Fantasia")
        categoria_ficcao = Categoria.objects.create(nome="Ficção")
        categoria_aventura = Categoria.objects.create(nome="Aventura")
        categoria_historia = Categoria.objects.create(nome="História")
        categoria_misterio = Categoria.objects.create(nome="Mistério")
        categoria_romance = Categoria.objects.create(nome="Romance")

        autor_jk_rowling = Autor.objects.create(nome="J.K. Rowling")
        autor_dan_brown = Autor.objects.create(nome="Dan Brown")
        autor_mary_shelley = Autor.objects.create(nome="Mary Shelley")
        autor_fj_scott = Autor.objects.create(nome="F. Scott Fitzgerald")
        autor_mark_twain = Autor.objects.create(nome="Mark Twain")

        Livro.objects.create(
            titulo="Harry Potter e a Pedra Filosofal",
            autor=autor_jk_rowling,
            categoria=categoria_fantasia,
            publicado_em="1997-06-26",
        )
        Livro.objects.create(
            titulo="Harry Potter e a Câmara Secreta",
            autor=autor_jk_rowling,
            categoria=categoria_fantasia,
            publicado_em="1998-07-02",
        )
        Livro.objects.create(
            titulo="O Código Da Vinci",
            autor=autor_dan_brown,
            categoria=categoria_misterio,
            publicado_em="2003-03-18",
        )
        Livro.objects.create(
            titulo="Orgulho e Preconceito",
            autor=autor_mary_shelley,
            categoria=categoria_romance,
            publicado_em="1813-01-28",
        )
        Livro.objects.create(
            titulo="O Grande Gatsby",
            autor=autor_fj_scott,
            categoria=categoria_romance,
            publicado_em="1925-04-10",
        )
        Livro.objects.create(
            titulo="As Aventuras de Tom Sawyer",
            autor=autor_mark_twain,
            categoria=categoria_aventura,
            publicado_em="1876-06-01",
        )
        Livro.objects.create(
            titulo="Frankenstein",
            autor=autor_mary_shelley,
            categoria=categoria_ficcao,
            publicado_em="1818-01-01",
        )
