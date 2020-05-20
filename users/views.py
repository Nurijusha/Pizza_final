from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from orders.models import Order, ItemInOrder
from users.models import Profile
from .forms import UserRegisterForm, ProfileImage, UserUpdateForm
from django.contrib import messages
from blog.models import News
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт {username} создан')
            return redirect('auth')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def account(request, user_id):
    user = request.user
    my_orders = Order.objects.filter(user=user)
    orders_info = Order.objects.all()
    order_items = ItemInOrder.objects.all()
    return render(request, "users/account.html",
                  {"my_orders": my_orders, "order_items": order_items, "orders_info": orders_info})
@login_required
def profile(request):
    user = request.user
    posts = News.objects.filter(author=user)
    profile = Profile.objects.get(user=user)
    friends = profile.friends.all()
    count_of_visits = 0
    count_of_comments = 0
    for post in posts:
        count_of_visits += post.count
        count_of_comments += post.review.count()
    context = {
        'posts': posts,
        'count_of_posts': len(posts),
        'count_of_visits': count_of_visits,
        'count_of_comments': count_of_comments,
        'friends': friends,
        'subscribers': user.friend.all().count()
    }

    return render(request, 'users/profile.html', context)


@login_required
def change(request):
    if request.method == "POST":
        img_profile = ProfileImage(request.POST, request.FILES, instance=request.user.profile)
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if img_profile.is_valid() and update_user.is_valid():
            img_profile.save()
            update_user.save()
            messages.success(request, 'Ваш аккаунт успешно обновлен!')
            return redirect('accounts:profile')
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {
        'img_profile': img_profile,
        'update_user': update_user,
    }

    return render(request, 'users/profile_change.html', data)

@login_required
def favourite_list(request):
    user = request.user
    favourite_list = user.favourite.all().order_by('-date')
    return render(request, 'users/favourite_list.html', {'favourite_list': favourite_list})
