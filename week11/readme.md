# Introduction to Neural Networks

In this week's lab, we are to revise the structure and parameters of artificial neural networks and see how they can be implemented in Python.

## Goals

* Apprehend the inner workings of a neural network in an intuitive fashion
* Learn how to implement neural networks for prediction tasks in Python

## Lab Structure

1. Questions about last week's lab?
2. Questions about the project?
3. Walkthrough: playing on the Playground
4. Group exercise: solve a problem on the Playground (10 minutes)
5. Walkthrough: regression and classification in PyTorch
6. Group exercise: build a neural network in PyTorch

In case we finish the lab earlier, students can use the remaining time to work on their project.

## Walkthroughs

The first part of the lab will be done on TensorFlow's **[Playground](https://playground.tensorflow.org)**. We will look at the various components and parameters of neural networks and witness how changing them can improve or decrease the quality of a model.

* Input, hidden, and output layers
* Epochs
* Batch size
* Learning rate
* Activation functions
* Regularization

For the second part, we will use the two notebooks found in this folder (regression and classification).

## Exercises

### A neural network for the "spiral" dataset

On the Playground, under classification problems, you will find a dataset where the data points form a spiral. Try to adjust the parameters of the neural network in order to predict the classes with minimal loss.

### Building a regression model in Pytorch

In this exrecise you will build a regression model with 3 hidden layers in pytorch and compare it with a single layer network. Also you will be able to compare Adam optimizer with SGD.

