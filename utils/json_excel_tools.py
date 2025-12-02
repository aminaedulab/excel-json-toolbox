# import streamlit as st
# import pandas as pd
# import json
# import requests
# from io import BytesIO

# def json_excel_tool_ui():
#     st.subheader("📦 JSON ↔ Excel / API → Excel Converter")

#     tool = st.radio(
#         "Select a Conversion Type",
#         ["JSON → Excel", "Excel → JSON", "API → Excel"]
#     )

#     # --- JSON → Excel ---
#     if tool == "JSON → Excel":
#         uploaded_file = st.file_uploader("Upload JSON File", type=["json"])
#         json_text = st.text_area("Or paste JSON data manually", height=200, placeholder='[{"id":1,"name":"John"}]')

#         if uploaded_file or json_text.strip():
#             try:
#                 if uploaded_file:
#                     data = json.load(uploaded_file)
#                 else:
#                     data = json.loads(json_text)

#                 if isinstance(data, dict):
#                     data = [data]

#                 df = pd.DataFrame(data)
#                 st.write("✅ Preview:")
#                 st.dataframe(df.head())

#                 output = BytesIO()
#                 with pd.ExcelWriter(output, engine="openpyxl") as writer:
#                     df.to_excel(writer, index=False, sheet_name="Data")

#                 st.download_button(
#                     "⬇️ Download Excel File",
#                     output.getvalue(),
#                     file_name="converted_data.xlsx",
#                     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                 )
#                 st.success("✅ JSON converted successfully!")
#             except Exception as e:
#                 st.error(f"❌ Error parsing JSON: {e}")

#     # --- Excel → JSON ---
#     elif tool == "Excel → JSON":
#         file = st.file_uploader("Upload Excel File", type=["xlsx"])
#         if file:
#             try:
#                 df = pd.read_excel(file)
#                 st.write("✅ Excel Preview:")
#                 st.dataframe(df.head())

#                 json_data = df.to_dict(orient="records")
#                 json_str = json.dumps(json_data, indent=2, ensure_ascii=False)

#                 st.download_button(
#                     "⬇️ Download JSON File",
#                     json_str,
#                     file_name="converted_data.json",
#                     mime="application/json"
#                 )
#                 st.code(json_str[:1000], language="json")
#                 st.success("✅ Excel converted to JSON successfully!")
#             except Exception as e:
#                 st.error(f"❌ Failed to read Excel file: {e}")

#     # --- API → Excel ---
#     elif tool == "API → Excel":
#         api_url = st.text_input("Enter API Endpoint (GET request only):", placeholder="https://api.example.com/data")
#         auth_header = st.text_area("Optional Authorization Header", placeholder="Bearer your_token_here")

#         if st.button("Fetch API Data"):
#             try:
#                 headers = {}
#                 if auth_header.strip():
#                     headers["Authorization"] = auth_header.strip()

#                 response = requests.get(api_url, headers=headers)
#                 response.raise_for_status()
#                 data = response.json()

#                 if isinstance(data, dict):
#                     # Flatten top-level list if exists
#                     if any(isinstance(v, list) for v in data.values()):
#                         data = next((v for v in data.values() if isinstance(v, list)), [])
#                     else:
#                         data = [data]

#                 df = pd.DataFrame(data)
#                 st.write("✅ API Data Preview:")
#                 st.dataframe(df.head())

#                 output = BytesIO()
#                 with pd.ExcelWriter(output, engine="openpyxl") as writer:
#                     df.to_excel(writer, index=False, sheet_name="API_Data")

#                 st.download_button(
#                     "⬇️ Download Excel File",
#                     output.getvalue(),
#                     file_name="api_data.xlsx",
#                     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                 )
#                 st.success("✅ API data converted successfully!")
#             except Exception as e:
#                 st.error(f"❌ Error fetching API data: {e}")
# # streamlit run app.py
import streamlit as st
import pandas as pd
import json
import requests
from io import BytesIO

