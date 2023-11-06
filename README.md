# Super-Resolution GAN (SRGAN) Project
[日本語]

## Introduction
This project leverages a Super-Resolution Generative Adversarial Network (SRGAN) to enhance image quality, built upon innovative research. Through our web platform, users can upscale images with ease, powered by our Flask-driven interface and back-end services.

## Model Development

### Research Paper
The foundation of our SRGAN model is a respected research [paper](https://arxiv.org/pdf/1609.04802.pdf) that provided a novel approach to super-resolution.

### Training Data
We employed the "mirflickr" dataset for training, starting with 12,500 images and later incorporating an additional 12,500 images for comprehensive learning.

### Training Process
Training was executed over 9 epochs across 3 days initially, followed by a secondary phase using the expanded dataset, resulting in improved performance and a higher PSNR value.

### Results
The extended training with the enriched dataset culminated in a PSNR of **29.35**, a testament to the model's enhanced super-resolution capabilities.
Here is the notebook [repository](https://github.com/rakibulhaque9954/SRGAN-from-scratch/blob/7ec72b1dd694e2b90e24d6ec8ff885cf8eb35c22/SRGAN_from_scratch.ipynb).

## Website and API Interface Using Flask

### Flask for Hosting
We chose Flask to serve our web application due to its simplicity and efficiency. Flask's ability to handle multiple requests at scale makes it an ideal choice for hosting both the front-end and back-end components of our platform.

### Flask for API Calls
Flask also powers our RESTful API, which is responsible for handling the image uploads and processing API calls. This API interacts with our SRGAN model hosted on Google Cloud Platform (GCP) to perform the super-resolution tasks.

### Data Upload and Processing
Users can upload images through the web interface, which are then sent to the Flask API. The API efficiently manages these requests, forwarding the images to the SRGAN model for upscaling and then returning the high-resolution images to the users.

## Google Cloud Platform (GCP) Hosting
Our model is hosted on GCP, taking advantage of its robust and scalable compute resources to ensure reliable model inference.

## Results and Website Interface

### Website Screenshots
![Homepage Screenshot](https://github.com/rakibulhaque9954/SRGAN_GCP/blob/91bd6a11730ba5ff5a873a27582613c1fd318dfd/screenshots/Screenshot%202023-11-06%20at%2020.31.00.png)
*Here is the homepage where users start their image upscaling journey.*

![Results Screenshot](https://github.com/rakibulhaque9954/SRGAN_GCP/blob/8745d1152bd58bc613e2a90a798e28e74a07cc66/screenshots/Screenshot%202023-11-06%20at%2020.30.46.png)
*The results page displays the original versus the super-resolved images, clearly demonstrating the model's capabilities.*

## Future Work
We are continually seeking to refine and improve our model. Plans for further training and optimization are in the pipeline to enhance the quality of results even further. The Model is still young and needs a lot of polishing.

## Usage
Its pretty simple upload an image with size presumably of 64 x 64 pixels and the model will enchance the image and scale it to 256 x 256 pixels. 

## Contributing
We welcome contributions from the community. Whether it's feature enhancements, bug fixes, or improvements to the code, we value your input.

## License
This project is made available under the [MIT License](https://github.com/rakibulhaque9954/blog_remastered/blob/a5e57fac46833fdcb26c28980d8f6b07980b0379/MIT_LICENSE_Rakibul_Haque.txt).
