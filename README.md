## Ear Disease Detection

# Introduction

Otitis Media (OM) is an infection of the middle ear. It is one of the most common childhood illnesses and the second most important reason leading to the loss of hearing. It is most common in developing countries and was ranked fifth on the global burden of disease and affected 1.23 billion people in 2013.


<img src="https://3.bp.blogspot.com/-WBPelBryAoE/WrJhXwz5XtI/AAAAAAAAEPA/iMSU4TXcNWIe7jK2G3P6xo4Ls4DWisbTgCLcBGAs/s1600/wix%2B11.jpg" width="48">


## Dataset Description

We obtained the ear disease dataset from an ENT doctor from AIMS. The dataset consists on 120 images with 7 classes. Details of the classes: 


![alt text](images/Dataset_Description.png?raw=true)

## Building a CNN

Now we are ready to build a CNN. After dabbling a bit with tensorflow, I decided it was way too much work for something incredibly simple. I decided to use keras. Keras is a high-level API wrapper around tensorflow. It made coding lot more palatable. The approach I used was similar to this. I used a 3 convolutional layers in my architecture initially.

![alt text](images/cnn.png?raw=true)

Figure
5 : (a) general CNN b ) co nvolutional filter (c) pooling window



## Deployment

We have developed a webapp using Flask API and have deployed it on Heroku that enables us to operate entirely on cloud.
A front-end for the website has been deployed on Netlify which could be accessed by [clicking here!](https://otology.netlify.com)


