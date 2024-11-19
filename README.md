# RealEyez-TheDeepFakeAI
RealEyez is a machine learning-based project designed to detect whether an image is real or AI-generated. This web application utilizes a Convolutional Neural Network (CNN) model based on EfficientNet to classify images. The project is built using Django for the web framework and integrates an AI model that analyzes images and predicts their authenticity.

## Project Video
Link: 

## Table of Content
- Features
- Dataset Used
- Technologies Used
- Setup and Installation
- Usage
- Model Description
- Contributing
- License
## Features
- Image Upload: Users can upload images to the web app for prediction.
- Real vs AI-Generated Classification: The model classifies the uploaded image as either 'Real' or 'AI-generated' with a percentage likelihood.
- EfficientNet Model: The AI model is built on EfficientNet for efficient and accurate predictions.
- User-friendly Interface: The web interface is intuitive and responsive, designed for seamless interaction with the model.

## Dataset Used
CIFAKE is a dataset that contains 60,000 synthetically-generated images and 60,000 real images (collected from CIFAR-10). The dataset contains two classes - REAL and FAKE. For REAL, we collected the images from Krizhevsky & Hinton's CIFAR-10 dataset For the FAKE images, we generated the equivalent of CIFAR-10 with Stable Diffusion version 1.4 There are 100,000 images for training (50k per class) and 20,000 for testing (10k per class).
(https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images)

## Technologies Used
- Django: Web framework for building the application.
- Python: Backend language.
- TensorFlow: Deep learning library used to implement the EfficientNet model.
- Keras: API for building and training neural networks, integrated with TensorFlow.
- Bootstrap: Frontend framework for responsive and modern design.
- HTML/CSS/JavaScript: Used for frontend development and interactivity.
- SQLite: Default database used by Django for storing minimal data.\
## Setup and Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/dnyanda123/RealEyez-TheDeepFakeAI
    cd RealEyez-TheDeepFakeAI
2. Set up a Virtual Environment
      ```bash
      python -m venv env
      source env/bin/activate  # On Windows: env\Scripts\activate
3. Install Dependencies:
      ```bash
      pip install -r requirements.txt
4. Run Migrations
      ```bash
      python manage.py migrate
5. Run the Django Development Server
      ```bash
      python manage.py runserver

## Usage
- Navigate to the Home page where you will see the "Upload Image" option.
- Upload an image you want to classify (either real or AI-generated).
- The model will predict whether the image is real or AI-generated, showing the result along with the likelihood percentage.

## Model Description
The model is based on EfficientNet, a highly efficient deep learning architecture for image classification tasks. The network uses a combination of depth, width, and resolution scaling to provide an efficient architecture. The model was trained on a large dataset of real and AI-generated images, achieving a high level of accuracy in classification.

## Training Details
- Model Architecture: EfficientNet (CNN)
- Framework: TensorFlow/Keras
- Input Size: 224x224 pixels
- Training Dataset: Custom dataset of real and AI-generated images
- Accuracy: The model achieves an accuracy of X% on the test dataset.

## Contributing
- Fork the repository.
- Create your feature branch (git checkout -b feature-branch).
- Commit your changes (git commit -m 'Add new feature').
- Push to the branch (git push origin feature-branch).
- Open a Pull Request to merge your changes into the main branch.

## Contact
For any questions or feedback, please reach out to:
 - Name: Dnyaneshwari Pramod Nemade
 - Email: dnyaneshwarinemade02@gmail.com

## License
This project is licensed under the MIT License - see the LICENSE file for details.
