import qrcode
import io
import streamlit as st
from streamlit_footer import PersonalFooter

st.title("QR Code Generator")

language_text = {
    'English': {
        'url': 'Insert url:',
        'download': 'Download QR Code',
        'fill_color': 'QR code color',
        'background_color': 'QR code background color',
        'complete': 'Download completed',
        'url_error': 'Please insert a url'
    },
    'Italian': {
        'url': 'Inserisci url:',
        'download': 'Scarica il QR Code',
        'fill_color': 'Colore del QR code',
        'background_color': 'Colore di sfondo del QR code',
        'complete': 'Download completato',
        'url_error': 'Inserisci un url valido'
    }
}

# Create an upper container
with st.container():
    language = st.selectbox("Language | Lingua", ["English", "Italian"])

st.markdown("""
<style>
    .column {
        margin-right: 40px;
    }
</style>
""", unsafe_allow_html=True)

# Create a lower container with two columns
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        url = st.text_input(language_text[language]['url'])
    with col2:
        fill_color = st.color_picker(language_text[language]['fill_color'], '#000000')
        background_color = st.color_picker(language_text[language]['background_color'], '#ffffff')

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

qr.add_data(url)
img = qr.make(fit=True)


img = qr.make_image(fill_color=fill_color, back_color=background_color)

# Convert to bytes-type file to allow downloading
img_byte_arr = io.BytesIO()
img.save(img_byte_arr, format='PNG')
img_byte_arr = img_byte_arr.getvalue()
st.image(img_byte_arr)

# Download
if st.download_button(label=language_text[language]['download'],
                      data=img_byte_arr,
                      file_name="qr_code.png",
                      mime="image/png"):
    
    # Check for the url
    if url != None:
        st.success(language_text[language]['complete'])
    else:
        st.error(language_text[language]['url_error'])

PersonalFooter()