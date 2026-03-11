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
    "Word": [
        "Fault-tolerant", "QEC", "Decoder", "Surface code", "Color code", 
        "Scalable", "Real-time", "Distance (d)", "Logical error", "Physical qubit", 
        "Syndrome", "Parity", "Encoding", "Neural network", "Inference", 
        "Latency", "Throughput", "Threshold", "Superconducting", "Topological", 
        "Clustering", "Bit-flip", "Phase-flip", "Stabilizer", "Ancilla", 
        "Transformer", "MLP", "Transformer encoder", "Backbone", "Weight optimization", 
        "Syndrome extraction", "Measurement noise", "Correlated errors", "Monte Carlo", "Stim", 
        "MWPM", "Union-Find", "Heuristic", "Generalization", "In-distribution", 
        "Out-of-distribution", "Fine-tuning", "Pre-training", "Tokenization", "Attention mechanism", 
        "Layer normalization", "Embedding", "Quantization", "FPGAs", "Accelerators"
    ],
    "Definition": [
        "容錯（フォールトトレラント）", "量子エラー訂正", "デコーダ", "表面符号", "カラー符号", 
        "スケーラブル（拡張性）", "リアルタイム", "コード距離", "論理エラー", "物理量子ビット", 
        "シンドローム（症候）", "パリティ", "符号化", "ニューラルネットワーク", "推論", 
        "遅延（レイテンシ）", "スループット", "閾値", "超伝導", "トポロジカル", 
        "クラスタリング", "ビット反転", "位相反転", "スタビライザ", "補助量子ビット", 
        "Transformer", "多層パーセプトロン", "Transformerエンコーダ", "バックボーン", "重み最適化", 
        "シンドローム抽出", "測定ノイズ", "相関エラー", "モンテカルロ法", "Stim（シミュレータ）", 
        "最小重み完全マッチング", "Union-Find法", "ヒューリスティック", "汎化", "分布内", 
        "分布外", "ファインチューニング", "事前学習", "トークン化", "注意機構", 
        "層正規化", "埋め込み", "量子化", "FPGA", "アクセラレータ"
    ],
    "Context": [
        "Fault-tolerant quantum computing will require error rates far below physical qubits.",
        "QEC bridges the gap between physical and logical error rates.",
        "AlphaQubit 2 is a neural-network decoder that achieves near-optimal rates.",
        "It achieves near-optimal logical error rates for surface codes.",
        "It is orders of magnitude faster for the colour code than other decoders.",
        "Decoders must be simultaneously fast, accurate, and scalable.",
        "We demonstrate real-time decoding faster than 1 microsecond per cycle.",
        "Experiments were conducted up to distance 11 (d=11) on accelerators.",
        "The goal of QEC is to minimize the logical error rate.",
        "Errors occur on physical qubits due to environmental noise.",
        "The decoder receives a syndrome as input to predict errors.",
        "Parity measurements are performed repeatedly to detect faults.",
        "Topological codes provide a robust way of encoding quantum information.",
        "A neural network is used to learn the mapping from syndrome to error.",
        "The inference time must be shorter than the cycle time.",
        "The decoder must have low latency to avoid a backlog of syndromes.",
        "Throughput refers to the number of syndromes decoded per second.",
        "The performance improves when the error rate is below the threshold.",
        "Realistic noise models for superconducting qubits were used for testing.",
        "Topological quantum codes like surface codes are highly robust.",
        "Clustering of errors is a common challenge in large-scale QEC.",
        "The decoder corrects both bit-flip (X) and phase-flip (Z) errors.",
        "Phase-flip errors are a primary source of noise in quantum systems.",
        "Stabilizer measurements are the basis for syndrome generation.",
        "Ancilla qubits are used to measure the parity of data qubits.",
        "AlphaQubit 2 is based on a Transformer-like architecture.",
        "MLP (Multi-Layer Perceptron) layers are used for feature processing.",
        "The Transformer encoder processes the sequence of syndromes.",
        "The backbone network extracts features from the measurement data.",
        "Thresholds can be improved by flagged weight optimization.",
        "Syndrome extraction is performed at each cycle of the QEC process.",
        "The model is robust to measurement noise in the syndrome data.",
        "Correlated errors can significantly degrade QEC performance.",
        "Monte Carlo simulations were used to evaluate the logical error rate.",
        "Stim is a fast simulator for quantum error correction circuits.",
        "MWPM is a classical algorithm used as a baseline for comparison.",
        "Union-Find is a fast heuristic decoder for topological codes.",
        "Heuristic decoders trade off accuracy for speed.",
        "The model shows strong generalization to different noise levels.",
        "Evaluation on in-distribution data matches training conditions.",
        "Performance on out-of-distribution noise shows the model's robustness.",
        "Fine-tuning can improve performance on specific hardware noise.",
        "Pre-training on synthetic data allows the model to learn error patterns.",
        "The syndrome data is converted into a sequence through tokenization.",
        "The attention mechanism allows the model to focus on relevant errors.",
        "Layer normalization is used to stabilize the training process.",
        "Each syndrome position is mapped to a high-dimensional embedding.",
        "Model quantization can further reduce the inference latency.",
        "FPGAs are potential targets for low-latency implementation.",
        "Commercial accelerators like GPUs/TPUs were used for benchmarking."
    ]
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
