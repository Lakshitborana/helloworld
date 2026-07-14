# 1. What is machine learning?
# Machine learning (ML) is a branch of Artificial intelligence where computers learn patterns from data and make predictions or decisions without being explicitly programmed for every task.

# Example: 
# suppose you have data like:
# house size(sq ft)                  house price
#      1000                            30 lakh
#      1500                            45 lakh
#      2000                            60 lakh

# An ML model learns the relationship between house size and price.

# Now if you enter:
# House size = 1800 sq ft
# it predicts:
# house price = 54 lakh 
# The model learned from previous examples instead of someone writing an exact formula.

# 2. What is a Feature?
# A feature is an input variable used to make predictions.
# Think of it as the information you give to the model.

# Example: 
# predicting house price:
# * house size(Feature)
# * Number of Bedrooms(Feature)
# * Location(Feature)
# * Age of House(Feature)

# Feature = inputs(X)

# 3. What is a Label?
# A label is the correct answer or output that the model is trying to predict.

# Example:

# house size                    house price
#   1000                          30 lakh

# here,
# house size > Feature
# price > Label

# label = Output(y)

# 4. Difference Between traditional programming and machine learning

# Traditional programming                       Machine Learning 
# Programmer writes rules                       Model learns rules from data
# Data + Rules = Output                          Data + correct Answers > Model
# Good for fixed tasks                           Good for tasks with patterns and predictions
# Example: Calculator                            Example: spam email Detection

# Traditional Programming 
# rules + data = output
# Example:
# if marks >= 40:
#   print("Pass")
# you explicitly define the rule.

# Machine Learning 
# data + labels 
# Train model 
# prediction 

# Example:

# Instead of writing a rule to detect spam emails, you provide the model with a dataset of emails labeled as "spam" or "not spam". The model learns the patterns in the data and can then predict whether new emails are spam or not.

# 5. Name the 3 types of Machine Learning 

# 1. Supervised Learning
# the model learns using features and labels.

# example:
# house price prediction 
# student marks prediction 
# email spam detection 
# Data has answers.
# Input> Output

# 2. Unsupervised Learning
# the model only gets features and tries to find hidden patters or groups.
# Example:
# Customer segmentation 
# Grouping similar products 
# Fraud pattern discovery 
# Data has no labels.

# 3. Reinforcement Learning 
# the model learns by trial and error using rewards and penalties.
# Example:
# chess AI 
# Self driving cars
# Robot learning
# Game-playing AI

# the Agent takes actions:
# Good action > Reward
# Bad action > penalty
# over time , it learns the best strategy.

