import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
if st.button("Check this"):
  time_series = np.random.randn(150)
  plt.plot(time_series)
  plt.title("Random 150-unit Time Series")
  plt.xlabel("Time")
  plt.ylabel("Values")
  coefficients = np.polyfit("Time" "Values",1)
  trendline = np.poly1d(coefficients)
  st.pyplot(plt.gcf())
