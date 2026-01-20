import streamlit as st

# Page configuration
st.set_page_config(
    page_title="HDL Tools Hub",
    page_icon="🔧",
    layout="wide"
)

# Title and description
st.title("🔧 Hardware Direct Tools Hub")
st.markdown("Central hub for all Hardware Direct internal applications")

st.divider()

# Dictionary of apps - easily add more apps here
apps = {
    "PO Wizard": {
        "description": "Multi-supplier Purchase Order Builder for Cin7",
        "url": "https://cin7-po-wizard.streamlit.app/",
        "emoji": "📦"
    },
    "PM7 to Cin7 Importer": {
        "description": "Import data from PM7 to Cin7 system",
        "url": "https://pm7-to-cin7-importer.streamlit.app/",
        "emoji": "📥"
    },
    "App 3": {
        "description": "Description of your third app",
        "url": "http://localhost:8503",
        "emoji": "🔍"
    }
}

# Custom CSS for big square buttons
st.markdown("""
<style>
    .app-button {
        display: block;
        padding: 40px 20px;
        background-color: #F8F9FA;
        border: 2px solid #F47920;
        border-radius: 10px;
        text-align: center;
        text-decoration: none;
        color: #2B2B2B;
        transition: all 0.3s ease;
        margin-bottom: 20px;
        min-height: 200px;
    }
    .app-button:hover {
        background-color: #F47920;
        color: white;
        transform: translateY(-5px);
        box-shadow: 0 5px 15px rgba(244, 121, 32, 0.3);
    }
    .app-emoji {
        font-size: 60px;
        margin-bottom: 15px;
    }
    .app-title {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .app-description {
        font-size: 14px;
        opacity: 0.8;
    }
</style>
""", unsafe_allow_html=True)

# Display apps in a grid layout
cols = st.columns(3)

for idx, (app_name, app_info) in enumerate(apps.items()):
    with cols[idx % 3]:
        st.markdown(f"""
        <a href="{app_info['url']}" target="_blank" class="app-button">
            <div class="app-emoji">{app_info['emoji']}</div>
            <div class="app-title">{app_name}</div>
            <div class="app-description">{app_info['description']}</div>
        </a>
        """, unsafe_allow_html=True)

# Instructions for adding new apps
with st.expander("ℹ️ How to add new apps"):
    st.markdown("""
    To add a new app to this hub:

    1. **Add an entry to the `apps` dictionary** in this file with:
       - App name as the key
       - A dictionary with `description`, `url`, and `emoji`

    2. **Example:**
    ```python
    "My New App": {
        "description": "What this app does",
        "url": "http://localhost:8504",
        "emoji": "🚀"
    }
    ```

    3. **Running apps on different ports:**
    ```bash
    streamlit run app1.py --server.port 8501
    streamlit run app2.py --server.port 8502
    streamlit run app3.py --server.port 8503
    ```
    """)

st.divider()

# Footer
st.markdown("*Add, modify, or remove apps by editing the `apps` dictionary in this file*")
