import streamlit as st
import requests

st.set_page_config(page_title="POP NOW URL Checker", layout="centered")

st.title("🎁 POP NOW Blind Box Checker")
st.write("Quickly find active POP NOW boxes by scanning a range of box IDs.")

# Default POP NOW base URL
base_url = st.text_input("Base URL", value="https://popnow.popmart.com/box?id=")

start_id = st.number_input("Start ID", min_value=0, value=100000, step=1)
end_id = st.number_input("End ID", min_value=0, value=100010, step=1)

if start_id > end_id:
    st.error("Start ID must be less than or equal to End ID.")

check_button = st.button("🔍 Check URLs")

if check_button:
    st.info("Checking URLs... please wait ⏳")
    working_urls = []

    for box_id in range(start_id, end_id + 1):
        url = f"{base_url}{box_id}"
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                working_urls.append(url)
        except requests.exceptions.RequestException:
            pass  # Skip failed requests

    if working_urls:
        st.success(f"✅ Found {len(working_urls)} working boxes:")
        for link in working_urls:
            st.markdown(f"- [Open Box]({link})")
    else:
        st.warning("😕 No working boxes found in this range.")
