
# OpenCV Image Processing Journey

Welcome to my OpenCV Image Processing repository! This repository documents my learning progress in OpenCV, an open-source computer vision and machine learning software library. I will continuously update this README with the new concepts and techniques I learn.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Topics Covered](#topics-covered)
  - [Reading Images and Videos](#reading-images-and-videos)
  - [Rescaling Frames](#rescaling-frames)
  - [Drawing Shapes](#drawing-shapes)
  - [Putting Text](#putting-text)
  - [Image Transformations](#image-transformations)
  - [Color Spaces](#color-spaces)
  - [Blurring Techniques](#blurring-techniques)
  - [Bitwise Operations](#bitwise-operations)
  - [Masking](#masking)
  - [Canny Edge Detection](#canny-edge-detection)
  - [Edge Detection](#edge-detection)
  - [Histograms](#histograms)

## Introduction

This repository is a log of my progress as I learn and experiment with OpenCV for image processing. The goal is to cover a wide range of topics and applications in computer vision.

## Getting Started

To get started with the code in this repository, you need to have Python and OpenCV installed. You can install OpenCV using pip:

```sh
pip3 install opencv-contrib-python
```

## Topics Covered

### Reading Images and Videos

- **Reading an Image**: Learn how to read and display images using OpenCV's `cv.imread()` and `cv.imshow()` functions.
- **Reading a Video**: Explore how to read and display video frames using `cv.VideoCapture()` and loop through each frame.

### Rescaling Frames

- **Rescaling**: Understand how to rescale images and videos to different sizes, typically for reducing computational load.

### Drawing Shapes

- **Rectangle, Circle, Line**: Discover how to draw various shapes like rectangles, circles, and lines on images using OpenCV's drawing functions.

### Putting Text

- **Adding Text**: Learn how to put text on images with customizable fonts, sizes, and colors.

### Image Transformations

- **Translation**: Shift images along the x and y axes.
- **Rotation**: Rotate images around a specified center point.
- **Flipping**: Flip images vertically, horizontally, or both.
- **Resizing**: Change the dimensions of images while maintaining aspect ratio.

### Color Spaces

- **BGR to RGB/Grayscale/HSV/LAB**: Convert images between different color spaces for various image processing tasks.

### Blurring Techniques

- **Averaging**: Apply simple averaging blur to smooth out images.
- **Gaussian Blur**: Use Gaussian blur for a more natural-looking smoothness.
- **Median Blur**: Effectively remove noise with median blur.
- **Bilateral Filtering**: Preserve edges while blurring using bilateral filtering.

### Bitwise Operations

- **Bitwise AND/OR/XOR/NOT**: Perform fundamental bitwise operations on images, often used for masking and combining image regions.

### Masking

- **Creating Masks**: Learn how to create and apply masks to images for focusing on specific regions.
- **Circular and Rectangular Masks**: Use geometric shapes to mask parts of an image.
- **Masked Images**: Apply masks to images using bitwise operations to highlight or hide parts of the image.

### Canny Edge Detection

- **Canny**: Apply the Canny edge detection method to identify edges in images.

### Edge Detection

- **Laplacian**: Apply the Laplacian method for edge detection.
- **Sobel**: Use the Sobel operator to detect edges in both x and y directions.
- **Combined Sobel**: Combine the results of Sobel X and Sobel Y for comprehensive edge detection.

### Histograms

- **Grayscale Histogram**: Construct and plot histograms for grayscale images.
- **Color Histogram**: Construct and plot histograms for color images (RGB).
- **Masked Histogram**: Create and plot histograms for specific regions of an image using masks.

For detailed code examples and implementations, please refer to the respective Python files in this repository.
