import streamlit as st
import pandas as pd

# 页面配置：使其看起来像移动 App
st.set_page_config(page_title="AlphaQubit 2 Vocab", layout="centered")

# 注入 CSS 优化 iPhone 体验
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        height: 4em;
        font-size: 20px;
        border-radius: 15px;
        background-color: #007AFF; /* 苹果蓝 */
        color: white;
    }
    .word-card {
        padding: 30px;
        background-color: #f0f2f6;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 模拟数据（你可以替换为连接 Google Sheets 的逻辑）
# df = st.connection("gsheets", type=GSheetsConnection).read()
data = {
    "Word": ["Fault-tolerant", "QEC", "Decoder", "Surface code", "Scalable"],
    "Definition": ["容错", "量子纠错", "解码器", "表面码", "可扩展"],
    "Context": ["Fault-tolerant quantum computing is the goal.", "QEC bridges the gap.", "AlphaQubit 2 is a neural decoder.", "Optimized for surface codes.", "A scalable architecture."]
}
df = pd.DataFrame(data)

# 初始化状态
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'show' not in st.session_state:
    st.session_state.show = False

# 单词卡片显示
current_word = df.iloc[st.session_state.count]

st.write(f"进度: {st.session_state.count + 1} / {len(df)}")

st.markdown(f"""
    <div class="word-card">
        <h1 style='font-size: 40px;'>{current_word['Word']}</h1>
    </div>
    """, unsafe_allow_html=True)

if st.button("查看释义 / Show Meaning"):
    st.session_state.show = True

if st.session_state.show:
    st.success(f"**释义:** {current_word['Definition']}")
    st.info(f"**文中语境:** {current_word['Context']}")

if st.button("下一个 / Next"):
    st.session_state.count = (st.session_state.count + 1) % len(df)
    st.session_state.show = False
    st.rerun()
