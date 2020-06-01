## Ear Disease Detection

# Introduction

Otitis Media (OM) is an infection of the middle ear. It is one of the most common childhood illnesses and the second most important reason leading to the loss of hearing. It is most common in developing countries and was ranked fifth on the global burden of disease and affected 1.23 billion people in 2013.


A classiffcation model is trained using Deep Learning, we tried several deep learning model architectures such as AlexNet, VGG16, InceptionV3 and Resnet-50. Best performance is achieved by ResNet-50 with pre-trained weights of imagenet dataset, this model is deployed on a website for anyone to test. 

## Dataset Description

We obtained the ear disease dataset from an ENT doctor from AIMS. The dataset consists on 120 images with 7 classes. Details of the classes: 

![alt text](images/Dataset_Description.png?raw=true)



## Deployment

We have developed a webapp using Flask API and have deployed it on Heroku that enables us to operate entirely on cloud.
We have developed a front-end for the website which could be accessed by [clicking here!](https://otology.netlify.com)
