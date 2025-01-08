from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.mail import send_mail
from .forms import ImageUploadForm
from django.contrib import messages
from .models import Image  # Assuming the ImageSlider model exists
from django.contrib.auth import authenticate, login, logout
from tensorflow.keras.models import load_model  # type: ignore
from tensorflow.keras.applications.efficientnet import preprocess_input  # type: ignore
import numpy as np
from PIL import Image  # Correct import for handling images
import os

# Load model once during server startup
MODEL_PATH = os.path.join('detection', 'models', 'efficientnet_model.keras')
model = load_model(MODEL_PATH)

def predict_image(image):
    img = Image.open(image)
    img = img.resize((32, 32))  # Resize both width and height to 32x32
    img_array = np.array(img)
    
    # Ensure the image has 3 channels (RGB)
    if img_array.shape[-1] != 3:
        img_array = np.stack([img_array] * 3, axis=-1)  # Convert to 3 channels if it's grayscale

    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array = preprocess_input(img_array)  # Preprocess the image (for EfficientNet)

    # Make the prediction
    prediction = model.predict(img_array)

    if prediction >= 0.5:
        return "Real", prediction[0][0] * 100  # Confidence as percentage
    else:
        return "AI-Generated", (1 - prediction[0][0]) * 100


def upload(request):
    form = ImageUploadForm()  # Always initialize 'form' to avoid the error
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            image_file = request.FILES['image']
            image_path = os.path.join('media', image_file.name)

            # Ensure the directory exists
            if not os.path.exists('media'):
                os.makedirs('media')

            with open(image_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)

            # Preprocess the image and pass it to the model
            label, confidence = predict_image(image_path)

            result = f"{label} ({confidence:.2f}%)"
            relative_image_path = f"{settings.MEDIA_URL}{image_file.name}"
            return render(request, 'result.html', {
                'result': result,
                'image_path': relative_image_path  # Use relative path for the template
            })
        else:
            form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})

def home(request):
    return render(request, 'home.html')

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def api_data(request):
    data = {"message": "Hello from Django API!"}
    return Response(data)


def pricing(request):
    return render(request, "pricing.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    message_sent = False
    if request.method == 'POST':
        # Get data from the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Process the form (e.g., save to database, send an email)
        # For now, we'll just display a success message on the same page.

        message_sent = True  # Set the flag to display the success message
        messages.success(request, 'Thank you for your message. We will revert back to you as soon as possible.')

    return render(request, 'contact.html', {'message_sent': message_sent})

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        User.objects.create_user(username=username, password=password)
        return redirect("login")
    return render(request, "register.html")

@login_required
def test_here_view(request):
    # Your logic for the "Test Here" page
    return render(request, 'upload.html')

def logout_user(request):
    logout(request)
    return redirect("home")

def payment(request):
    return render(request, "payment.html")

def thankyou(request):
    return render(request, "thankyou.html")