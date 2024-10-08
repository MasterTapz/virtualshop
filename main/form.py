from django import forms
from django.utils.html import strip_tags
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'status']

    def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data['description']
        return strip_tags(description)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_status(self):
        status = self.cleaned_data['status']
        valid_status_choices = [choice[0] for choice in Product.STATUS_CHOICES]
        if status not in valid_status_choices:
            raise forms.ValidationError("Invalid status selected.")
        return status
