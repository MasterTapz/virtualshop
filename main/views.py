from django.shortcuts import render
from .models import Product  # Import the Product model

def show_main(request):
    # Fetch all products from the database
    products = Product.objects.all()

    context = {
        'app_name': 'VirtualShop',
        'name': 'Muhammad Brian Subekti',
        'products': products  # Pass the products from the database to the template
    }

    return render(request, "main.html", context)