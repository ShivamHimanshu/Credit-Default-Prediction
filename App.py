#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pickle


model = pickle.load(open('model.pkl', 'rb'))

def run():
    
    st.title("Credit Default Prediction using Machine Learning")

    ##age
    Age = st.number_input("Age(in Years)",value=0)
    
    ## For gender
    gen_display = ('Female','Male')
    gen_options = list(range(len(gen_display)))
    gen = st.selectbox("Gender",gen_options, format_func=lambda x: gen_display[x])

    ## For Car ownership
    car_display = ('No','Yes')
    car_options = list(range(len(car_display)))
    car = st.selectbox("Owns Car", car_options, format_func=lambda x: car_display[x])

    ## For House ownership
    house_display = ('No','Yes')
    house_options = list(range(len(house_display)))
    house = st.selectbox("Owns House", house_options, format_func=lambda x: house_display[x])

    ##No. of Children
    No_of_Children = st.number_input("No. of Children",value=0)
    
    ##Net Yearly income
    Net_Yearly_Income = st.number_input("Net Yearly Income",value=0)
    
    ##No of Years Employed
    No_of_years_employed = st.number_input("No. of Years Employed",value=0)
    
    ##Occupation Type
    Occupation_display = ('Accountants','Cleaning staff','Cooking staff','Core staff','Drivers','High skill tech staff','HR staff',
                       'IT staff','Laborers','Low-skill Laborers','Managers', 'Medicine staff', 'Private service staff',
                       'Realty agents','Sales staff','Secretaries','Security staff',
                       'Unknown','Waiters/barmen staff')
    Occupation_options = list(range(len(Occupation_display)))
    Occupation = st.selectbox("Occupation Type", Occupation_options, format_func=lambda x: Occupation_display[x])
    
    ##Total Family Members
    Total_Family_members = st.number_input("No. of Family Members",value=0)
    
     ## For Migrant
    Migrant_display = ('No','Yes')
    Migrant_options = list(range(len(Migrant_display)))
    Migrant = st.selectbox("Migrant Worker", Migrant_options, format_func=lambda x: Migrant_display[x])
    
    ##Yearly debt payments
    Yearly_Debt_Payments = st.number_input("Yearly Debt Payments",value=0)
    
    ##Credit limit
    Credit_limit = st.number_input("Credit limit",value=0)
    
    ##Credit limit used
    Credit_limit_used = st.number_input("Credit limit used(%)",value=0)
    
    ##Credit Score
    Credit_Score = st.number_input("Credit Score",value=0)
    
    #Prev Default
    Prev_Default = st.number_input("No. of Previous Defaults",value=0)
    
    #Default in last 6 months
    
    default_display = ('No','Yes')
    default_options = list(range(len(default_display)))
    default = st.selectbox("Defaulted in last 6 months",default_options, format_func=lambda x: default_display[x])

    if st.button("Submit"):
        
        features = [[Age,gen,car,house,No_of_Children,Net_Yearly_Income,Occupation,Total_Family_members,
                    Migrant,Yearly_Debt_Payments,Credit_limit,Credit_limit_used,Credit_Score,Prev_Default,
                    default,No_of_years_employed]]
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 1:
            st.error(
                
                'Customer will default'
            )
        else:
            st.success(

                'Customer will not default'
            )
            
    if st.button("About"):
        st.text("Predicts whether the Credit Card Customer will default or not")
        st.text("Built by Shivam Himanshu")

run()

