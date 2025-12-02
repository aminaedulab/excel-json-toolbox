import streamlit as st
import sqlparse
import json

def sql_validator_ui():
    st.subheader("🧠 SQL / Mongo Validator & Formatter")

    query_type = st.radio("Select Query Type:", ["SQL", "MongoDB"])

    query_input = st.text_area(
        "Paste your query below 👇",
        height=250,
        placeholder="Example: SELECT * FROM users WHERE id = 10;"
    )

    if st.button("Validate & Format"):
        if query_type == "SQL":
            validate_sql(query_input)
        else:
            validate_mongo(query_input)


def validate_sql(query: str):
    if not query.strip():
        st.warning("⚠️ Please enter an SQL query.")
        return

    try:
        formatted = sqlparse.format(query, reindent=True, keyword_case="upper")
        st.code(formatted, language="sql")

        if not query.strip().endswith(";"):
            st.warning("⚠️ Missing semicolon at the end.")
        if query.count("(") != query.count(")"):
            st.warning("⚠️ Unbalanced parentheses detected.")
        if query.count("'") % 2 != 0:
            st.warning("⚠️ Unmatched quotes detected.")

        st.success("✅ SQL syntax appears valid (basic validation).")

    except Exception as e:
        st.error(f"❌ SQL Error: {e}")


def validate_mongo(query: str):
    if not query.strip():
        st.warning("⚠️ Please enter a Mongo query.")
        return

    try:
        json_part = query[query.index("{"):]
        json_part = json_part.replace("'", '"')
        json.loads(json_part)
        st.success("✅ MongoDB JSON syntax looks valid.")
        st.code(json.dumps(json.loads(json_part), indent=2), language="json")

    except Exception as e:
        st.error(f"❌ Invalid Mongo syntax: {e}")
