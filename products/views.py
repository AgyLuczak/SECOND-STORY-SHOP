from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.urls import reverse

from .models import Product, Category  # Correct import for your models
from .forms import ProductForm

def all_products(request):
    products = Product.objects.all()
    current_categories = Category.objects.all()
    query = None
    categories = None
    sortkey = request.GET.get('sort', None)
    direction = request.GET.get('direction', 'asc')

    # Initialize flags
    is_sorting_default = True
    is_price_asc = is_price_desc = is_name_asc = is_name_desc = is_category_asc = is_category_desc = False

    if sortkey and direction:
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))
        elif sortkey == 'category':
            sortkey = 'category__name'

        # Apply sorting
        if direction == 'desc':
            sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

        # Update flags based on current_sorting
        current_sorting = f'{sortkey}_{direction}'
        is_sorting_default = False
        is_price_asc = current_sorting == 'price_asc'
        is_price_desc = current_sorting == 'price_desc'
        is_name_asc = current_sorting == 'name_asc'
        is_name_desc = current_sorting == 'name_desc'
        is_category_asc = current_sorting == 'category__name_asc'
        is_category_desc = current_sorting == 'category__name_desc'

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        current_categories = Category.objects.filter(name__in=categories)

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse('products'))
        
        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': current_categories,
        'is_sorting_default': is_sorting_default,
        'is_price_asc': is_price_asc,
        'is_price_desc': is_price_desc,
        'is_name_asc': is_name_asc,
        'is_name_desc': is_name_desc,
        'is_category_asc': is_category_asc,
        'is_category_desc': is_category_desc,
        'border_class': 'info' if is_sorting_default else 'black',
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    """
    A view to show individual product details
    """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def add_product(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Edit a product in the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """ Delete a product from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))