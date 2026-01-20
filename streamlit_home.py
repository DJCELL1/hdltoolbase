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
    "App 2": {
        "description": "Description of your second app",
        "url": "http://localhost:8502",
        "emoji": "📈"
    },
    "App 3": {
        "description": "Description of your third app",
        "url": "http://localhost:8503",
        "emoji": "🔍"
    }
}

# Display apps in a grid layout
cols = st.columns(3)

for idx, (app_name, app_info) in enumerate(apps.items()):
    with cols[idx % 3]:
        st.markdown(f"### {app_info['emoji']} {app_name}")
        st.markdown(app_info['description'])
        st.markdown(f"[Open {app_name}]({app_info['url']})")
        st.markdown("---")

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
