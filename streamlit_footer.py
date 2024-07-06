import streamlit as st

class PersonalFooter:
    def __init__(self,
                 author='Leonardo Acquaroli',
                 image_url='https://raw.githubusercontent.com/LeonardoAcquaroli/Free-QRcode-Generator/master/Leo_wood-circlecrop.png',
                 linkedin_url='https://www.linkedin.com/in/leonardo-acquaroli/',
                 github_url='https://github.com/LeonardoAcquaroli'
                 ):
        
        # Divider line    
        st.markdown('<hr>', unsafe_allow_html=True)
        
        # Footer content
        st.html(f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Personal Footer</title>
            <link rel="stylesheet" href="styles.css">
        </head>
        <body>
            <!-- Footer Section -->
            <footer>
                <div class="footer-content">
                    <p>Brought to you by {author}</p>
                    <img src="{image_url}" alt="Leonardo Acquaroli" class="footer-photo">
                    <div class="footer-info">
                        <a href="{linkedin_url}" target="_blank">LinkedIn</a>
                        <a href="{github_url}" target="_blank">GitHub</a>
                    </div>
                </div>
            </footer>   
        </body>
        </html>
        """)