from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "products_list.html", context)


def contacts(request):
    return render(request, "contacts.html")


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)  # Получаем товар по ID
    return render(request, "catalog/product_detail.html", {"product": product})
