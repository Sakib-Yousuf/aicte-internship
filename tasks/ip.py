import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
st.title("The data is ")
d1=pd.read_csv("country_wise_latest.csv",na_values="?",skipinitialspace=True)
# print(d1.head())
print(d1.shape)
print(d1.info())
# d1.isnull().sum()
# d1.duplicated().sum()
plt.xlabel='Deaths'
plt.ylabel='confirmed'
plt.plot(d1['Deaths'],d1['Confirmed'])
plt.show()
d1['Country/Region'].duplicated().sum()
max1=d1['Deaths'].max()
sum1=d1['Deaths'].sum()
st.dataframe(d1)
print("the max is ",max1,' the sum is ',sum1)
count=1
for val in d1['Deaths']:
    if val==max1:
        print(count)
    count+=1
