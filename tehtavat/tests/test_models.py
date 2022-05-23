import pytest

from ..models import Kategoria


@pytest.mark.parametrize("nimi", ["", "hei"])
def test_kategoria_init(nimi):
    kategoria = Kategoria(nimi=nimi)

    assert kategoria.id is None
    assert kategoria.nimi == nimi



@pytest.mark.django_db
def test_kategoria_tallennus():
    kategoria = Kategoria(nimi="moi")

    # Ennen tallennusta id on None
    assert kategoria.id is None

    kategoria.save()

    assert kategoria.nimi == "moi"
    assert kategoria.id
    assert isinstance(kategoria.id, int)


@pytest.mark.django_db
def test_kategoria_create():
    kategoria = Kategoria.objects.create(nimi="moi")

    assert kategoria.id, "Pitäisi olla id, eli on tallennettu tietokantaan"


@pytest.mark.parametrize("filtteri,odotettu_tulos", [
    (dict(nimi__contains="o"), {"moi"}),
    (dict(nimi__contains="i"), {"moi", "hei"}),
    (dict(nimi__startswith="h"), {"hei"}),
    (dict(nimi__startswith="h", nimi__contains="o"), set()),
])
@pytest.mark.django_db
def test_kategoria_filter(filtteri, odotettu_tulos):
    kategoria1 = Kategoria.objects.create(nimi="moi")
    kategoria2 = Kategoria.objects.create(nimi="hei")

    tulos = Kategoria.objects.filter(**filtteri)

    assert set(x.nimi for x in tulos) == odotettu_tulos
