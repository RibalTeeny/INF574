# Sign Language Translator

## Project Overview

This project is centered on developing a tool for translating sign language into the alphabet, specifically designed to facilitate communication for individuals with disabilities. The project explores two different methodologies: feature detection and neural network-based image classification.

### Idea & Motivation
- **Primary Goal**: Enable disabled people to communicate effectively using sign language by translating it into the alphabet.

## Methods and Implementation

### Method 1: Feature Detection
- **Process**:
  - Hand contours are extracted from images.
  - Scale Invariant Feature Transform (SIFT) is used for feature detection within a focused rectangle derived from hand contours.
  - A feature matcher is run against images representing each letter, filtering out matches with low confidence.
  - Distances are computed between the coordinates of the test image and those of the alphabet images, with normalized coordinates for accuracy.
  - The image with the smallest distance is identified as the best match.

### Method 2: Neural Network
- **Process**:
  - A pretrained model (Mediapipe) is used to recognize hand patterns.
  - Photos (approximately 100 for each letter) are captured, and the coordinates of 21 points are extracted from each photo.
  - The data is manipulated and then fed into a 3-layer neural network for training.

## Results and Conclusion
- **Feature Detection**: This approach did not yield satisfactory results. The distance measure used was not effective in accurately matching images.
- **Neural Network**: Demonstrated more promising results than the first method. The project could have achieved better accuracy with a larger dataset. This method was more effective in recognizing and translating sign language.
