from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Exists, OuterRef, Value, BooleanField
from django.db.models.functions import Lower
from .models import Product, Category
from wishlist.models import WishlistItem
from .forms import ProductForm


def all_products(request):
    products = Product.objects.all()
    current_categories = Category.objects.all()
    query = None
    sortkey = request.GET.get("sort", None)
    direction = request.GET.get("direction", "asc")
    is_sorting_default = True

    if request.user.is_authenticated:
        wishlist_products = WishlistItem.objects.filter(
            user=request.user, product=OuterRef("pk")
        )
        products = products.annotate(in_wishlist=Exists(wishlist_products))
    else:
        products = products.annotate(
            in_wishlist=Value(False, output_field=BooleanField())
        )

    if sortkey:
        if sortkey == "name":
            sortkey = "lower_name"
            products = products.annotate(lower_name=Lower("name"))
        elif sortkey == "category":
            sortkey = "category__name"
        elif sortkey == "size":
            sortkey = f'{"-" if direction == "desc" else ""}size'

        products = products.order_by(
            f'{"-" if direction == "desc" and sortkey != "size" else ""}{sortkey}'
        )
        is_sorting_default = False

    if "category" in request.GET:
        categories = request.GET["category"].split(",")
        products = products.filter(category__name__in=categories)
        current_categories = Category.objects.filter(name__in=categories)

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
    product = get_object_or_404(Product, pk=product_id)
    if request.user.is_authenticated:
        product.in_wishlist = WishlistItem.objects.filter(
            user=request.user, product=product
        ).exists()
    else:
        product.in_wishlist = False
    return render(request, "products/product_detail.html", {"product": product})


@login_required
def add_product(request):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    if request.method == "POST":
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
        form = ProductForm()
    return render(request, "products/add_product.html", {"form": form})


@login_required
def edit_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Successfully updated product!")
        return redirect(reverse("product_detail", args=[product.id]))
    else:
        messages.info(request, f"You are editing {product.name}")
    return render(
        request, "products/edit_product.html", {"form": form, "product": product}
    )


@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))
