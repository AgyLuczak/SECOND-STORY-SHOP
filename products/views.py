from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from django.db.models import Exists, OuterRef
from django.db.models import Value, BooleanField


from .models import Product, Category  # Correct import for your models
from wishlist.models import WishlistItem 
from .forms import ProductForm

def all_products(request):
    products = Product.objects.all()
    current_categories = Category.objects.all()
    query = None
    categories = None
    sortkey = request.GET.get('sort', None)
    direction = request.GET.get('direction', 'asc')

    # Initialize all sorting flags at the beginning
    is_sorting_default = True
    is_price_asc = is_price_desc = is_name_asc = is_name_desc = is_category_asc = is_category_desc = is_size_asc = is_size_desc = False

    if request.user.is_authenticated:
        wishlist_products = WishlistItem.objects.filter(user=request.user, product=OuterRef('pk'))
        products = products.annotate(in_wishlist=Exists(wishlist_products))
    else:
        products = products.annotate(in_wishlist=Value(False, output_field=BooleanField()))

    if sortkey and direction:
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))
        elif sortkey == 'category':
            sortkey = 'category__name'
        elif sortkey == 'size':  # Ensure this condition is handled
            if direction == 'desc':
                sortkey = '-size'
                is_size_desc = True
            else:
                sortkey = 'size'
                is_size_asc = True

        if direction == 'desc' and sortkey != '-size':
            sortkey = f'-{sortkey}'
        products = products.order_by(sortkey)

        # Update flags based on current_sorting
        is_sorting_default = False
        is_price_asc = sortkey == 'price' and direction == 'asc'
        is_price_desc = sortkey == '-price'
        is_name_asc = sortkey == 'lower_name' and direction == 'asc'
        is_name_desc = sortkey == '-lower_name'
        is_category_asc = sortkey == 'category__name' and direction == 'asc'
        is_category_desc = sortkey == '-category__name'
        is_size_asc = sortkey == 'size' and direction == 'asc'
        is_size_desc = sortkey == '-size'

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
        'is_size_asc': is_size_asc,
        'is_size_desc': is_size_desc,
        'border_class': 'info' if is_sorting_default else 'black',
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        product.in_wishlist = WishlistItem.objects.filter(user=request.user, product=product).exists()
    else:
        product.in_wishlist = False

    context = {
        'product': product,
    }
 
    request.session.pop('wishlist_action', None)
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


