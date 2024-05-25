from PIL import Image
import google.generativeai as genai
import streamlit as st
import re

#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


genai.configure(api_key='AIzaSyBLofJGHX1U96SCLOn5hytoOaLcEIDoFcY')

generation_config = {
    "temperature": 0.2,
    "top_p": 1,
    "top_k": 0,
    "max_output_tokens": 200,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", 
     "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH",
     "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
     "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", 
     "threshold": "BLOCK_NONE"},
]


model = genai.GenerativeModel(
    model_name="gemini-1.0-pro",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

def gemini_pro_response(user_prompt):
    chat_session = model.start_chat()
    response = chat_session.send_message(user_prompt)
    response_text = ""
    for chunk in response:
        response_text += chunk.text
    return response_text


model1 = genai.GenerativeModel("gemini-1.5-pro",safety_settings=safety_settings,
    generation_config=generation_config,)
def gemini_pro_vision_response(image):
    gemini_pro_vision_model = model1
    response = gemini_pro_vision_model.generate_content(["given medicine image ,read it properly as much as possible like a ocr manner and give accurate text from medicine image ", image])
    text = response.text
    return text
    

def mask_sensitive_infot(respose_text):
            respose_text = re.sub(r'\b[A-Z][a-z]*\b', '[NAME]', text)
            respose_text = re.sub(r'\b\d{1,2}/\d{1,2}/\d{2,4}\b', '[DATE]', text)
            respose_text = re.sub(r'\b\d{1,2}-\d{1,2}-\d{2,4}\b', '[DATE]', text)
            return respose_text
chat_session = model.start_chat(
    history=[
    {
      "role": "user",
      "parts": [
        "can you tell me about ajapride diabetes tablets\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        "can you tell me about ajapride diabetes tablets",
        "tell me about ajapride tablets",
        "can you tell me about ajapride diabetes tablets\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Ajapride is a medication used to treat gastrointestinal disorders such as heartburn, indigestion, and nausea. It is not indicated for the treatment of diabetes.\n\n**Important Note:** I am not a medical professional and cannot provide medical advice. If you have questions about diabetes or any other health condition, please consult with a qualified healthcare provider.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "what is the approximate price of ajapride in india\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The approximate price of Ajapride in India can vary depending on the dosage, brand, and location. \n\nAccording to online pharmacies and drug price comparison websites, the approximate price range for Ajapride tablets in India is as follows:\n\n* **Ajapride 10 mg tablets:** INR 10 to INR 20 per strip of 10 tablets\n* **Ajapride 20 mg tablets:** INR 15 to INR 30 per strip of 10 tablets\n\nPlease note that these prices are approximate and may vary depending on factors such as:\n\n* Brand and manufacturer\n* Dosage and quantity\n* Location and availability\n* Pharmacy or retailer\n\nFor the most accurate and up-to-date pricing information, it is recommended to consult with a local pharmacy or check online drug price comparison websites.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "Hydrochlorothiazide (Microzide) telll me about this tablet",
      ],
    },
    {
      "role": "model",
      "parts": [
      ],
    },
    {
      "role": "user",
      "parts": [
        "Hydrochlorothiazide (Microzide) telll me about this tablet",
      ],
    },
    {
      "role": "model",
      "parts": [
      ],
    },
    {
      "role": "user",
      "parts": [
        "er\nwhat is the approximate price of ajapride in india",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The approximate price of Ajapride in India can vary depending on the dosage, brand, and location. \n\nAccording to online pharmacies and drug price comparison websites, the approximate price range for Ajapride tablets in India is as follows:\n\n* **Ajapride 10 mg tablets:** INR 10 to INR 20 per strip of 10 tablets\n* **Ajapride 20 mg tablets:** INR 15 to INR 30 per strip of 10 tablets\n\nPlease note that these prices are approximate and may vary depending on factors such as:\n\n* Brand and manufacturer\n* Dosage and quantity\n* Location and availability\n* Pharmacy or retailer\n\nFor the most accurate and up-to-date pricing information, it is recommended to consult with a local pharmacy or check online drug price comparison websites.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "what is the approximate price of  Amlodipine in india",
      ],
    },
    {
      "role": "model",
      "parts": [
        "The approximate price of Amlodipine in India can vary depending on the dosage, brand, and location. \n\nAccording to online pharmacies and drug price comparison websites, the approximate price range for Amlodipine tablets in India is as follows:\n\n* **Amlodipine 5 mg tablets:** INR 2 to INR 5 per tablet\n* **Amlodipine 10 mg tablets:** INR 3 to INR 7 per tablet\n\nPlease note that these prices are approximate and may vary depending on factors such as:\n\n* Brand and manufacturer\n* Dosage and quantity\n* Location and availability\n* Pharmacy or retailer\n\nFor the most accurate and up-to-date pricing information, it is recommended to consult with a local pharmacy or check online drug price comparison websites.",
      ],
    },
    {
      "role": "user",
      "parts": [
        "can you tell me about amlodipine in india\n",
      ],
    },
    {
      "role": "model",
      "parts": [
      ],
    },
    {
      "role": "user",
      "parts": [
        "can you tell me about amlodipine in india\n",
      ],
    },
    {
      "role": "model",
      "parts": [
        "**Amlodipine in India**\n\nAmlodipine is a calcium channel blocker medication used to treat high blood pressure (hypertension) and angina (chest pain). It is marketed in India under various brand names, including:\n\n* Amlodipine\n* Amlodac\n* Amlokind\n* Amlovas\n* Caduet\n* Norvasc\n\n**Dosage and Administration**\n\nAmlodipine is available in tablet form in strengths of 5 mg and 10 mg. The usual starting dose is 5 mg once daily, which can be increased to 10 mg once daily as needed.\n\n**Price**\n\nThe price of Amlodipine in India varies depending on the brand, dosage, and quantity. According to online pharmacies and drug price comparison websites, the approximate price range is as follows:\n\n* **Amlodipine 5 mg tablets:** INR 2 to INR 5 per tablet\n* **Amlodipine 10 mg tablets:** INR 3 to INR 7 per tablet\n\n**Availability**\n\nAmlodipine is widely available in India and can be purchased from pharmacies with a doctor's prescription.\n\n**Uses**\n\nAmlodipine is primarily used to treat:\n\n* **Hypertension:** Amlodipine helps lower blood pressure by relaxing the blood vessels, allowing blood to flow more easily.\n* **Angina:** Amlodipine improves blood flow to the heart, which can relieve chest pain caused by angina.\n\n**Side Effects**\n\nCommon side effects of Amlodipine include:\n\n* Headache\n* Dizziness\n* Flushing\n* Leg swelling\n* Nausea\n\n**Precautions**\n\nBefore taking Amlodipine, it is important to inform your doctor about any of the following:\n\n* Liver disease\n* Kidney disease\n* Heart failure\n* Aortic stenosis (narrowing of the aortic valve)\n\n**Drug Interactions**\n\nAmlodipine may interact with other medications, including:\n\n* Digoxin\n* Warfarin\n* Lithium\n* Nonsteroidal anti-inflammatory drugs (NSAIDs)\n\n**Important Note**\n\nThe information provided here is for general knowledge and informational purposes only, and does not constitute medical advice. It is essential to consult with a qualified healthcare professional for any health concerns or before making any decisions related to your health or treatment.",
      ],
    },
  ]
)


# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Display the logo
#image = Image.open(r"C:\Users\YESHWANTH M S\OneDrive\Pictures\LOGO (1).png")
st.markdown("<h1 style='text-align: left; font-size:50px;color: green;'>Welcome to Medilyzer⚕️</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: left; font-size:25px;font-weight:bold; color: white;'>Choose your input form</h1>", unsafe_allow_html=True)


option = st.radio("Choose Input Type:", ("Text", "Image"))

if option == "Text":
    text_input = st.text_area("Enter Text:")
    if st.button("Submit"):
        user_prompt = ( 
            f"Note: if text is one or two word given related to medicine or company or any medicine technical term, just give output but don't give null answer or not sufficient answer. Can you provide detailed information about the following medicine from given image or text: '{text_input}'. "
            "Specifically, include:\n"
            "1.  Whether this medicine is generic or branded (Note: give same answer of each iteration,Before giving answer verify once trained data and confirm it and give same answer every time) (just specify whether it is generic/branded; caution: always give the correct answer and once cross verify, don't give irrelevant information)and at next line.\n\n"
            "2. Give the approximate price range within 50INR if available like(30-35)(30-45)(25-30)(25-35)(20-30)(NOTE: Always give same answer after each iteration).\n"
            "3. A brief description (including: precautions but not much just give 3-4 points) of this medicine.\n"
            "4. Always display disclaimer to refer doctors."
        )
        response_text = gemini_pro_response(user_prompt)
        st.session_state['chat_history'].append({"user": text_input, "response": response_text})
        st.markdown(f"**Description:** {mask_sensitive_infot(respose_text)}")

if option == "Image":
    image_file = st.file_uploader("Upload Image:", type=["jpg", "png", "jpeg"])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("Extract Text"):
            extracted_text =gemini_pro_vision_response(image)
            user_prompt = (
                f"Can you provide detailed information about the following medicine extracted from an image: {extracted_text}.\n"
                "Specifically, give output each next line for following commands:\n"
                "1. Whether this medicine is generic or branded (Note: give same answer of each iteration,Before giving answer verify once trained data and confirm it and give same answer every time) (just specify whether it is generic/branded; caution: always give the correct answer and once cross verify, don't give irrelevant information)and at next line.\n\n"
                "2. at next line mention and Give the approximate price range within 50INR if available like Rs(30-35)Rs(30-45)Rs(25-30)Rs(25-35)(20-30)(NOTE: Always give same answer after each iteration).\n"
                "3. A very small description (including: precautions in 3-4 points) of this medicine.\n"
                "4. Always display disclaimer to refer doctors."
            )
            response_text = gemini_pro_response(user_prompt)
            st.session_state['chat_history'].append({"user": extracted_text, "response": response_text})
            st.markdown(f"**Description:** {mask_sensitive_infot(response_text)}")

# Display chat history
if 'chat_history' in st.session_state and st.session_state['chat_history']:
    st.write("### Chat History")
    for i, chat in enumerate(st.session_state['chat_history']):
        st.write(f"**User:** {chat['user']}")
        st.write(f"**Response:** {chat['response']}")   
