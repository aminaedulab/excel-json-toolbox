import streamlit as st
import pandas as pd
from io import BytesIO

def vlookup_tool_ui():
    st.subheader("🔍 Excel VLOOKUP Utility")

    # 📁 File uploaders
    file_main = st.file_uploader("Upload Main Excel (Target File)", type=['xlsx'], key="main")
    file_lookup = st.file_uploader("Upload Lookup Excel (Reference File)", type=['xlsx'], key="lookup")

    if file_main and file_lookup:
        # 📄 Show uploaded file names
        st.markdown(f"**📂 Main File Uploaded:** `{file_main.name}`")
        st.markdown(f"**📘 Lookup File Uploaded:** `{file_lookup.name}`")

        # Read Excel files
        df_main = pd.read_excel(file_main)
        df_lookup = pd.read_excel(file_lookup)

        # 👀 Preview data
        st.write("### 👀 Preview - Main File")
        st.dataframe(df_main.head())

        st.write("### 👀 Preview - Lookup File")
        st.dataframe(df_lookup.head())

        # 🔑 Key column selections
        main_key = st.selectbox("🔑 Select Key Column (Main File)", df_main.columns)
        lookup_key = st.selectbox("🔍 Select Matching Column (Lookup File)", df_lookup.columns)
        lookup_values = st.multiselect("📊 Select Columns to Fetch from Lookup File", df_lookup.columns)

        convert_numbers = st.checkbox("🔢 Convert matching columns to numeric before merging")

        # 🚀 Run merge
        if st.button("🚀 Run VLOOKUP"):
            try:
                if convert_numbers:
                    df_main[main_key] = pd.to_numeric(df_main[main_key], errors="ignore")
                    df_lookup[lookup_key] = pd.to_numeric(df_lookup[lookup_key], errors="ignore")

                # Track original columns
                original_columns = set(df_main.columns)

                # Perform merge
                merged = pd.merge(
                    df_main,
                    df_lookup[[lookup_key] + lookup_values],
                    left_on=main_key,
                    right_on=lookup_key,
                    how="left"
                )

                # ✅ Keep key column if same name, otherwise drop lookup_key
                if lookup_key != main_key:
                    merged.drop(columns=[lookup_key], inplace=True, errors="ignore")

                # Detect newly added columns
                new_columns = [col for col in merged.columns if col not in original_columns]

                st.success("✅ VLOOKUP completed successfully!")

                # 🆕 Show newly added columns
                st.markdown("### 🆕 Newly Added Columns from Lookup File:")
                if new_columns:
                    st.write(", ".join(new_columns))
                else:
                    st.write("No new columns added.")

                # ✨ Highlight new columns
                def highlight_new_cols(col):
                    if col.name in new_columns:
                        return ['background-color: #fff8dc'] * len(col)
                    return [''] * len(col)

                st.write("### 🔎 Merged Preview (New columns highlighted)")
                st.dataframe(merged.head(20).style.apply(highlight_new_cols))

                # 💾 Prepare Excel for download
                output = BytesIO()
                with pd.ExcelWriter(output, engine="openpyxl") as writer:
                    merged.to_excel(writer, index=False)

                st.download_button(
                    "⬇️ Download Result Excel",
                    output.getvalue(),
                    file_name=f"vlookup_result_{file_main.name.replace('.xlsx', '')}.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

            except Exception as e:
                st.error(f"❌ Error: {e}")
                
