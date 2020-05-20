from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from blog import views
from cooks import views
from Pizza_site import views as about
from pizza_products import views
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from django.contrib.auth import views as authViews

schema_view = get_swagger_view(title='Pastebin API')
urlpatterns = [
        path('ckeditor/', include('ckeditor_uploader.urls')),
        path('admin/', admin.site.urls),
        path('cart/', include('cart.urls')),
        path('orders/', include('orders.urls')),
        path('', include('pizza_products.urls')),
        path('', include('users.urls', namespace='accounts')),
        path('blog/', include('blog.urls')),
        path('about/',about.about_page, name='about'),
        path('cooks/', include('cooks.urls')),
        path('Topcooks/', include('cookTop.urls')),
        path('authentication/', authViews.LoginView.as_view(template_name='users/authentication.html'), name='auth'),
        path('exit/', authViews.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
        path('pass-reset/', authViews.PasswordResetView.as_view(template_name='users/pass_reset.html'), name='pass-reset'),
        path('password_reset_confirm/<uidb64>/<token>/',
            authViews.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
            name='password_reset_confirm'),
        path('password_reset_done/',
            authViews.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
            name='password_reset_done'),
        path('password_reset_complete/',
            authViews.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
            name='password_reset_complete'),
      ] \
          + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
          + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
