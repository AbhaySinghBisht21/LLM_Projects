from dotenv import load_dotenv
load_dotenv() #loads all the env vars

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#configure Genai key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


##Function to load google Gemini MODEL and """provide query as response"""

def get_gemini_response(question,prompt): # input and prompt("how the model is going to behave")
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

##Function to retrieve query from the database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()  # Close the connection before processing the rows
    for row in rows:
        print(row)
    return rows

##defining the prompt 

prompt=[
    
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in AI class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="AI"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
        
        ]

#Streamlit APP

st.set_page_config(page_title="I can Retrive any sql query")
st.header("Gemini to retrieve sql data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)