import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import streamlit as st

st.title("Sales Insights for Retail Store")
st.write("This Application analyzes Sales data for various categories")
# Load the data
data=pd.read_csv(r"C:\Users\ymani\OneDrive\Desktop\NIT_Files\Statisticss\advance statistics\15th,17th- Advanced stats\15th,17th- Advanced stats\STATISTICS- Resume Project\sales_data.csv")

st.write("Sales Data: ")
st.dataframe(data)
#Descriptive Statistics
described_stats=data['units_sold'].describe()
st.subheader("Descriptive Statistics: ")
st.dataframe(described_stats)

mean_sales=data['units_sold'].mean()
median_sales=data['units_sold'].median()
mode_sales=data['units_sold'].mode()[0]
variance_sales=data['units_sold'].var()
standard_sales=data['units_sold'].std()

category_stats=data.groupby('category')['units_sold'].agg(['sum','mean','std']).reset_index()
category_stats.columns=['category','Total Units Sold', 'Average Units Sold', 'Std dev of Units Sold']
st.subheader("Categorical Statistics: ")
st.dataframe(category_stats)

#Inferential Statistics
confidence_level=0.95
degrees_freedom=len(data['units_sold'])-1
sample_mean=mean_sales
sample_standard_error=standard_sales/np.sqrt(len(data['units_sold']))

t_score=stats.t.ppf((1+confidence_level)/2,degrees_freedom)
margin_of_error=t_score*sample_standard_error

confidence_interval=(sample_mean-margin_of_error,sample_mean+margin_of_error)
st.subheader("\n Confidence Interval for the Mean of Units Sold:")
st.dataframe(confidence_interval)



confidence_level=0.99
degrees_freedom=len(data['units_sold'])-1
sample_mean=mean_sales
sample_standard_error=standard_sales/np.sqrt(len(data['units_sold']))

t_score=stats.t.ppf((1+confidence_level)/2,degrees_freedom)
margin_of_error=t_score*sample_standard_error

confidence_interval=(sample_mean-margin_of_error,sample_mean+margin_of_error)
st.subheader("\nConfidence Interval for the mean of Units Sold: ")
st.dataframe(confidence_interval)


#Hypothesis Testing

t_statistic,p_value=stats.ttest_1samp(data['units_sold'],20)

st.subheader("Hypothesis Testing(t-test):")
st.write(f'T-statistic:{t_statistic},P-value:{p_value}')

if p_value<0.05:
    st.write("Reject the Null Hypothesis: The mean units sold is significantly different from 20")
else:
    st.write("Fail to reject null Hypothesis: The mean units sold is not significantly different from 20")


#Visualizations
st.subheader("Visualizations:")
sns.set(style="whitegrid")

#Plot distribution
plt.figure(figsize=(10,6))
sns.histplot(data['units_sold'],bins=10,kde=True)
plt.title("Distribution of Units Sold")
plt.xlabel("Units Sold")
plt.ylabel("Frequency")
plt.axvline(mean_sales,color='red',linestyle='--',label='Mean')
plt.axvline(median_sales,color='blue',linestyle='--',label='Median')
plt.axvline(mode_sales,color='green',linestyle='--',label='Mode')
plt.legend()
st.pyplot(plt)



plt.figure(figsize=(10,6))
sns.barplot(x='category',y='Total Units Sold',data=category_stats)
plt.title("Total Units Sold by Category")
plt.xlabel("Category")
plt.ylabel("Total Units Sold")
st.pyplot(plt)