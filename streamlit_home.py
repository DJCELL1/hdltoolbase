import streamlit as st

# Page configuration
st.set_page_config(
    page_title="HDL Tools Hub",
    page_icon="🔧",
    layout="wide"
)

# Header with logo
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("Logos-01.jpg", use_container_width=True)

st.markdown("<h2 style='text-align: center; color: #2B2B2B;'>Tools Hub</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Central hub for all Hardware Direct internal applications</p>", unsafe_allow_html=True)

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
    "Kickplate Nesting Optimizer": {
        "description": "Optimize cutting layouts and generate door labels",
        "url": "https://hdlkpnester.streamlit.app/",
        "emoji": "🔶"
    },
    "Dave's Door Pricer": {
        "description": "Door pricing and quotation tool",
        "url": "https://daves-door-pricer-app.streamlit.app/",
        "emoji": "💰"
    },
    "ARA Schedule Extract": {
        "description": "Extract and process ARA schedule data",
        "url": "https://arascheduleextract.streamlit.app/",
        "emoji": "📋"
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

st.divider()

# Footer
st.markdown("<p style='text-align: center; color: #999; font-size: 12px;'>© Hardware Direct Limited</p>", unsafe_allow_html=True)
