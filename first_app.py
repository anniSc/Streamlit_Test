import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('ML4B 2024')

#checkbox
if st.checkbox('Show Image'):
    image = Image.open('./puppy.jpg')
    st.image(image, caption='Running Puppy')

st.write("Here's my data:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.write(df)

#Line chart
chart_data = df

st.line_chart(chart_data)
    

#widget in sidebar
option = st.sidebar.selectbox(
    'Which column do you like best?',
     df['first column'])

'You selected:', option

