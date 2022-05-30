import pytest
from django.http import HttpResponse
from django.urls import reverse

from ..models import Tehtava


@pytest.mark.django_db
def test_etusivu(client):
    url = reverse('etusivu')

    tulos = client.get(url)

    assert isinstance(tulos, HttpResponse)
    assert tulos.status_code == 200
    assert "Etusivu" in tulos.content.decode("utf-8")


@pytest.mark.django_db
def test_tehtava_sivu(client):
    tehtava = Tehtava.objects.create(otsikko="Aja testit")
    url = reverse('tehtava', kwargs={'id': tehtava.id})

    vastaus = client.get(url)

    assert isinstance(vastaus, HttpResponse)
    assert vastaus.status_code == 200
    html_sisalto = vastaus.content.decode("utf-8")
    assert "<title>Tehtävä: Aja testit</title>" in html_sisalto


@pytest.mark.django_db
def test_tehtava_sivu_ei_loydy(client):
    url = reverse('tehtava', kwargs={'id': 0})

    vastaus = client.get(url)

    assert isinstance(vastaus, HttpResponse)
    assert vastaus.status_code == 404
    assert "Tehtävää 0 ei löydy." in vastaus.content.decode("utf-8")
