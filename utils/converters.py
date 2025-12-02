import streamlit as st
import pandas as pd
from io import BytesIO
import pyperclip

# --- Convert to Number ---
def convert_to_number_ui():
    st.subheader("🔢 Convert Columns to Numbers")

    file = st.file_uploader("Upload Excel File", type=['xlsx'])
    if file:
        df = pd.read_excel(file)
        columns = st.multiselect("Select columns to convert to numbers", list(df.columns))
        if st.button("Convert Columns"):
            for col in columns:
                df[col] = pd.to_numeric(df[col], errors="ignore")

            output = BytesIO()
            with pd.ExcelWriter(output, engine="openpyxl") as writer:
                df.to_excel(writer, index=False)

            st.download_button(
                "⬇️ Download Converted File",
                output.getvalue(),
                file_name="converted_numbers.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
            st.success("✅ Columns converted successfully.")


# --- Comma Separator / String Formatter ---
def comma_string_formatter_ui():
    st.subheader("🧩 Comma / Quote String Converter")

    input_text = st.text_area(
        "Enter values (each in new line or separated by commas)",
        placeholder="Example:\n12345\n67890\nJohn\nDoe",
        height=200
    )

    output_type = st.radio("Choose Output Format", [
        "Comma separated (A, B, C)",
        "Comma separated with single quotes ('A', 'B', 'C')"
    ])

    if st.button("Convert"):
        items = [x.strip() for x in input_text.replace(",", "\n").split("\n") if x.strip()]

        if not items:
            st.warning("⚠️ Please enter some values.")
            return

        if "quotes" in output_type.lower():
            formatted = ", ".join(f"'{x}'" for x in items)
        else:
            formatted = ", ".join(items)

        st.code(formatted, language="text")

        try:
            pyperclip.copy(formatted)
            st.success("✅ Copied to clipboard!")
        except Exception:
            st.warning("⚠️ Clipboard copy not supported in browser — copy manually.")

        st.download_button(
            "⬇️ Download as .txt",
            formatted,
            file_name="formatted_values.txt",
            mime="text/plain"
        )
