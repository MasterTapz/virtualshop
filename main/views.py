from django.shortcuts import render,redirect
from main.models import Product  # Import the Product model
from main.form import ProductForm

from django.http import HttpResponse
from django.core import serializers


def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")



def create_product_entry(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product_entry.html", context)


def show_main(request):
    # Fetch all products from the database
    products = Product.objects.all()

    context = {
        'app_name': 'VirtualShop',
        'name': 'Muhammad Brian Subekti',
        'products': products
        
    }

    return render(request, "main.html", context)