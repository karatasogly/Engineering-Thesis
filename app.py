import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="Universal Decision AI", layout="centered")

# --- INITIALIZE SESSION STATE ---
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "mode" not in st.session_state:
    st.session_state.mode = "welcome"
if "category" not in st.session_state:
    st.session_state.category = None
if "likes" not in st.session_state:
    st.session_state.likes = []
if "data_pool" not in st.session_state:
    st.session_state.data_pool = {}


# --- FETCH REMOTE DATA FROM CLOUD (SANAL VERİ ÇEKME) ---
# We are fetching the data layout dynamically from a live JSON source instead of hardcoding it.
@st.cache_data
def fetch_cloud_data():
    # A public, real-time JSON file simulating our cloud database repository
    url = "https://raw.githubusercontent.com/fatihbaltaci/json-api/main/decision_data.json"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
    except Exception:
        pass

    # Fallback structure if cloud connection drops during testing
    return {
        "Movies 🎬": [{"title": "Inception (Local Fallback)", "desc": "Cloud connection issue.", "img": "🎬"}],
        "Food 🍕": [{"title": "Pizza (Local Fallback)", "desc": "Cloud connection issue.", "img": "🍕"}],
        "Games 🎮": [{"title": "Minecraft (Local Fallback)", "desc": "Cloud connection issue.", "img": "🎮"}]
    }


# Load the dynamic remote data into session
st.session_state.data_pool = fetch_cloud_data()

# --- 1. WELCOME SCREEN ---
if st.session_state.mode == "welcome":
    st.title("🎬 Universal Decision AI")
    st.subheader("Stop arguing, start swiping.")
    st.write("---")

    st.markdown("### 🚀 Choose Your Mode")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("▶️ Go Solo (Single Mode)", use_container_width=True):
            st.session_state.mode = "category_selection"
            st.rerun()

    with col2:
        if st.button("👥 Create a Room (Group Mode)", use_container_width=True):
            st.session_state.mode = "category_selection"
            st.rerun()

    st.write("---")
    st.markdown("### 🔑 Have a Room Code?")
    room_code = st.text_input("Enter 4-digit Room Code:", placeholder="e.g. A79X")
    if st.button("🚪 Join Room", use_container_width=True):
        if room_code:
            st.session_state.mode = "category_selection"
            st.rerun()

# --- 2. CATEGORY SELECTION SCREEN ---
elif st.session_state.mode == "category_selection":
    st.title("📂 Select Category")
    st.write("---")
    st.markdown("What are we deciding on today? *(Data loaded dynamically from Cloud)*")

    for cat in st.session_state.data_pool.keys():
        if st.button(cat, use_container_width=True):
            st.session_state.category = cat
            st.session_state.mode = "swiping"
            st.rerun()

# --- 3. SWIPING DECK SCREEN ---
elif st.session_state.mode == "swiping":
    st.title(f"🃏 Swiping: {st.session_state.category}")
    st.write("---")

    active_items = st.session_state.data_pool[st.session_state.category]

    if st.session_state.current_index < len(active_items):
        current_item = active_items[st.session_state.current_index]

        st.markdown(f"<h1 style='text-align: center; font-size: 80px;'>{current_item['img']}</h1>",
                    unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{current_item['title']}</h3>", unsafe_allow_html=True)
        st.write(f"**Description:** {current_item['desc']}")
        st.write("---")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("❌ Dislike", use_container_width=True, key="dislike"):
                st.session_state.current_index += 1
                st.rerun()
        with col2:
            if st.button("❤️ Like", use_container_width=True, key="like"):
                st.session_state.likes.append(current_item['title'])
                st.session_state.current_index += 1
                st.rerun()
    else:
        st.success("🎉 Review Completed!")
        st.markdown("### 📊 Your Matches / Likes:")
        if st.session_state.likes:
            for liked_item in st.session_state.likes:
                st.write(f"- {liked_item}")
        else:
            st.write("No items liked in this session. 😢")

        st.write("---")
        if st.button("🔄 Restart", use_container_width=True):
            st.session_state.current_index = 0
            st.session_state.likes = []
            st.session_state.category = None
            st.session_state.mode = "welcome"
            st.rerun()