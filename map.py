import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt


data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['a', 'b', 'c']
        )

city = pd.DataFrame({
'nigerian_cities' : ['Lagos', 'Abeokuta', 'Port Harcourt', 'Maiduguri', 'Kano', 
'Katsina', 'Nnewi, Anambra', 'Agbor, Ika South', 'Ikeja, Lagos', 'Ughelli', 'Akure'],
'latitude' : [6.465422, 7.145244, 4.824167, 11.833333, 12.000000, 12.985531, 6.010519, 6.264092, 6.605874, 5.500187, 7.250771],
'longitude' : [3.406448, 3.327695, 7.033611, 13.150000, 8.516667, 7.617144, 6.910345, 6.201883, 3.349149, 5.993834,  5.210266]
})

st.image('Kings.PNG', width=900)


x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

st.title('Using Streamlit to Plot Chart')

st.subheader('Nigerian city Lat and Long')
st.map(city)

st.subheader('Line Chart')
st.line_chart(data)
st.subheader('Area Chart')
st.area_chart(data)

st.subheader('Bar Chart')
st.bar_chart(data)

# st.subheader('Scatter Plot')
# plt.scatter(data['a'], data['b'])
# st.pyplot()

st.graphviz_chart("""
                  digraph{
                      watch -> like
                      like -> share
                      share -> substribe
                      share -> watch
                  }
                  """)