# Guess-the-image

> This application is a simple image classification tool built with React, Flask, and TensorFlow. It allows users to upload images,
  which are then sent to the server for processing using a pre-trained TensorFlow model. The app classifies uploaded images into predefined
  categories and provides results to the user. Users can explore the world of image classification and gain insights into the underlying
  machine learning techniques.

## Key Features

  * User-friendly interface for image uploads.  
  * Server-side image processing using TensorFlow.
  * Pre-trained model for image classification.
  * Easily extendable for custom models and categories.

## Note

  * Dataset Trained on [CIFAR-10 dataset][dataset]
  * Trained on 8000 images
  * Tested on 4000 images
  * Accuracy : 68%
  
## Tech Stack

  * Frontend: React and axios
  * Backend: Python and Flask Framework
  * Libraries: numpy, matplotlib, opencv-python, tensorflow
    
## Dependencies

- **Operating System:** Windows / Linux / macOS
- **Recommended RAM:** 8GB or higher

## Software Dependencies

- React.js (for the frontend)
- Python 3 (for the backend)
- npm (Node Package Manager)
- pip (Python package manager)


## Setup

### Client-side (Frontend)

   ```bash
   $ cd frontend
   $ npm install
   $ npm start
  ```

### Server-side (Backend)

   ```bash
   $ cd backend
   $ pip install -r requirements.txt
   $ python3 application.py
   ``` 

## Tools

  * Visual Studio Code
  * Postman
  * Git

## Acknowledgments

  * [Youtube][youtube]
  * [React][react]
  * [Flask][flask]

[dataset]:https://www.cs.toronto.edu/~kriz/cifar.html
[youtube]:https://www.youtube.com/watch?v=t0EzVCvQjGE&t=1s
[react]:https://legacy.reactjs.org/docs/getting-started.html
[flask]:https://www.tutorialspoint.com/flask/index.htm
