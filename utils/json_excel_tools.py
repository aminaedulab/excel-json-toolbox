# # import streamlit as st
# # import pandas as pd
# # import json
# # import requests
# # from io import BytesIO

# # def json_excel_tool_ui():
# #     st.subheader("📦 JSON ↔ Excel / API → Excel Converter")

# #     tool = st.radio(
# #         "Select a Conversion Type",
# #         ["JSON → Excel", "Excel → JSON", "API → Excel"]
# #     )

# #     # --- JSON → Excel ---
# #     if tool == "JSON → Excel":
# #         uploaded_file = st.file_uploader("Upload JSON File", type=["json"])
# #         json_text = st.text_area("Or paste JSON data manually", height=200, placeholder='[{"id":1,"name":"John"}]')

# #         if uploaded_file or json_text.strip():
# #             try:
# #                 if uploaded_file:
# #                     data = json.load(uploaded_file)
# #                 else:
# #                     data = json.loads(json_text)

# #                 if isinstance(data, dict):
# #                     data = [data]

# #                 df = pd.DataFrame(data)
# #                 st.write("✅ Preview:")
# #                 st.dataframe(df.head())

# #                 output = BytesIO()
# #                 with pd.ExcelWriter(output, engine="openpyxl") as writer:
# #                     df.to_excel(writer, index=False, sheet_name="Data")

# #                 st.download_button(
# #                     "⬇️ Download Excel File",
# #                     output.getvalue(),
# #                     file_name="converted_data.xlsx",
# #                     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
# #                 )
# #                 st.success("✅ JSON converted successfully!")
# #             except Exception as e:
# #                 st.error(f"❌ Error parsing JSON: {e}")

# #     # --- Excel → JSON ---
# #     elif tool == "Excel → JSON":
# #         file = st.file_uploader("Upload Excel File", type=["xlsx"])
# #         if file:
# #             try:
# #                 df = pd.read_excel(file)
# #                 st.write("✅ Excel Preview:")
# #                 st.dataframe(df.head())

# #                 json_data = df.to_dict(orient="records")
# #                 json_str = json.dumps(json_data, indent=2, ensure_ascii=False)

# #                 st.download_button(
# #                     "⬇️ Download JSON File",
# #                     json_str,
# #                     file_name="converted_data.json",
# #                     mime="application/json"
# #                 )
# #                 st.code(json_str[:1000], language="json")
# #                 st.success("✅ Excel converted to JSON successfully!")
# #             except Exception as e:
# #                 st.error(f"❌ Failed to read Excel file: {e}")

# #     # --- API → Excel ---
# #     elif tool == "API → Excel":
# #         api_url = st.text_input("Enter API Endpoint (GET request only):", placeholder="https://api.example.com/data")
# #         auth_header = st.text_area("Optional Authorization Header", placeholder="Bearer your_token_here")

# #         if st.button("Fetch API Data"):
# #             try:
# #                 headers = {}
# #                 if auth_header.strip():
# #                     headers["Authorization"] = auth_header.strip()

# #                 response = requests.get(api_url, headers=headers)
# #                 response.raise_for_status()
# #                 data = response.json()

# #                 if isinstance(data, dict):
# #                     # Flatten top-level list if exists
# #                     if any(isinstance(v, list) for v in data.values()):
# #                         data = next((v for v in data.values() if isinstance(v, list)), [])
# #                     else:
# #                         data = [data]

# #                 df = pd.DataFrame(data)
# #                 st.write("✅ API Data Preview:")
# #                 st.dataframe(df.head())

# #                 output = BytesIO()
# #                 with pd.ExcelWriter(output, engine="openpyxl") as writer:
# #                     df.to_excel(writer, index=False, sheet_name="API_Data")

# #                 st.download_button(
# #                     "⬇️ Download Excel File",
# #                     output.getvalue(),
# #                     file_name="api_data.xlsx",
# #                     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
# #                 )
# #                 st.success("✅ API data converted successfully!")
# #             except Exception as e:
# #                 st.error(f"❌ Error fetching API data: {e}")
# # # streamlit run app.py
# import streamlit as st
# import pandas as pd
# import json
# import requests
# from io import BytesIO

# def json_excel_tool_ui():
#     st.subheader("📦 JSON ↔ Excel / API → Excel / Text → Excel Converter")

