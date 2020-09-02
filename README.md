This is a project working on segmentation of diabetic retinopathy and bolld vessels from retinal images.

Features of diabetic retinopathy including Microaneurysms,Haemorrhages,Hard exudates and Soft exudates should be detected.

The main techniques used in the segmentation includes watershed, normalized cuts and meanshift.

Datasets of retinal image used in this project are IDRiD (Indian Diabetic Retinopathy Image Dataset) and DRIVE (Digital Retinal Images for Vessel Extraction). The datasets are separated into two parts: one for diabetic retinopathy (haemorrhages, microaneurysms, hard exudates and soft exudates) detection, and the other for blood vessel detection, both with multiple subsets of retinal images and ground truth images(label retinal images respectively accordig to diabetic retinopathy and blood vessels) provided. There are 27 sets for test and 54 sets for train in the diabetic retinopathy detection part, and 20 sets for test along with 40 sets for test in the blood vessel detection part.

Python 3.7 is used to implement the whole project. More specifically, pytorch for training algorithm, numpy for scientific computation, and opencv along with PIL for image processing. GPU in Google Colab for project running.

U-Net is processed with a fully convolutional network. It uses asymmetric U-shaped structure containing a compressed path and an extended path.
