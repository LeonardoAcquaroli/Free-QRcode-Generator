import streamlit as st

class PersonalFooter:
    def __init__(self,
                 line_separator=True,
                 author='Leonardo Acquaroli',
                 emoji='👌🏻',
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
        footer_col1, footer_col2 = st.columns(2)
        with footer_col1:
            st.markdown(f"Brought to you by **{author}**{emoji if emoji else ''}")
        with footer_col2:
            st.image(image_url, width=image_width)
            st.markdown(f"[LinkedIn]({linkedin_url}) | [GitHub]({github_url})")
