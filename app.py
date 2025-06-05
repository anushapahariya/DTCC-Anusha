import streamlit as st

st.set_page_config(page_title="AURA", layout="wide")

st.markdown("""
    <style>
        html, body, [data-testid="stApp"] {
            background-color: #e8eaed;
            color: black;
            font-family: serif;
        }
        .header {
            background-color: #005c99;
            color: white;
            padding: 1rem;
            font-size: 2rem;
            text-align: center;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
            font-weight: 800; /* extra bold */
            font-family: serif;
        }
        .result-box {
            background-color: white;
            padding: 1.5rem;
            border-radius: 0.75rem;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            height: 100%;
            color: black;
            font-family: serif;
            font-weight: 800;
        }
        .stTextInput > div > div > input {
            font-weight: 800;
            background-color: white;
            font-family: serif;
        }
        .stButton > button {
            background-color: #007acc;
            color: white;
            font-weight: 800;
            font-family: serif;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
   <div class='header' style="line-height: 1.2;">
    <h8 style="margin-bottom: 0;">AURA</h8>
    <h4 style="margin-top: 0;">Automated Understanding & Regulatory Assistant</h4>
</div>
""", unsafe_allow_html=True)

left_col, right_col = st.columns([1, 2.5])

with left_col:
    st.subheader("Upload")
    uploaded_file = st.file_uploader("Upload a document", type=["pdf", "txt", "docx"])

    st.subheader("Ask")
    question = st.text_input("Your Question", placeholder="e.g., What is the document about?")

    get_answer = st.button("Get Answer")

with right_col:
    st.subheader("Result")
    st.markdown('<div class="result-box">', unsafe_allow_html=True)

    if get_answer:
        if not uploaded_file:
            st.error("Please upload a document.")
        elif not question.strip():
            st.error("Please type a question.")
        else:
            st.success(f"Answer to: {question}")
            st.write("This is a placeholder answer. Connect to a model backend here.")
    else:
        st.info("Upload a document and ask a question to see the result here.")

    st.markdown('</div>', unsafe_allow_html=True)
