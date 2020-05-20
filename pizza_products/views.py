from django.shortcuts import render,get_object_or_404, redirect
from pizza_products.models import PizzaProduct, pizza_comment
from cart.forms import CartAddProductForm
from pizza_products.forms import Pizza_commentForm
from django.views.generic import View
from django.contrib.auth.models import User
from users.models import Profile


def home(request):
    pizzas = PizzaProduct.objects.all()
    cart_product_form = CartAddProductForm()
    return render(request, 'pizzeria/home.html', locals())

def pizza_detail(request, pk):
    pizza = get_object_or_404(PizzaProduct, pk=pk)
    form = Pizza_commentForm()
    return render(request, 'pizzeria/new_comment.html', {'object': pizza, 'form':form})

def add_comment(request, pk):
    if request.POST:
        form = Pizza_commentForm(request.POST)
        pizza = PizzaProduct.objects.get(pk=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.pizza = pizza
            form.user = request.user
            form.save()
    return redirect(pizza.get_absolute_url())
