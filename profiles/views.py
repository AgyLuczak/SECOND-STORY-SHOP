from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile  # Import UserProfile from models
from .forms import UserProfileForm  # Import UserProfileForm from forms
from checkout.models import Order


@login_required
def profile(request):
    """Display the user's profile."""
    # Retrieve the UserProfile instance for the logged-in user, or return a 404 error if not found
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        # If the request method is POST, process the submitted form data
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            # Save the form if it's valid and show a success message
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            # Show an error message if the form is invalid
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        # For a GET request, display the form with the existing profile data
        form = UserProfileForm(instance=profile)

    # Retrieve all orders associated with the user's profile
    orders = profile.orders.all()

    # Render the profile page with the form and orders data
    template = "profiles/profile.html"
    context = {"form": form, "orders": orders, "on_profile_page": True}

    return render(request, template, context)


def order_history(request, order_number):
    """Display the past order confirmation for a specific order."""
    # Retrieve the Order instance by its order number, or return a 404 error if not found
    order = get_object_or_404(Order, order_number=order_number)

    # Show an info message indicating that this is a past order confirmation
    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    # Render the checkout success page with the order data, indicating it's from the profile page
    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
