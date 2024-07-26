<div align="center">
   <h1> MiniAiLive ID Document Liveness Detection Windows SDK </h1>
   <img src=https://miniai.live/wp-content/uploads/2024/02/logo_name-1-768x426-1.png alt="MiniAiLive Logo"
   width="300">
</div>

## Welcome to the [MiniAiLive](https://www.miniai.live/)!
Welcome to the ID Document Liveness Detection SDK! MiniAiLive's Complete Document Liveness Detection Solution for Digital Onboarding here!
With 70% of fraud in digital onboarding and KYC happening with document fraud—or document presentation attacks—identity verification is a critical line of defense against the financial and reputational damage of document fraud. That’s where document liveness detection software comes in. It detects when an identity document is not genuine but instead a document presentation attack.
With our product suite, you can address the three most common presentation attacks universally across all the common types of identity documents anywhere in the world without needing to train on document templates.
Try it out today!

> **Note**
> - Our SDK is fully on-premise, processing all happens on hosting server and no data leaves server.

## Table of Contents

- [Installation Guide](#installation-guide)
- [API Details](#api-details)
- [Gradio Demo](#gradio-demo)
- [Python Test API Example](#python-test-api-example)

## Installation Guide

### Prerequisites

- Python 3.6+
- Windows
- CPU: 2cores or more
- RAM: 4GB or more

### Installation Steps

1. **Download the ID Document Liveness Detection Windows Server Installer:**

   Download the Server installer for your operating system from the following link:
   
   [Download the On-premise Server Installer](https://drive.google.com/file/d/1FTtd5Ylpiy8iNgDnEbxtcg6GAJiVxWUi/view?usp=sharing)

2. **Install the On-premise Server:**

   Run the installer and follow the on-screen instructions to complete the installation.
   <div align="center">
      <img src=https://github.com/user-attachments/assets/f50289a4-94de-49e2-b6a7-699f5e8f41d7 alt="install">
   </div>

3. **Request License and Update:**

   Run MIRequest.exe file to generate a license request file. You can find it here.
   
   > CC:\Users\Dev-1\AppData\Local\MiniAiLive\MiniAiLive-IDLiveness-WinServer

   Open it, generate a license request file, and send it to us via email or WhatsApp. We will send the license based on your Unique Request file, then you can upload the license file to allow to use. Refer the below images.
   <div align="center">
      <img src="https://github.com/user-attachments/assets/bb44d95c-8627-459a-9030-a5ea853b2112" width="300" />
      <img src="https://github.com/user-attachments/assets/f7d56833-cf2a-4199-895a-73df30062cbc" width="300" />
      <img src="https://github.com/user-attachments/assets/1fe95038-79e6-4bf7-b0c9-5002e6b540e9" width="300" />
      <img src="https://github.com/user-attachments/assets/d0cd7fb6-670e-42b6-8dcf-e32015b96b12" width="300" />
   </div>

4. **Verify Installation:**

   After installation, verify that the On-premise Server is correctly installed by checking the task manager:
   <div align="center">
      <img src="https://github.com/user-attachments/assets/2a0dea15-8c8b-4fd1-9de2-3be6fec2fc1a" width="300" />
   </div>

## API Details

### Endpoint

- `POST http://127.0.0.1:8093/api/check_id_liveness` ID Document Liveness Detection API
- `POST http://127.0.0.1:8093/api/check_id_liveness_base64` ID Document Liveness Detection API
  
### Request

- **URL:** `http://127.0.0.1:8093/api/check_id_liveness`
- **Method:** `POST`
- **Form Data:**
  - `image`: The image file (PNG, JPG, etc.) to be analyzed. This should be provided as a file upload.
<img width="1049" alt="Screenshot 2024-07-16 at 5 12 01 AM" src="https://github.com/user-attachments/assets/d8c35a5a-3556-4975-b457-a3e601a7d730">

- **URL:** `http://127.0.0.1:8093/api/check_id_liveness_base64`
- **Method:** `POST`
- **Raw Data:**
  - `JSON Format`:
    {
       "image": "--base64 image data here--"
    }
<img width="1049" alt="Screenshot 2024-07-16 at 5 11 34 AM" src="https://github.com/user-attachments/assets/6621a288-6bcf-4703-bba2-60c35c05fe84">

### Response

The API returns a JSON object with the ID document liveness detection details. Here is an example response:
   <div align="center">
      <img src="https://github.com/user-attachments/assets/e1c03a1b-d29a-495c-891a-26cc48a0a481" />
   </div>

## Gradio Demo

We have included a Gradio demo to showcase the capabilities of our ID Document Liveness Detection SDK. Gradio is a Python library that allows you to quickly create user interfaces for machine learning models.

### How to Run the Gradio Demo

1. **Install Gradio:**

   First, you need to install Gradio. You can do this using pip:

   ```sh
   git clone https://github.com/MiniAiLive/ID-Document-LivenessDetection-Windows-SDK.git
   pip install -r requirement.txt
   cd gradio
   ```
2. **Run Gradio Demo:**
   ```sh
   python app.py
   ```
## Python Test API Example

To help you get started with using the API, here is a comprehensive example of how to interact with the ID Document Liveness Detection API using Python. You can use API with another language you want to use like C++, C#, Ruby, Java, Javascript, and more

### Prerequisites

- Python 3.6+
- `requests` library (you can install it using `pip install requests`)

### Example Script

This example demonstrates how to send an image file to the API endpoint and process the response.

```python
import requests

# URL of the web API endpoint
url = 'http://127.0.0.1:8093/api/check_id_liveness'

# Path to the image file you want to send
image_path = './test_image.jpg'

# Read the image file and send it as form data
files = {'image': open(image_path, 'rb')}

try:
    # Send POST request
    response = requests.post(url, files=files)

    # Check if the request was successful
    if response.status_code == 200:
        print('Request was successful!')
        # Parse the JSON response
        response_data = response.json()
        print('Response Data:', response_data)
    else:
        print('Request failed with status code:', response.status_code)
        print('Response content:', response.text)

except requests.exceptions.RequestException as e:
    print('An error occurred:', e)
```

## Request license
Feel free to [Contact US](https://www.miniai.live/contact/)  to get a trial License. We are 24/7 online on WhatsApp: [+19162702374](https://wa.me/+19162702374).

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:
```java 
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the original repository.
```
## Try Online Demo
Please visit our ID API Web Demo here. https://demo.miniai.live
<a href="https://demo.miniai.live" target="_blank">
  <img alt="" src="https://github.com/MiniAiLive/ID-DocumentRecognition-Windows-SDK/assets/127708602/15de62ae-1d5a-408f-9805-60e935da40b4">
</a>

## Related Product
No | Project | Feature
---|---|---|
1 | [FaceRecognition-LivenessDetection-Android-SDK](https://github.com/MiniAiLive/FaceRecognition-LivenessDetection) | Face Matching, 3D Face Passive Liveness
2 | [FaceRecognition-LivenessDetection-Windows-SDK](https://github.com/MiniAiLive/FaceRecognition-LivenessDetection-Windows-SDK) | Face Matching, 3D Face Passive Liveness
3 | [FaceLivenessDetection-Android-SDK](https://github.com/MiniAiLive/FaceLivenessDetection-Android-SDK) | 3D Face Passive Liveness
4 | [FaceLivenessDetection-Linux-SDK](https://github.com/MiniAiLive/FaceLivenessDetection-Linux-SDK) | 3D Face Passive Liveness
5 | [FaceLivenessDetection-Windows-SDK](https://github.com/MiniAiLive/FaceLivenessDetection-Windows-SDK) | 3D Face Passive Liveness
6 | [FaceMatching-Android-SDK](https://github.com/MiniAiLive/FaceMatching-Android-SDK) | 1:1 Face Matching
7 | [FaceMatching-Windows-Demo](https://github.com/MiniAiLive/FaceMatching-Windows-Demo) | 1:1 Face Matching
8 | [FaceAttributes-Android-SDK](https://github.com/MiniAiLive/FaceAttributes-Android-SDK) | Face Attributes
9 | [ID-Document-Recognition-Android-SDK](https://github.com/MiniAiLive/ID-Document-Recognition-Android-SDK) | ID Document, Credit, MRZ Recognition
10 | [ID-Document-Recognition-Linux-SDK](https://github.com/MiniAiLive/ID-Document-Recognition-Linux-SDK) | ID Document, Credit, MRZ Recognition
11 | [ID-Document-Recognition-Windows-SDK](https://github.com/MiniAiLive/ID-Document-Recognition-Windows-SDK) | ID Document, Credit, MRZ Recognition
12 | [ID-Document-LivenessDetection-Linux-SDK](https://github.com/MiniAiLive/ID-Document-LivenessDetection-Linux-SDK) | ID Document Liveness Detection
13 | [ID-Document-LivenessDetection-Windows-SDK](https://github.com/MiniAiLive/ID-Document-LivenessDetection-Windows-SDK) | ID Document Liveness Detection

## About MiniAiLive
[MiniAiLive](https://www.miniai.live/) is a leading AI solutions company specializing in computer vision and machine learning technologies. We provide cutting-edge solutions for various industries, leveraging the power of AI to drive innovation and efficiency.

## Contact US
For any inquiries or questions, please [Contact US](https://www.miniai.live/contact/)

<p align="center">
<a target="_blank" href="https://t.me/Contact_MiniAiLive"><img src="https://img.shields.io/badge/telegram-@MiniAiLive-blue.svg?logo=telegram" alt="www.miniai.live"></a>&emsp;
<a target="_blank" href="https://wa.me/+19162702374"><img src="https://img.shields.io/badge/whatsapp-MiniAiLive-blue.svg?logo=whatsapp" alt="www.miniai.live"></a>&emsp;
<a target="_blank" href="https://join.skype.com/invite/ltQEVDmVddTe"><img src="https://img.shields.io/badge/skype-MiniAiLive-blue.svg?logo=skype" alt="www.miniai.live"></a>&emsp;
</p>
