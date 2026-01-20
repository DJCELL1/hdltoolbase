# HDL Tools Hub

Central hub for all Hardware Direct internal Streamlit applications.

## Overview

This landing page provides a single point of reference for accessing all HDL Streamlit tools and applications.

## Features

- Hardware Direct themed interface
- Easy navigation to all internal tools
- Consistent branding across applications
- Simple configuration for adding new apps

## Running the Hub

```bash
streamlit run streamlit_home.py --server.port 8501
```

## Adding New Applications

1. Open `streamlit_home.py`
2. Add a new entry to the `apps` dictionary:

```python
"Your App Name": {
    "description": "What your app does",
    "url": "http://localhost:PORT",
    "emoji": "🚀"
}
```

3. Run your app on the specified port:

```bash
streamlit run your_app.py --server.port PORT
```

## Theme

The Hardware Direct theme is configured in `.streamlit/config.toml`:
- Primary Color: `#F47920` (Hardware Direct Orange)
- Clean, professional design
- Consistent across all applications

## Current Applications

- **PO Wizard**: Multi-supplier Purchase Order Builder for Cin7
