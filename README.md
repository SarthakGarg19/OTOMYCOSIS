# Ear Disease Detection

## Introduction

Otitis Media (OM) is an infection of the middle ear. It is one of the most common childhood illnesses and the second most important reason leading to the loss of hearing. It is most common in developing countries and was ranked fifth on the global burden of disease and affected 1.23 billion people in 2013.

OM is often misdiagnosed or not diagnosed at all, especially when it is in the early stages. It is often either under-diagnosed or over-diagnosed depending on the factors like clinicians, symptoms, otoscopes etc. Detection of OM requires a good medical practitioner (ENT), whose availability is difficult in remote village areas especially in developing countries. That is why OM is ignored amongst these kinds of groups and is a second major cause of hearing loss.

The aim of the study is to develop a diagnostic system using Ear Drum (Tympanic Membrane) images and applying machine learning to automatically extract certain features and perform image classification which can help diagnose otitis media(OM) with greater accuracy.
This diagnostic system will provide a reliable data to a survey volunteer to advise the patient or his family to visit an ENT or take professional help if OM is present.


<img src="https://3.bp.blogspot.com/-WBPelBryAoE/WrJhXwz5XtI/AAAAAAAAEPA/iMSU4TXcNWIe7jK2G3P6xo4Ls4DWisbTgCLcBGAs/s1600/wix%2B11.jpg" width="400">


## Dataset Description

One of the biggest challenge faced during the project was the collection of image data for normal and infected tympanic membrane. We obtained the ear disease dataset from an ENT doctor  AIMS. The dataset consists on 120 images with 7 classes. Details of the classes: 

![alt text](images/Dataset_Description.png?raw=true)

## Building a CNN

Now we are ready to build a CNN. After dabbling a bit with tensorflow, I decided it was way too much work for something incredibly simple. I decided to use keras. Keras is a high-level API wrapper around tensorflow. It made coding lot more palatable. The approach I used was similar to this. I used a 3 convolutional layers in my architecture initially.

![alt text](images/cnn.png?raw=true)


## Deployment

We have developed a webapp using Flask API and have deployed it on Heroku that enables us to operate entirely on cloud.
A front-end for the website has been deployed on Netlify which could be accessed by [clicking here!](https://otology.netlify.com)


