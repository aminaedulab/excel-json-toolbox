import streamlit as st
import pandas as pd
import json
import requests
from io import BytesIO
from openpyxl import Workbook

# -------------------------
# 🌟 PAGE SETUP
# -------------------------
st.set_page_config(page_title="File Converter & API Data Tool", layout="wide")
st.title("📦 File Converter & API → Excel Tool")
st.write("Easily convert between JSON ↔ Excel or fetch API data into Excel.")

# -------------------------
# 🔹 SIDEBAR OPTIONS
# -------------------------
operation = st.sidebar.selectbox(
    "Choose an Operation",
    [
        "JSON → Excel",
        "Excel → JSON",
        "API → Excel"
    ]
)

# -------------------------
# 🧾 JSON → EXCEL
# -------------------------
if operation == "JSON → Excel":
    st.subheader("📤 Convert JSON → Excel")

    uploaded_file = st.file_uploader("Upload JSON File", type=["json"])
    json_text = st.text_area("Or paste JSON data manually", height=200)

    if uploaded_file or json_text.strip():
        try:
            if uploaded_file:
                data = json.load(uploaded_file)
            else:
                data = json.loads(json_text)

            # Handle list or dict
            if isinstance(data, dict):
                data = [data]

            df = pd.DataFrame(data)
            st.write("✅ Preview:")
            st.dataframe(df.head())

            # Save Excel
            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="Data")

            st.download_button(
                label="⬇️ Download Excel",
                data=output.getvalue(),
                file_name="converted_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            st.success("✅ JSON converted successfully!")
        except Exception as e:
            st.error(f"❌ Error parsing JSON: {e}")

# -------------------------
# 📥 EXCEL → JSON
# -------------------------
elif operation == "Excel → JSON":
    st.subheader("📥 Convert Excel → JSON")

    file = st.file_uploader("Upload Excel File", type=["xlsx"])
    if file:
        df = pd.read_excel(file)
        st.write("✅ Excel Preview:")
        st.dataframe(df.head())

        # Convert to JSON
        json_data = df.to_dict(orient="records")
        json_str = json.dumps(json_data, indent=2, ensure_ascii=False)

        st.download_button(
            "⬇️ Download JSON File",
            json_str,
            file_name="converted_data.json",
            mime="application/json"
        )

        st.code(json_str[:1000], language="json")  # show preview
        st.success("✅ Excel converted to JSON successfully!")

# -------------------------
# 🌐 API → EXCEL
# -------------------------
elif operation == "API → Excel":
    st.subheader("🌐 Fetch API Data → Convert to Excel")

    api_url = st.text_input("Enter API Endpoint (GET request only):", placeholder="https://api.example.com/data")
    auth_header = st.text_area("Optional: Add Authorization Header (e.g. Bearer Token)", placeholder="Bearer your_token_here")

    if st.button("Fetch API Data"):
        try:
            headers = {}
            if auth_header:
                headers["Authorization"] = auth_header.strip()

            response = requests.get(api_url, headers=headers)
            response.raise_for_status()

            data = response.json()

            # Handle dict or list
            if isinstance(data, dict):
                if any(isinstance(v, list) for v in data.values()):
                    # Pick first list inside dict if exists
                    list_data = next((v for v in data.values() if isinstance(v, list)), [])
                    df = pd.DataFrame(list_data)
                else:
                    df = pd.DataFrame([data])
            else:
                df = pd.DataFrame(data)

            st.write("✅ API Data Preview:")
            st.dataframe(df.head())

            # Convert to Excel
            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False, sheet_name="API_Data")

            st.download_button(
                label="⬇️ Download Excel File",
                data=output.getvalue(),
                file_name="api_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            st.success("✅ API data converted successfully!")
        except Exception as e:
            st.error(f"❌ Error fetching API data: {e}")
