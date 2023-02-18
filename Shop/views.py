from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from cart.forms import CartAddProductForm, ShortCartAddProductForm
from .models import Category, Product, ProductImage


# Create your views here.
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'shop/index.html',
        {
            'title': 'Home Page',
            # 'staticfiles' : 'static'
            'year': datetime.now().year,
        }
    )


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = ShortCartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'Shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'cart_product_form': cart_product_form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    products_photo = ProductImage.objects.filter(product_id=id)
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        'cart_product_form': cart_product_form,
                                                        'products_photo': products_photo})


def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST":  # после отправки формы

        regform = UserCreationForm(request.POST)

        if regform.is_valid():  # валидация полей формы
            reg_f = regform.save(commit=False)  # не сохраняем автоматически данные формы
            reg_f.is_staff = False  # запрещен вход в административный раздел
            reg_f.is_active = True  # активный пользователь
            reg_f.is_superuser = False  # не является суперпользователем
            reg_f.date_joined = datetime.now()  # дата регистрации
            reg_f.last_login = datetime.now()  # дата последней авторизации
            reg_f.save()  # сохраняем изменения после добавления данных
            return redirect('product_list')  # переадресация на главную страницу после регистрации

    else:

        regform = UserCreationForm()  # создание объекта формы для ввода данных нового пользователя

    return render(
        request,
        'shop/registration.html',
        {
            'regform': regform,  # передача формы в шаблон веб-страницы

            'year': datetime.now().year,
        }

    )