def json_excel_tool_ui():
    st.subheader("📦 JSON ↔ Excel / API → Excel / Text → Excel Converter")

    tool = st.radio(
        "Select a Conversion Type",
        ["JSON → Excel", "Excel → JSON", "API → Excel", "Text → Excel"]
    )

    # --- JSON → Excel ---
    if tool == "JSON → Excel":
        uploaded_file = st.file_uploader("Upload JSON File", type=["json"])
        json_text = st.text_area("Or paste JSON data manually", height=200, placeholder='[{"id":1,"name":"John"}]')

        if uploaded_file or json_text.strip():
            try:
                if uploaded_file:
                    data = json.load(uploaded_file)
                else:
                    data = json.loads(json_text)

                if isinstance(data, dict):
                    data = [data]

                df = pd.DataFrame(data)
                st.write("✅ Preview:")
                st.dataframe(df.head())

                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False, sheet_name="Data")

                st.download_button(
                    "⬇️ Download Excel File",
                    output.getvalue(),
                    file_name="converted_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                st.success("✅ JSON converted successfully!")
            except Exception as e:
                st.error(f"❌ Error parsing JSON: {e}")

    # --- Excel → JSON ---
    elif tool == "Excel → JSON":
        file = st.file_uploader("Upload Excel File", type=["xlsx"])
        if file:
            try:
                df = pd.read_excel(file)
                st.write("✅ Excel Preview:")
                st.dataframe(df.head())

                json_data = df.to_dict(orient="records")
                json_str = json.dumps(json_data, indent=2, ensure_ascii=False)

                st.download_button(
                    "⬇️ Download JSON File",
                    json_str,
                    file_name="converted_data.json",
                    mime="application/json"
                )
                st.code(json_str[:1000], language="json")
                st.success("✅ Excel converted to JSON successfully!")
            except Exception as e:
                st.error(f"❌ Failed to read Excel file: {e}")

    # --- API → Excel ---
    elif tool == "API → Excel":
        api_url = st.text_input("Enter API Endpoint (GET request only):", placeholder="https://api.example.com/data")
        auth_header = st.text_area("Optional Authorization Header", placeholder="Bearer your_token_here")

        if st.button("Fetch API Data"):
            try:
                headers = {}
                if auth_header.strip():
                    headers["Authorization"] = auth_header.strip()

                response = requests.get(api_url, headers=headers)
                response.raise_for_status()
                data = response.json()

                if isinstance(data, dict):
                    # Flatten top-level list if exists
                    if any(isinstance(v, list) for v in data.values()):
                        data = next((v for v in data.values() if isinstance(v, list)), [])
                    else:
                        data = [data]

                df = pd.DataFrame(data)
                st.write("✅ API Data Preview:")
                st.dataframe(df.head())

                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False, sheet_name="API_Data")

                st.download_button(
                    "⬇️ Download Excel File",
                    output.getvalue(),
                    file_name="api_data.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
                st.success("✅ API data converted successfully!")
            except Exception as e:
                st.error(f"❌ Error fetching API data: {e}")

    # --- NEW FEATURE: Text → Excel ---
# --- TEXT → EXCEL ---
    elif tool == "Text → Excel":
        txt_file = st.file_uploader("Upload .txt file containing JSON", type=["txt"])

        if txt_file:
            try:
                # Read raw text
                raw_text = txt_file.read().decode("utf-8").strip()

                # Try to parse as JSON
                data = json.loads(raw_text)

                # Extract list from {"data": [...]} or direct list
                if isinstance(data, dict) and "data" in data:
                    data = data["data"]
                elif isinstance(data, dict):
                    data = [data]

                # Convert to DataFrame
                df = pd.DataFrame(data)

                st.write("✅ Preview:")
                st.dataframe(df.head())

                # Export to Excel
                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    df.to_excel(writer, index=False, sheet_name="TXT_Data")

                st.download_button(
                    "⬇️ Download Excel File",
                    output.getvalue(),
                    file_name="txt_converted.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

                st.success("✅ Text file converted successfully!")

            except Exception as e:
                st.error(f"❌ Failed to parse text as JSON: {e}")
