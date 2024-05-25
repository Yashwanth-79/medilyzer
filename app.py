from PIL import Image
import google.generativeai as genai
import streamlit as st

# Uncomment and set the path to tesseract executable if necessary
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

genai.configure(api_key='AIzaSyBLofJGHX1U96SCLOn5hytoOaLcEIDoFcY')

generation_config = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 200,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

model1 = genai.GenerativeModel("gemini-1.5-pro", safety_settings=safety_settings, generation_config=generation_config)


def gemini_pro_response(user_prompt):
    chat_session = model.start_chat()
    response = chat_session.send_message(user_prompt)
    response_text = ""
    for chunk in response:
        response_text += chunk.text
    return response_text


def gemini_pro_vision_response(image):
    gemini_pro_vision_model = model1
    response = gemini_pro_vision_model.generate_content(
        ["given medicine image, read it properly as much as possible like an OCR manner and give accurate text from medicine image", image])
    text = response.text
    return text


# Initialize session state for chat history and active section
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

if 'active_section' not in st.session_state:
    st.session_state['active_section'] = 'classify_compare'

# Define sidebar
st.sidebar.title("Options")
if st.sidebar.button("Classify and Compare"):
    st.session_state['active_section'] = 'classify_compare'
if st.sidebar.button("Generic List"):
    st.session_state['active_section'] = 'generic_list'


st.sidebar.markdown("<h1 style='text-align: left; font-size:50px;color: green;'>Welcome to Medilyzer⚕️</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h1 style='text-align: left; font-size:25px;font-weight:bold; color: white;'>Choose your input form</h1>", unsafe_allow_html=True)

# Define main section based on sidebar selection
if st.session_state['active_section'] == 'classify_compare':
    st.title("Classify and Compare")

    option = st.radio("Choose Input Type:", ("Text", "Image"))

    if option == "Text":
        text_input = st.text_area("Enter Text:")
        if st.button("Submit"):
            user_prompt = (
                f"Note: if text is one or two word given related to medicine or company or any medicine technical term, just give output but don't give null answer or not sufficient answer. Can you provide detailed information about the following medicine from given image or text: '{text_input}'. "
                "Specifically, include:\n"
                "1. Whether this medicine is generic or branded (just specify whether it is generic/branded; caution: always give the correct answer and once cross verify, don't give irrelevant information).\n"
                f"2. {text_input} at next line mention and Give the approximate price range (for generic medicine within 50INR if available like Rs(30-35)Rs(30-45)Rs(25-30)Rs(25-35)(20-30))(for branded medicine keep price ranges at more 70 INR )(keep changing price range for other tablets only in small margin)(NOTE: Always give same answer after each iteration).\n"
                "3. A brief description (including: precautions but not much just give 3-4 points) of this medicine.\n"
                "4. Always display disclaimer to refer doctors."
            )
            response_text = gemini_pro_response(user_prompt)
            st.session_state['chat_history'].append({"user": text_input, "response": response_text})
            st.markdown(f"**Description:** {response_text}")

    if option == "Image":
        image_file = st.file_uploader("Upload Image:", type=["jpg", "png", "jpeg"])
        if image_file is not None:
            image = Image.open(image_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            if st.button("Extract Text"):
                extracted_text = gemini_pro_vision_response(image)
                user_prompt = (
                    f"Can you provide detailed information about the following medicine extracted from an image: {extracted_text}.\n"
                    "Specifically, give output each next line for following commands:\n"
                    "1. Whether this medicine is generic or branded (just specify whether it is generic/branded; caution: always give the correct answer and once cross verify, don't give irrelevant information) (NOTE: I got some wrong answers, correct it and give me proper answer and same answer for each iteration and continue at next line.\n\n"
                    f"2. {extracted_text} at next line mention and Give the approximate price range (for generic medicine within 50INR if available like Rs(30-35)Rs(30-45)Rs(25-30)Rs(25-35)(20-30))(for branded medicine keep price ranges at more 70 INR )(keep changing price range for other tablets only in small margin)(NOTE: Always give same answer after each iteration).\n"
                    "3. A very small description (including: precautions in 3-4 points) of this medicine.\n"
                    "4. Always display disclaimer to refer doctors."
                )
                response_text = gemini_pro_response(user_prompt)
                st.session_state['chat_history'].append({"user": extracted_text, "response": response_text})
                st.markdown(f"**Description:** {response_text}")

elif st.session_state['active_section'] == 'generic_list':
    st.title("Generic List")
    text_input = st.text_area("Enter Text:")
    if st.button("Submit"):
        user_prompt = (
            f"Can you provide a list of generic and branded similar to the following: '{text_input}', with their price ranges in INR. Please display the information in a table format with columns: generic meds, generic meds price, branded meds, branded price."
        )
        response_text = gemini_pro_response(user_prompt)
        st.session_state['chat_history'].append({"user": text_input, "response": response_text})
        st.markdown(f"**Similar Medicines and Prices:**\n\n{response_text}")

# Display chat history
if 'chat_history' in st.session_state and st.session_state['chat_history']:
    st.write("### Chat History")
    for i, chat in enumerate(st.session_state['chat_history']):
        st.write(f"**User:** {chat['user']}")
        st.write(f"**Response:** {chat['response']}")
