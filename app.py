import streamlit as st
import json

with open("output/report.json", "r", encoding="utf-8") as file:
    bugs = json.load(file)

high = sum(1 for bug in bugs if bug["severity"] == "HIGH")
medium = sum(1 for bug in bugs if bug["severity"] == "MEDIUM")
low = sum(1 for bug in bugs if bug["severity"] == "LOW")

st.title("🐞 CodeBugFinder Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total", len(bugs))
col2.metric("HIGH", high)
col3.metric("MEDIUM", medium)
col4.metric("LOW", low)

st.subheader("Detected Issues")

st.dataframe(bugs)

uploaded_file = st.file_uploader(
    "Upload a Python File",
    type=["py"]
)
severity_filter = st.selectbox(
    "Filter Severity",
    ["ALL", "HIGH", "MEDIUM", "LOW"]
)

import pandas as pd

df = pd.DataFrame(bugs)

severity_counts = df["severity"].value_counts()

st.subheader("Severity Distribution")
st.bar_chart(severity_counts)

uploaded_file = st.file_uploader(
    "Upload Python File",
    type=["py"]
)

import tempfile

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".py"
    ) as tmp:

        tmp.write(uploaded_file.getvalue())
        temp_path = tmp.name

from scanner.bug_detector import scan_file


if uploaded_file is not None:

    bugs = scan_file(temp_path)

    st.subheader("Scan Results")

    if bugs:
        st.dataframe(bugs)
    else:
        st.success("No bugs found!")

import json

with open("output/report.json", "r", encoding="utf-8") as f:
    json_data = f.read()

st.download_button(
    label="📥 Download JSON Report",
    data=json_data,
    file_name="report.json",
    mime="application/json"
)

with open("output/report.csv", "r", encoding="utf-8") as f:
    csv_data = f.read()

st.download_button(
    label="📥 Download CSV Report",
    data=csv_data,
    file_name="report.csv",
    mime="text/csv"
)

search = st.text_input("Search Issue")
filtered_bugs = [
    bug for bug in bugs
    if search.lower() in bug["issue"].lower()
]
severity_filter = st.selectbox(
    "Filter Severity",
    ["ALL", "HIGH", "MEDIUM", "LOW"]
)
if severity_filter == "ALL":
    filtered_bugs = bugs
else:
    filtered_bugs = [
        bug for bug in bugs
        if bug["severity"] == severity_filter
    ]

st.dataframe(filtered_bugs)

search = st.text_input("Search Issue")

if search:
    filtered_bugs = [
        bug for bug in filtered_bugs
        if search.lower() in bug["issue"].lower()
    ]
import pandas as pd

df = pd.DataFrame(bugs)

st.subheader("Severity Distribution")

st.bar_chart(
    df["severity"].value_counts()
)
rules = {
    "CBF001":"Hardcoded credentials",
    "CBF002":"Infinite loop risk",
    "CBF003":"Debug statement",
    "CBF004":"Empty exception handler",
    "CBF005":"Pending TODO",
    "CBF006":"Hardcoded API key",
    "CBF007":"Bare exception",
    "CBF008":"Wildcard import"
}
{
    "id":"CBF001",
    "issue":"Hardcoded Password",
    "fix":"Use environment variables"
}
