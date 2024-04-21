import streamlit as st


st.set_page_config(layout="wide")
st.title("Decision making for autonomous driving vehicle using Deep Q network")
col = st.columns((1.5,2), gap='medium')

with col[0]:
    st.markdown('#### Gains/Losses')
    st.video('https://www.youtube.com/watch?v=2c-KlQ8SFcc')

with col[1]:
    st.markdown('###Action')
    s='left'
    st.write("action: {x}")


