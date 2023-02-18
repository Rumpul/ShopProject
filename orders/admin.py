from django.contrib import admin
from .models import Order, OrderItem
from import_export.admin import ExportActionMixin


# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class ExportActionMixinRus(ExportActionMixin):

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions.update(
            export_admin_action=(ExportActionMixin.export_admin_action,
                                 "export_admin_action",
                                 "Экспортировать выбранные %(verbose_name_plural)s",
                                 )
        )
        return actions


class OrderAdmin(ExportActionMixinRus, admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    search_fields = ['id', 'first_name', 'last_name', 'email',
                     'address', 'postal_code', 'city', 'paid',
                     'created', 'updated']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
