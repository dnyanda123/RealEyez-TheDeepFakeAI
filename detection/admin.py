from django.contrib import admin
from .models import Image  # Make sure to import your model

admin.site.register(Image)  # Register your model with the admin
