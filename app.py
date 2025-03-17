import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
if st.button("Check this"):
  #time_series = np.random.randn(150)
  n = 150    #No. of time steps
  x = np.arange(n)    #time steps
  y = np.cumsum(np.random.randn(n))    #Random walk - cumulative sum of normal distribution
  coefficients = np.polyfit(x, y, 1)
  trendline = np.poly1d(coefficients)
  plt.plot(x,y)
  plt.plot(x,trend_line(x))
  plt.xlabel("Time steps")
  plt.ylabel("Values")
  plt.title("Random walk with trend line")
  #plt.plot(time_series)
  #plt.title("Random 150-unit Time Series")
  #plt.xlabel("Time")
  #plt.ylabel("Values")
  st.pyplot(plt.gcf())
