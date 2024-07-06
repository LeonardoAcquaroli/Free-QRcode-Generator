import streamlit as st

class PersonalFooter:
    def __init__(self,
                 line_separator=True,
                 author='Leonardo Acquaroli',
                 image_url='https://raw.githubusercontent.com/LeonardoAcquaroli/Free-QRcode-Generator/master/Leo_wood-circlecrop.png',
                 linkedin_url='https://www.linkedin.com/in/leonardo-acquaroli/',
                 github_url='https://github.com/LeonardoAcquaroli',
                 image_width=10, 
                 image_height=10 
                 ):
        
        # Divider line
        if line_separator:
            st.markdown('<hr>', unsafe_allow_html=True)
        
        # Adjusted footer content with image size parameters applied directly to the img tag
        st.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Personal Footer</title>
        </head>
        <body>
            <!-- Footer Section -->
            <footer>
                <div class="footer-content">
                    <p>Brought to you by {author}</p>
                    <img src="{image_url}" alt="Leonardo Acquaroli" style="width: {image_width}px; height: {image_height}px;" class="footer-photo">
                    <div class="footer-info">
                        <a href="{linkedin_url}" target="_blank">LinkedIn</a>
                        <a href="{github_url}" target="_blank">GitHub</a>
                    </div>
                </div>
            </footer>   
        </body>
        </html>
        """)