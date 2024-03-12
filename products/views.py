from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category  # Correct import for your models

# Your view functions follow here...




def all_products(request):
    """
    A view to show all products, including sorting and search queries.
    """
    products = Product.objects.all()
    current_categories = Category.objects.all()
    query = None
    categories = None
    sort = None
    direction = "asc"

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            elif sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
            sortkey = f'-{sortkey}' if direction == 'desc' else sortkey
            products = products.order_by(sortkey)

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

    current_sorting = f'{sort}_{direction}' if sort and direction else 'None_None'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': current_categories,
        'current_sorting': current_sorting,
        'is_sorting_default': current_sorting == 'None_None',
        'is_price_asc': current_sorting == 'price_asc',
        'is_price_desc': current_sorting == 'price_desc',
        'is_name_asc': current_sorting == 'name_asc',
        'is_name_desc': current_sorting == 'name_desc',
        'is_category_asc': current_sorting == 'category_asc',
        'is_category_desc': current_sorting == 'category_desc',
        'border_class': 'info' if current_sorting == 'None_None' else 'black',
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



