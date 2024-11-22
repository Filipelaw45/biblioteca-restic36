import pytest
from rest_framework.test import APIClient
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_403_FORBIDDEN,
    HTTP_401_UNAUTHORIZED,
)
from .factories import UserFactory, ColecaoFactory, LivroFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def authenticated_user(api_client):
    user = UserFactory()
    api_client.force_authenticate(user)
    return user


@pytest.mark.django_db
def test_criar_colecao(api_client, authenticated_user):
    livro = LivroFactory()
    data = {
        "nome": "Minha Coleção",
        "descricao": "Coleção de teste",
        "livros": [livro.id],
    }
    response = api_client.post("/colecoes/", data)
    assert response.status_code == HTTP_201_CREATED
    assert response.data["colecionador"] == authenticated_user.id


@pytest.mark.django_db
def test_permissao_editar_colecao(api_client, authenticated_user):
    colecao = ColecaoFactory(colecionador=authenticated_user)
    data = {"nome": "Novo Nome"}
    response = api_client.patch(f"/colecoes/{colecao.id}/", data)
    assert response.status_code == HTTP_200_OK
    assert response.data["nome"] == "Novo Nome"


@pytest.mark.django_db
def test_bloquear_edicao_por_outro_usuario(api_client):
    colecao = ColecaoFactory()
    api_client.force_authenticate(UserFactory())
    data = {"nome": "Tentativa"}
    response = api_client.patch(f"/colecoes/{colecao.id}/", data)
    assert response.status_code == HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_bloquear_acesso_nao_autenticado(api_client):
    colecao = ColecaoFactory()
    response = api_client.delete(f"/colecoes/{colecao.id}/")
    assert response.status_code == HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_listar_colecoes(api_client, authenticated_user):
    ColecaoFactory(colecionador=authenticated_user)
    response = api_client.get("/colecoes/")
    assert response.status_code == HTTP_200_OK
    assert len(response.data) > 0
