# Final_Project
## NLP: Sentiment Analysis on Healthcare Reviews

# Objective:
The goal of this project is to develop a model that can classify sentiments in healthcare reviews. This involves analyzing text data from healthcare reviews and determining whether the sentiment expressed in each review is good, bad, or neutral.

# Steps Included
1. # Data Preprocessing:
This task involves cleaning and preparing the text data from healthcare reviews. It includes tasks like text tokenization, removing stopwords, and handling any missing data.Data set contained 100 null values in review_text column which I have handled using mode operation.

2. # Sentiment Analysis Model:
Develop a machine learning or natural language processing (NLP) model that can classify sentiments in healthcare reviews. This model should be able to categorize reviews as positive, negative, or neutral based on the text content.

3. # Model Evaluation:
Accessed the performance of the sentiment analysis model using appropriate evaluation metrics. This step is crucial to ensure the model's accuracy and effectiveness.
Models used are logisticRegression,Naivebayes,Random Forest,SupportVector in which the highest score is obtain by using logisctic regression which is 54%

   precision    recall  f1-score   support

           0       0.42      0.33      0.37        80
           1       0.61      0.70      0.65       120

    accuracy                           0.55       200
   macro avg       0.51      0.51      0.51       200
weighted avg       0.53      0.55      0.54       200

4. # Insights & Visualization:
After building and evaluating the model, generated insights from the sentiment analysis results using bar chart.

# Analysis
The data provided is very small and also contain dulicated data due to which the model performance is not at all good.Since it is healthcare reviews threfore does not manipulated data.  

# Email Id: apkhare29@gmail.com
# LinkedIn : www.linkedin.com/in/apoorva-khare-7548642a6
