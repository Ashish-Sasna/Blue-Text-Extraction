# Text Extraction Using OCR

## Project Overview
This project demonstrates how to perform text extraction from images using Optical Character Recognition (OCR) with a PyTorch-based model from Hugging Face. The goal is to accurately detect and extract blue colour text from images, even in challenging scenarios with varying background colors and text layouts.

## Prerequisites
- Python 3.x
- Required Python libraries:
  - 'torch'
  - 'transformers'
  - 'PIL' (from 'pillow')
  - 'opencv-python'
  - 'numpy'
  - 'Levenshtein' (for evaluating text accuracy)

You can install the required libraries using:
pip install torch transformers pillow opencv-python numpy python-Levenshtein

## Procedure
For text from pdf/doc file image
   Blue Text filtering - 
	1. Convert the BGR(as read by OpenCv)image into HSV image
	2. Define a blue colour range in HSV handling all shades of blue
	3. Create a mask of that range to capture the required colours
	4. Apply the mask on the image using bitwise and operation
For hand written text from image
   Blue Text filtering - 
	1. Convert the BGR(as read by OpenCv)image into HSV image
	2. Check the background of the image by checking the 'V' value of HSV. If 'V' < 200 then shaded background
	3. Split the original image into B, G, R
	3. Apply histogram equalization on Blue channel of the original image and merge it with other channels
	4. Convert the equalized image into HSV image
	5. Apply Gaussian blur to the image for smoothing
	6. Define a blue colour range in HSV handling all shades of blue
	7. Create a mask of that range to capture the required colours
	8. Apply the mask on the image using bitwise and operation


Text Extraction -
	1. Use an OCR pre-trained model for text extraction from image - HuggingFace model: 'ucaslcl/GOT-OCR2_0' 
	2. Extract the text
	3. Calculate the Leveshtein distance and word error rate between the original(blue colour only) and the extracted text
	4. Lower value of the both show high accuracy

## Results
For text from pdf/doc file image - 
   Leveshtein distance = 16
   Word Error Rate = 0.18

For hand written text from image - 
   Leveshtein distance = 5
   Word Error Rate = 1   

This process works well on white background images and text from pdf/ doc file. However with additional processing on the image and different model, it can be extended to different kinds of images.