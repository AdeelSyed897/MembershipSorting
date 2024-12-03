import streamlit as st
import pandas as pd

def lower(str):
    return str.lower()

st.write("SASE Backend")
file = st.file_uploader('Create DataSet',accept_multiple_files=False)



newDf= pd.DataFrame(columns=['WPI Email', 'Name', 'Points', 'Events Attended'])


if file is not None:
    df = pd.read_csv(file)
    nameCol=df['Full Name']
    emailCol=df['WPI Email']
    lowerName=nameCol.apply(lower)
    lowerEmail=emailCol.apply(lower)
    df['Full Name']=lowerName
    df['WPI Email']=lowerEmail
    st.write(df)
    visited=[]
    for i in range(len(df)):
        row=[]
        events=[]
        fullName=df['Full Name'][i]
        email=df['WPI Email'][i]
        events.append(df['Event'][i])
        if email in visited:
            continue
        filteredNames = df[df['WPI Email'] == email]
        points=len(filteredNames)
        events=filteredNames['Event'].tolist()
        visited.append(email)
        row.append(email)
        row.append(fullName)
        row.append(points)
        row.append(events)
        newDf.loc[len(newDf)] = row


st.write(newDf)
