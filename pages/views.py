from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import TemplateView , ListView
from django.views import View 
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from .models import Product 
 
class Product: 
    products = [ 
        {"id":"1", "name":"TV", "description":"Best TV", "price":50}, 
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price":150}, 
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price":80}, 
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price":30} 
    ] 

class ProductIndexView(View): 
    template_name = 'products/index.html' 

    def get(self, request): 
        viewData = {} 
        viewData["title"] = "Products - Online Store" 
        viewData["subtitle"] =  "List of products" 
        viewData["products"] = Product.objects.all() 
    
        return render(request, self.template_name, viewData) 

class ProductShowView(View): 
    template_name = 'products/show.html' 
 
    def get(self, request, id):  
        try: 
            product_id = int(id) 
            if product_id < 1: 
                raise ValueError("Product id must be 1 or greater") 
            product = get_object_or_404(Product, pk=product_id) 
        except (ValueError, IndexError): 
            # If the product id is not valid, redirect to the home page 
            return HttpResponseRedirect(reverse('home')) 
         
        viewData = {} 
        product = get_object_or_404(Product, pk=product_id) 
        viewData["title"] = product.name + " - Online Store" 
        viewData["subtitle"] =  product.name + " - Product information" 
        viewData["product"] = product 
 
        return render(request, self.template_name, viewData) 

class ProductListView(ListView): 
    model = Product 
    template_name = 'product_list.html' 
    context_object_name = 'products'  # This will allow you to loop through 'products' in your template 
 
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['title'] = 'Products - Online Store' 
        context['subtitle'] = 'List of products' 
        return context    


class HomePageView(TemplateView): 
    template_name = "pages/home.html"

class AboutPageView(TemplateView): 
    template_name = 'pages/about.html' 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context.update({ 
            "title": "About us - Online Store", 
            "subtitle": "About us", 
            "description": "This is an about page ...", 
            "author": "Developed by: Alberto Diaz", 
        }) 
    
        return context 
    
class ContactPageView(View):
    template_name = 'pages/contact.html'
    def get(self, request):
        viewData = {}
        viewData["email"] = "example@eafit.edu.co"
        viewData["address"] =  "cra 1231 # as - bc"
        viewData["phoneNumber"] = "3128861871"

        return render(request, self.template_name, viewData)

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    description = forms.CharField(required=True)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price is not None and price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price
    
class ProductCreateView(View):
    template_name = 'pages/products/create.html'

    def get(self, request):
        form = ProductForm()
        viewData = {
            'form': form,
            'title': 'Create Product'            
        }
        return render(request, self.template_name, viewData)

    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']

            new_product = {
            'id': str(len(Product.products) + 1),
            'name': name,
            'price': price,
            'description': description
            }
            Product.products.append(new_product)
            return redirect('success') 
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        
        
class SuccessPageView(TemplateView):
    template_name = 'pages/products/success.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
        })
        return context