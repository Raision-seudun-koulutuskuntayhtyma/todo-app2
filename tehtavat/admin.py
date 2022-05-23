from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Kategoria, Tehtava


class TehtyFilter(SimpleListFilter):
    title = _('Tehty')

    parameter_name = 'tehty'

    def lookups(self, request, model_admin):
        return (
            (None, "Tekemättömät"),
            ('tehty', _('Tehdyt')),
            ('kaikki', _('Kaikki')),
        )

    def choices(self, cl):
        for (lookup, title) in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        value = self.value()
        if value is None:
            return queryset.filter(tehty=False)
        elif value == 'tehty':
            return queryset.filter(tehty=True)
        return queryset


@admin.register(Tehtava)
class TehtavaAdmin(admin.ModelAdmin):
    list_display = ["id", "otsikko", "kategoria"]

    list_filter = [TehtyFilter] 


@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    pass
