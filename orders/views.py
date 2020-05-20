from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ItemInOrder
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                ItemInOrder.objects.create(order=order,
                                           product=item['product'],
                                           price=item['price'],
                                           quantity=item['quantity'],
                                           )
            cart.clear()
            order_created(order.id)

            return render(request, 'orders/order/created.html',
                          {'order': order})
    else:
        form = OrderCreateForm
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