#     tool = st.radio(
#         "Select a Conversion Type",
#         ["JSON → Excel", "Excel → JSON", "API → Excel", "Text → Excel"]
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

#     # --- NEW FEATURE: Text → Excel ---
# # --- TEXT → EXCEL ---
#     elif tool == "Text → Excel":
#         txt_file = st.file_uploader("Upload .txt file containing JSON", type=["txt"])

#         if txt_file:
#             try:
#                 # Read raw text
#                 raw_text = txt_file.read().decode("utf-8").strip()

#                 # Try to parse as JSON
#                 data = json.loads(raw_text)

#                 # Extract list from {"data": [...]} or direct list
#                 if isinstance(data, dict) and "data" in data:
#                     data = data["data"]
#                 elif isinstance(data, dict):
#                     data = [data]

#                 # Convert to DataFrame
#                 df = pd.DataFrame(data)

#                 st.write("✅ Preview:")
#                 st.dataframe(df.head())

#                 # Export to Excel
#                 output = BytesIO()
#                 with pd.ExcelWriter(output, engine="openpyxl") as writer:
#                     df.to_excel(writer, index=False, sheet_name="TXT_Data")

#                 st.download_button(
#                     "⬇️ Download Excel File",
#                     output.getvalue(),
#                     file_name="txt_converted.xlsx",
#                     mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#                 )

#                 st.success("✅ Text file converted successfully!")

