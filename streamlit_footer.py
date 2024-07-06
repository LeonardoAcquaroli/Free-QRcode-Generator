import streamlit as st

class PersonalFooter:
    def __init__(self,
                 line_separator=True,
                 author='Leonardo Acquaroli',
                 image_url='https://raw.githubusercontent.com/LeonardoAcquaroli/Free-QRcode-Generator/master/Leo_wood-circlecrop.png',
                 linkedin_url='https://www.linkedin.com/in/leonardo-acquaroli/',
                 github_url='https://github.com/LeonardoAcquaroli',
                 image_width=70, 
                 image_height=70 
                 ):
        
        # Divider line
        if line_separator:
            st.markdown('<hr>', unsafe_allow_html=True)
        
        # Adjusted footer content with streamlit elements
        st.markdown(f"Brought to you by **{author}**")
        st.image(image_url, width=image_width, caption="Leonardo Acquaroli")
        st.markdown(f"[LinkedIn]({linkedin_url}) | [GitHub]({github_url})")
