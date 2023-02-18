from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .services import open_file
from Shop.models import Category, Product, ProductImage


# Create your views here.

def reviews_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'product_reviews/reviews_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def review_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    products_photo = ProductImage.objects.filter(product_id=id)
    return render(request, 'product_reviews/review_detail.html', {'product': product,
                                                                  'products_photo': products_photo})


def get_streaming_video(request, id: int):
    file, status_code, content_length, content_range = open_file(request, id)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response
