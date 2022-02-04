import streamlit as st
import pickle
import openpyxl
import xlrd
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.cluster import MiniBatchKMeans


# loading the trained model
model = pickle.load(open('kmeansModel.pkl','rb'))


def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:#002E6D;padding:20px;font-weight:15px"> 
    <h1 style ="color:white;text-align:center;">Image Clustering</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    default_value_goes_here = ""

    uploaded_file = st.file_uploader("Choose a XLSX file (it must contain pixel details of images)", type="xlsx")

    global dataframe
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        dataframe = df
   
    result = ""
    if st.button("Cluster"):
      featureshost = dataframe
      model = KMeans(n_clusters=10, max_iter=1000)
      prediction = model.fit(featureshost)
    
      result = prediction.labels_
      st.write(result)


if __name__ == '__main__':
    main()
