from django.contrib import admin
from .models import Category, Product, ProductImage


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProductImage, ProductImageAdmin)


class ProductImageInline(admin.StackedInline):
    model = ProductImage
    max_num = 10
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug', 'main_image', 'video', 'price', 'stock',
                    'available', 'created', 'updated']
    list_filter = ['category', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline, ]


admin.site.register(Product, ProductAdmin)
