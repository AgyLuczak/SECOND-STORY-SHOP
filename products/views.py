from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Exists, OuterRef, Value, BooleanField
from django.db.models.functions import Lower
from .models import Product, Category
from wishlist.models import WishlistItem
from .forms import ProductForm


def all_products(request):
    """ View to display all products """
    # Retrieve all products and categories from the database
    products = Product.objects.all()
    current_categories = Category.objects.all()
    query = None
    sortkey = request.GET.get("sort", "name")  # Sort key provided by the user
    direction = request.GET.get("direction", "asc")  # Sorting direction (asc or desc)
    is_sorting_default = True

    # Check if the user is authenticated
    if request.user.is_authenticated:
        # Annotate products with a Boolean flag indicating if they are in the wishlist
        wishlist_products = WishlistItem.objects.filter(
            user=request.user, product=OuterRef("pk")
        )
        products = products.annotate(in_wishlist=Exists(wishlist_products))
    else:
        # For unauthenticated users, set in_wishlist to False
        products = products.annotate(
            in_wishlist=Value(False, output_field=BooleanField())
        )

    # Apply sorting to the products based on the sort key and direction
   
    # Initialize the sort variable to None
    sort = None     
    # Initialize the sort variable to None
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
        if sortkey == 'name':
            sortkey = 'lower_name'
            products = products.annotate(lower_name=Lower('name'))
        elif sortkey == 'category':
            sortkey = 'category__name'
        elif sortkey == 'size':
            # Filter out products without sizes
            products = products.exclude(size__isnull=True)
        if 'direction' in request.GET: #solution found on chatGPT4
            direction = request.GET['direction']
            if direction == 'desc':
                sortkey = f'-{sortkey}'
        # Apply sorting
        if sortkey:
            products = products.order_by(sortkey)

    # Display only products with sizes if sorting by size
    if sort == 'size':
        products = products.filter(size__isnull=False)


   # Filter products by categories provided in the request
    if "category" in request.GET:
        categories = request.GET["category"].split(",")
        products = products.filter(category__name__in=categories)
        current_categories = Category.objects.filter(name__in=categories)

    # Search products based on the search term provided in the request
    if "q" in request.GET:
        query = request.GET["q"]
        if not query:
            messages.error(request, "You didn't enter any search criteria!")
            return redirect(reverse("products"))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    context = {
        "products": products,
        "search_term": query,
        "current_categories": current_categories,
        "is_sorting_default": is_sorting_default,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """ View to display details of a single product """
    # Retrieve the product by its ID, or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)

    # Check if the product is in the wishlist for authenticated users
    if request.user.is_authenticated:
        product.in_wishlist = WishlistItem.objects.filter(
            user=request.user, product=product
        ).exists()
    else:
        product.in_wishlist = False

    # Render the product detail page
    return render(request, "products/product_detail.html", {"product": product})


@login_required
def add_product(request):
    """ View to add a new product (superusers only) """
    # Only superusers can add a product
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        # If form is submitted, validate and save the new product
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        # Display an empty product form for adding a new product
        form = ProductForm()

    return render(request, "products/add_product.html", {"form": form})


@login_required
def edit_product(request, product_id):
    """ View to edit an existing product (superusers only) """
    # Only superusers can edit a product
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    # Retrieve the product by its ID, or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)

    # Initialize the form with the existing product instance
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)

    if request.method == "POST" and form.is_valid():
        # If form is submitted and valid, update the product
        form.save()
        messages.success(request, "Successfully updated product!")
        return redirect(reverse("product_detail", args=[product.id]))
    else:
        # Display a message indicating that the product is being edited
        messages.info(request, f"You are editing {product.name}")

    return render(
        request, "products/edit_product.html", {"form": form, "product": product}
    )


@login_required
def delete_product(request, product_id):
    """ View to delete a product (superusers only) """
    # Only superusers can delete a product
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    # Retrieve the product by its ID, or return a 404 error if not found
    product = get_object_or_404(Product, pk=product_id)

    # Delete the product and show a success message
    product.delete()
    messages.success(request, "Product deleted!")

    return redirect(reverse("products"))
