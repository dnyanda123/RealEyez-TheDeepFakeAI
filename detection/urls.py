from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import api_data

urlpatterns = [
    path("", views.home, name="home"),
    path('api/data/', api_data, name='api_data'),
    path("pricing/", views.pricing, name="pricing"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("upload/", views.upload, name="upload"),
    path("login/", views.user_login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_user, name="logout"),
    path("payment/", views.payment, name="payment"),
    path("thankyou/", views.thankyou, name="thankyou"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
