# import streamlit as st
# import pandas as pd
# import json
# import requests
# from io import BytesIO
# import zipfile
# from openpyxl import load_workbook
# from openpyxl.styles import PatternFill
# import pyperclip  # ✅ for clipboard copy (make sure to `pip install pyperclip`)

# st.set_page_config(page_title="Excel & JSON Utility", layout="wide")
# st.title("🧾 Excel & JSON Converter & Analyzer")
# st.write("Split, merge, convert, and analyze Excel or JSON data easily.")

# operation = st.sidebar.selectbox(
#     "Choose an Operation",
#     [
#         "Split Excel",
#         "Merge Excel",
#         "JSON → Excel",
#         "Excel → JSON",
#         "Find Duplicates",
#         "API → Excel",
#         "VLOOKUP",
#         "Convert to Number",
#         "Comma Separator / String Formatter"  # ✅ NEW FEATURE
#     ]
# )

# # Helper: Save dataframe to Excel (openpyxl)
# def to_excel(df):
#     output = BytesIO()
#     with pd.ExcelWriter(output, engine="openpyxl") as writer:
#         df.to_excel(writer, index=False, sheet_name="Sheet1")
#     return output.getvalue()


# # --- Split Excel ---
# if operation == "Split Excel":
#     file = st.file_uploader("Upload Excel File", type=['xlsx'])
#     entries_per_file = st.number_input("Entries per file", min_value=1, value=100)

#     if st.button("Split File") and file:
#         df = pd.read_excel(file)
#         chunks = [df[i:i + entries_per_file] for i in range(0, len(df), entries_per_file)]
#         zip_buffer = BytesIO()

#         with zipfile.ZipFile(zip_buffer, "w") as zipf:
#             for idx, chunk in enumerate(chunks, 1):
#                 part_output = BytesIO()
#                 with pd.ExcelWriter(part_output, engine="openpyxl") as writer:
#                     chunk.to_excel(writer, index=False, sheet_name="Sheet1")
#                 zipf.writestr(f"split_part_{idx}.xlsx", part_output.getvalue())

#         st.download_button(
#             "⬇️ Download All Parts (ZIP)",
#             zip_buffer.getvalue(),
#             file_name="split_files.zip",
#             mime="application/zip"
#         )
#         st.success(f"✅ Split into {len(chunks)} files and ready for download.")


# # --- Find Duplicates ---
# elif operation == "Find Duplicates":
#     file = st.file_uploader("Upload Excel File", type=['xlsx'])
#     if file:
#         df = pd.read_excel(file)
#         columns = st.multiselect("Select columns to check for duplicates", list(df.columns))
#         if st.button("Find Duplicates") and columns:
#             dups = df[df.duplicated(subset=columns, keep=False)]
#             st.write(f"Found {len(dups)} duplicate rows based on {columns}.")

#             # Highlight duplicates in selected columns
#             output = BytesIO()
#             with pd.ExcelWriter(output, engine="openpyxl") as writer:
#                 df.to_excel(writer, index=False, sheet_name="Sheet1")
#                 workbook = writer.book
#                 sheet = writer.sheets["Sheet1"]

#                 yellow_fill = PatternFill(start_color="FFFF00", end_color="FFFF00", fill_type="solid")

#                 for col in columns:
#                     col_idx = df.columns.get_loc(col) + 1
#                     duplicate_vals = df[df.duplicated(subset=[col], keep=False)][col].unique()
#                     for row_idx, val in enumerate(df[col], start=2):
#                         if val in duplicate_vals:
#                             sheet.cell(row=row_idx, column=col_idx).fill = yellow_fill

#             st.download_button(
#                 "⬇️ Download Highlighted Excel",
#                 output.getvalue(),
#                 file_name="highlighted_duplicates.xlsx",
#                 mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             )


# # --- Convert to Number ---
# elif operation == "Convert to Number":
#     file = st.file_uploader("Upload Excel File", type=['xlsx'])
#     if file:
#         df = pd.read_excel(file)
#         columns = st.multiselect("Select columns to convert to numbers", list(df.columns))
#         if st.button("Convert Columns"):
#             for col in columns:
#                 df[col] = pd.to_numeric(df[col], errors="ignore")

#             output = BytesIO()
#             with pd.ExcelWriter(output, engine="openpyxl") as writer:
#                 df.to_excel(writer, index=False, sheet_name="Sheet1")

#             st.download_button(
#                 "⬇️ Download Converted File",
#                 output.getvalue(),
#                 file_name="converted_numbers.xlsx",
#                 mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#             )
#             st.success("✅ Selected columns converted to numeric type!")


# # --- NEW FEATURE: Comma Separator / String Formatter ---
# elif operation == "Comma Separator / String Formatter":
#     st.subheader("🧩 Comma or Quote String Converter")

#     input_text = st.text_area(
#         "Enter values (numbers, words, emails, etc.)",
#         placeholder="Example:\n12345\n67890\nJohn\nDoe",
#         height=200
#     )

#     separator_type = st.radio(
#         "Choose output format:",
#         [
#             "Comma separated (A, B, C)",
#             "Comma separated with single quotes ('A', 'B', 'C')"
#         ]
#     )

#     if st.button("Convert"):
#         # Split input by newlines, commas, or spaces
#         items = [x.strip() for x in input_text.replace(",", "\n").split("\n") if x.strip()]

#         if not items:
#             st.warning("⚠️ Please enter at least one value.")
#         else:
#             if "quotes" in separator_type.lower():
#                 formatted = ", ".join(f"'{x}'" for x in items)
#             else:
#                 formatted = ", ".join(items)

#             st.code(formatted, language="text")

#             # Copy to clipboard
#             try:
#                 pyperclip.copy(formatted)
#                 st.success("✅ Copied to clipboard!")
#             except Exception:
#                 st.warning("⚠️ Clipboard copy not supported in browser — please copy manually.")

#             # Add download option
#             st.download_button(
#                 "⬇️ Download as .txt",
#                 formatted,
#                 file_name="formatted_values.txt",
#                 mime="text/plain"
#             )
import streamlit as st
from utils.vlookup_tool import vlookup_tool_ui
from utils.converters import convert_to_number_ui, comma_string_formatter_ui
from utils.file_utils import split_excel_ui, find_duplicates_ui,merge_excel_ui
from utils.json_excel_tools import json_excel_tool_ui  # ✅ NEW MODULE

st.set_page_config(page_title="Excel & JSON Utility", layout="wide")
st.title("🧾 Excel & JSON Converter & Analyzer")
st.write("Easily split, merge, convert, validate, and format your data — for developers, analysts, and engineers.")

operation = st.sidebar.selectbox(
    "Choose an Operation",
    [
        "Split Excel",
        "Find Duplicates",
        "Merge Excel",
        "Convert to Number",
        "Comma Separator / String Formatter",
        "VLOOKUP",
        "JSON ↔ Excel / API → Excel",  # ✅ NEW OPTION
        # "SQL / Mongo Validator"
    ]
)

if operation == "Split Excel":
    split_excel_ui()

elif operation == "Find Duplicates":
    find_duplicates_ui()

elif operation == "Convert to Number":
    convert_to_number_ui()

elif operation == "Comma Separator / String Formatter":
    comma_string_formatter_ui()

elif operation == "VLOOKUP":
    vlookup_tool_ui()

elif operation == "JSON ↔ Excel / API → Excel":
    json_excel_tool_ui()

if operation == "Merge Excel":
    merge_excel_ui()

# elif operation == "SQL / Mongo Validator":
#     sql_validator_ui()
