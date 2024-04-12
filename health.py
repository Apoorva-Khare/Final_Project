#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pymongo
import seaborn as sns
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# READING THE CLEANED DATAFRAME
df = pd.read_csv('C:/Users/Dell/JupyterPythoncodes/FinalProject/cleaned_health_reviews.csv')


# Setting up page configuration
icon = Image.open("C:/Users/Dell/JupyterPythoncodes/FinalProject/sentiment.jpg")
st.set_page_config(page_title= "NLP Sentiment Analysis of Health Care Reviews | By Apoorva Khare",
                   page_icon= icon,
                   layout= "wide",
                   initial_sidebar_state= "expanded",
                   menu_items={'About': """# This dashboard app is created by *Apoorva Khare*!
                                      """}
                  )

st.title("NLP SENTIMENT ANALYSIS FOR HEALTH CARE REVIEWS ")
st.write("")

SELECT = option_menu(
    menu_title = None,
    options = ["Home", "Data Exploration", "Insights"],
    default_index=0,
    orientation="horizontal",
    styles={"container": {"padding": "0!important", "background-color": "white","size":"cover", "width": "100"},
        "icon": {"color": "black", "font-size": "20px"},

        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-selected": {"background-color": "#6F36AD"}})


if SELECT == "Home":
    st.header("Sentiment Analysis of Healthcare Reviews")
    
    st.markdown(":blue[**OBJECTIVE**]")
    st.write("***The goal of this project is to develop a model that can classify sentiments in healthcare reviews. This involves analyzing text data from healthcare reviews and determining whether the sentiment expressed in each review is positive, negative, or neutral.***")
    
    st.write(":blue[**TASK**]")
    
    st.write("***Data Preprocessing***")
    st.write("***Sentiment Analysis Model***")
    st.write("***Model Evaluation***")
    st.write("***Insights & Visualization***")

if SELECT == "Data Exploration":
    tab1, tab2,tab3= st.tabs(["**HEALTHCARE REVIEWS DATAFRAME**","**ACTUAL RATING CLASS AND ITS COUNTS**", "**RATINGS AND WORDCLOUD FOR GOOD AND BAD REVIEWS**"])
    
    with tab1:
        st.write(df)
    
        st.write(":violet[**Unique Reviews Count**]",df.clean_text.value_counts())
           
    with tab2:
               
        df1 = df.groupby(["rating_class"]).size().reset_index(name="counts")
        fig = px.bar(df1,
                    title='Actual Rating Class And its Counts',
                    x='rating_class',
                    y='counts',
                    color_discrete_sequence=px.colors.sequential.Oranges_r
        )
        
        st.plotly_chart(fig,use_container_width=True)
        
    with tab3:
        col1,col2= st.columns([2,2],gap="large")
        with col1:
        

            rating_class_list=[]

            for i in df['rating_class']:
                if i=='Bad':
                    rating_class_list.append(0)

                else:
                    rating_class_list.append(1)

            df['rating_class']=rating_class_list
            df1 = df.groupby(["rating_class"]).size().reset_index(name="counts")
            fig = px.bar(df1,
                        title='Total Ratings of Good(1) and Bad(0) Reviews',
                        x='rating_class',
                        y='counts',
                        color_discrete_sequence=px.colors.sequential.Emrld_r
            )

            st.plotly_chart(fig,use_container_width=True)

        with col2:
            Negative_Reviews = ' '.join(word for word in df['clean_text'][df['rating_class']==0].astype(str))
            Positive_Reviews = ' '.join(word for word in df['clean_text'][df['rating_class']==1].astype(str))
        
            topic = st.selectbox('Select Reviews Type',['WordCloud For Good_Reviews','WordCloud For Bad_Reviews'])       
            def create_wordcloud(topic):
                if topic == 'WordCloud For Good_Reviews':
                    topic = Positive_Reviews
                else:
                    #topic == 'WordCloud For Bad_Reviews':
                    topic = Negative_Reviews
                    

                wordcloud = WordCloud().generate(topic)
                return wordcloud

            wordcloud = create_wordcloud(topic)

            # Display the generated image:
            fig, ax = plt.subplots(figsize = (8, 8))
            ax.imshow(wordcloud)
            plt.axis("off")
            st.pyplot(fig)

if SELECT == "Insights":
    
    st.write("***As we can see that the number of unique reviews are only nine and ratings are also not according to the reviews as shown in the positive and negative word cloud.***")
    
    st.write("*** The number of Good Reviews is 602 after merging neutral and good reviews and the number of Bad Reviews is 398.***")
    
    st.write(":blue[Total 9 reviews text are used with different ratings] ")
    
    st.write("*****GOOD REVIEWS***** ---provider excellent,satisfied service,staff care,highly recommend,experience healthcare")
    
    st.write("****BAD REIEWS****--- bad experience,disappointing service,provider avoid,experience terrible.")
    
    st.write("***MAXIMUM REVIEWS ARE LIKE ---mixed feeling, neither good nor bad-- where rating is given 3,4,5 for the same reviewtext.***")
    
    st.write("***Even after the data preprocessing the Machine Learning Models are not able to get good score.***")
    
    st.write("***Logistic Regression Model scored 0.54 score averge f1 score.***")
    
    st.write("")
    st.write("")
    
    st.write("***After using SMOTE technique Naive Bayes machine learning model has achieved 0.54 averge f1 score but still this score is also not good.***")
       
    st.write("***The data provided is very small and also contain duplicated data due to which the model performance is not good. Since it is related to medical field so preffered to not make any changes.So we can say that machine learning model requires large dataset and clear reviews to analyse sentiments clearly***")
    
    st.write("***Recommendation***: Data is very small and the information provided is very less try to make review section bit easy by providing clear drop down, containing options like staff, doctors, infrastructure etc so that reviews will be clear and easy for the cusomer to rate the service without their wastage of time.")

    st.write("***Understanding***: According to my understanding provider and staff is satisfactory but some improvement is required in the management for providing smooth service to the customer.")
    
    
    
    