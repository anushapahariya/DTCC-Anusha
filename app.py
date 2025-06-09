import streamlit as st

# Page configuration
st.set_page_config(page_title="AURA", layout="wide")

# ---------- CSS Styling ----------
st.markdown("""
    <style>
        .stApp {
            background-color: #D3D3D3;
        }

        section[data-testid="stSidebar"] {
            background-color: #f0f0f0;
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

        .main-header h1, .main-header h3 {
            color: white;
            margin: 0;
        }

        summary {
            background-color: #003366 !important;
            color: white !important;
            padding: 12px;
            font-size: 16px;
            border-radius: 8px 8px 0 0;
            font-weight: bold;
        }

        details[open] > summary ~ * {
            background-color: white;
            padding: 16px;
            border-radius: 0 0 8px 8px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }

        details {
            margin-bottom: 20px;
        }
        
    div.stButton > button {
    background-color: #fffff;
    color: black;
    font-family: serif;
    font-weight: bold;
    border: None;
    border-radius: 8px;
    padding: 0.5em 1em;
}

div.stButton > button:hover {
    background-color: #002244;
    color: white;
}
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
   <div class='header' style="line-height: 1.2;">
    <h8 style="margin-bottom: 0;">AURA</h8>
    <h4 style="margin-top: 0;">Automated Understanding & Regulatory Assistant</h4>
</div>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("📑 AURA")

    # Regulation selection
    selected_regulation = st.selectbox("Choose Regulation:", [
        "Regulation 2021", "Regulation 2019", "Regulation 2017"
    ])

    # Action selector
    action = st.radio("Choose Action", [
        "Compare Previous vs Latest Regulation",
        "New Regulation"
    ])
    st.markdown("-----------------------------")
    if st.button(" 🕰️ View History"):
        st.info("Getting history")
    if st.button("🔍 Summary"):
        st.info("Getting Summary")
    if st.button("📄 View Documentation"):
        st.info("Getting history")


# ---------- MAIN PAGE ----------

st.subheader("DASHBOARD")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button(" 🔄 Regenerate Graph"):
        st.info("Regenerate ")

with col2:
    if st.button(" 📁 Download the KOP"):
        st.success("KOP is being downloaded")

with col3:
    if st.button(" 📊 Download New Graph"):
        st.info("Download New Graph selected.")

with col4:
    if st.button(" 📄 Download the BRD"):
        st.info("Download New Graph selected.")

with col5:
    if st.button("🏠 Home Page"):
        st.info("Go to home page selected.")

st.subheader("UPLOAD REGULATIONS")

# Upload New Regulation
new_pdf = st.file_uploader("Upload New Regulation PDF", type=["pdf"])

# Upload Old Regulation (if comparing)
old_pdf = None
if action == "Compare Previous vs Latest Regulation":
    old_pdf = st.file_uploader("Upload Old Regulation PDF", type=["pdf"])

# Upload Button
if st.button("Upload"):
    if action == "Compare Previous vs Latest Regulation":
        if new_pdf and old_pdf:
            st.success(f"Both PDFs uploaded:\n- Old: {old_pdf.name}\n- New: {new_pdf.name}")
        else:
            st.warning("Please upload both Old and New regulation PDFs.")
    else:
        if new_pdf:
            st.success(f"Uploaded New Regulation PDF: {new_pdf.name}")
        else:
            st.warning("Please upload the New Regulation PDF.")

st.markdown("-----------------------------")