#             except Exception as e:
#                 st.error(f"❌ Failed to parse text as JSON: {e}")
import streamlit as st
import pandas as pd
import ujson as json
import requests
import os
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
                output.seek(0)

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
    # --- API → Excel ---
    elif tool == "API → Excel":
        api_url = st.text_input("Enter API Endpoint (GET request only):", value="http://localhost:4002/v1/studentmaster/get-studentmaster")
        # Provide a place to paste token, and an option to use server-stored token
        use_server_token = st.checkbox("Use server-stored token (st.secrets or env)", value=False)
        token_input = st.text_area("Paste Bearer token here (if not using server-stored)", height=120, placeholder="eyJhbGciOiJSUzI1NiIsInR5cCI...")

        # Optional: read a token from st.secrets or an env variable if checkbox checked
        server_token = None
        if use_server_token:
            # prefer st.secrets if available, fallback to env var
            server_token = st.secrets.get("API_BEARER_TOKEN") if hasattr(st, "secrets") else None
            if not server_token:
                import os
                server_token = os.environ.get("API_BEARER_TOKEN")
            if not server_token:
                st.warning("No server token found in st.secrets or env var API_BEARER_TOKEN. Paste token manually or set secrets/env var.")
        
        # Choose final token to use
        token = server_token if use_server_token else token_input.strip()

        # Additional request options
        verify_ssl = st.checkbox("Verify SSL (set false for local self-signed/localhost)", value=True)
        timeout_seconds = st.number_input("Request timeout (seconds)", min_value=1, max_value=60, value=15)

        if st.button("Fetch API Data"):
            if not api_url.strip():
                st.error("❌ Please enter API URL.")
            elif not token:
                st.error("❌ Please provide a Bearer token (paste it or enable server-stored token).")
            else:
                try:
                    headers = {
                        "Authorization": f"Bearer {token}",
                        "Accept": "application/json",
                    }

                    # Make the GET request
                    response = requests.get(api_url.strip(), headers=headers, timeout=int(timeout_seconds), verify=bool(verify_ssl))
                    # Raise for HTTP errors (4xx/5xx)
                    response.raise_for_status()

                    # Try parse JSON
                    data = response.json()

                    # Normalize possible shapes:
                    # - If dict with a list under 'data' -> use that
                    # - If dict with any list value -> pick the first list value
                    # - If dict (single object) -> wrap into list
                    # - If list -> use directly
                    def normalize_json(resp):
                        if isinstance(resp, list):
                            return resp
                        if isinstance(resp, dict):
                            if "data" in resp and isinstance(resp["data"], list):
                                return resp["data"]
                            # find first list value
                            for v in resp.values():
                                if isinstance(v, list):
                                    return v
                            return [resp]
                        raise ValueError("Response JSON is not a list or object.")

                    data_list = normalize_json(data)

                    # convert to DataFrame (if empty, show message)
                    if not data_list:
                        st.warning("✅ API returned an empty list.")
                        st.json(data)  # show raw
                    else:
                        df = pd.DataFrame(data_list)
                        st.write("✅ API Data Preview:")
                        st.dataframe(df.head())

                        output = BytesIO()
                        with pd.ExcelWriter(output, engine="openpyxl") as writer:
                            df.to_excel(writer, index=False, sheet_name="API_Data")
                        output.seek(0)

                        # filename suggestion from endpoint
                        suggested_name = api_url.strip().rstrip("/").split("/")[-1] or "api_data"
                        suggested_name = suggested_name + ".xlsx"

                        st.download_button(
                            "⬇️ Download Excel File",
                            output.getvalue(),
                            file_name=suggested_name,
                            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        )
                        st.success("✅ API data converted successfully!")
                except requests.HTTPError as he:
                    st.error(f"❌ HTTP error: {he} — Response: {getattr(he, 'response').text if getattr(he,'response',None) else ''}")
                except requests.RequestException as re:
                    st.error(f"❌ Request failed: {re}")
                except ValueError as ve:
                    st.error(f"❌ JSON parsing/normalization error: {ve}")
                except Exception as e:
                    st.error(f"❌ Unexpected error: {e}")

    # --- TEXT → EXCEL ---
    elif tool == "Text → Excel":
        st.write("Choose input method:")
        choice = st.radio("Input source", ["Upload .txt file", "Server file path (server-side)"])

        def parse_json_from_text(raw_text):
            # Try parsing JSON; handle dict with "data" key or direct list/dict
            try:
                parsed = json.loads(raw_text)
            except json.JSONDecodeError as e:
                raise ValueError(f"Invalid JSON content: {e}")

            # If top-level dict contains a list under "data", use that
            if isinstance(parsed, dict) and "data" in parsed and isinstance(parsed["data"], list):
                return parsed["data"]
            # If parsed is a dict (single object), wrap it to list
            if isinstance(parsed, dict):
                return [parsed]
            # If parsed is a list, return directly
            if isinstance(parsed, list):
                return parsed

            raise ValueError("JSON root must be an object or an array (or contain a 'data' list).")

        if choice == "Upload .txt file":
            txt_file = st.file_uploader("Upload .txt file containing JSON", type=["txt", "json"])
            if txt_file:
                try:
                    raw_text = txt_file.read().decode("utf-8").strip()
                    data_list = parse_json_from_text(raw_text)

                    df = pd.DataFrame(data_list)
                    st.write("✅ Preview:")
                    st.dataframe(df.head())

                    # Prepare Excel in-memory
                    output = BytesIO()
                    with pd.ExcelWriter(output, engine="openpyxl") as writer:
                        df.to_excel(writer, index=False, sheet_name="TXT_Data")
                    output.seek(0)

                    st.download_button(
                        "⬇️ Download Excel File",
                        output.getvalue(),
                        file_name="txt_converted.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
                    st.success("✅ Text file converted successfully!")
                except Exception as e:
                    st.error(f"❌ Failed to parse text as JSON: {e}")

        else:  # Server file path
            st.write("Enter server-side file path (a path accessible to the Streamlit server).")
            server_path = st.text_input("Server file path (e.g., C:\\Users\\Dell\\Downloads\\order.txt or /tmp/order.txt)")

            if st.button("Convert server file to Excel"):
                if not server_path.strip():
                    st.error("❌ Please provide a valid server file path.")
                else:
                    if not os.path.exists(server_path):
                        st.error(f"❌ File not found on server: {server_path}")
                    else:
                        try:
                            with open(server_path, "r", encoding="utf-8") as f:
                                raw_text = f.read().strip()

                            data_list = parse_json_from_text(raw_text)

                            df = pd.DataFrame(data_list)
                            st.write("✅ Preview:")
                            st.dataframe(df.head())

                            # In-memory Excel
                            output = BytesIO()
                            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                                df.to_excel(writer, index=False, sheet_name="TXT_Data")
                            output.seek(0)

                            st.download_button(
                                "⬇️ Download Excel File",
                                output.getvalue(),
                                file_name=os.path.basename(server_path).rsplit(".", 1)[0] + ".xlsx",
                                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                            )
                            st.success(f"✅ Converted server file: {server_path}")
                        except Exception as e:
                            st.error(f"❌ Error reading/parsing server file: {e}")
