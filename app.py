import streamlit as st
from datetime import datetime
from agent import run_agent

st.set_page_config(
    page_title="Personal Healthcare Navigator",
    layout="wide"
)

st.markdown(
    """
    <style>

    .stApp {
        background:
        linear-gradient(
            135deg,
            #050505,
            #0b1114,
            #061817
        );
        color:white;
    }

    .wave-lines {
        position:fixed;
        left:0;
        bottom:0;
        width:100%;
        height:45%;
        pointer-events:none;
        z-index:0;
        overflow:hidden;
    }

    .wave-lines::before {

        content:"";

        position:absolute;

        width:150%;

        height:220px;

        left:-25%;

        bottom:25%;

        border-top:2px solid rgba(0,229,255,0.25);

        border-radius:50%;

        transform:rotate(-12deg);

        filter:blur(0.5px);

    }

    .wave-lines::after {

        content:"";

        position:absolute;

        width:150%;

        height:180px;

        right:-30%;

        bottom:5%;

        border-top:2px solid rgba(0,255,170,0.22);

        border-radius:50%;

        transform:rotate(12deg);

        filter:blur(0.5px);

    }

    .block-container {

        position:relative;

        z-index:5;

    }

    h1 {

        color:#00E5FF;

        font-size:46px;

        font-weight:800;

    }

    h2,h3 {

        color:#00FFAA;

        font-weight:700;

    }

    p {

        color:#D8F3FF;

        font-size:17px;

    }

    .stTextInput input {

        background:rgba(10,15,20,0.9);

        color:white;

        border:2px solid #00E5FF;

        border-radius:12px;

    }

    .stButton button {

        background:
        linear-gradient(
            90deg,
            #0066FF,
            #00D4A8
        );

        color:white;

        border:none;

        border-radius:15px;

        height:50px;

        width:240px;

        font-size:18px;

        font-weight:bold;

    }

    .stButton button:hover {

        background:
        linear-gradient(
            90deg,
            #00D4A8,
            #0066FF
        );

    }

    .stAlert {

        background:rgba(10,20,25,0.9);

        border-left:5px solid #00FFAA;

        border-radius:12px;

    }

    footer {

        visibility:hidden;

    }

    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="wave-lines"></div>
    """,
    unsafe_allow_html=True
)

st.title(
    "Personal Healthcare Navigator"
)

st.write(
    "A healthcare AI system that investigates your medical questions, "
    "analyzes trusted medical evidence, generates recommendations, "
    "and explains the reasoning behind them."
)

st.markdown("---")

condition = st.text_input(
    "Medical Condition (e.g. COPD, Diabetes)"
)

question = st.text_input(
    "Your Question"
)
if st.button("Start Investigation"):

    if condition and question:

        with st.spinner("Investigating trusted medical sources..."):

            result = run_agent(
                condition,
                question
            )

        # -----------------------------
        # Retrieved Evidence
        # -----------------------------
        st.subheader(
            "📚 Retrieved Evidence & Source Analysis"
        )

        if result["evidence"]:

            for item in result["evidence"]:

                with st.expander(item["source"]):

                    st.write(item["evidence"])

                    st.caption(
                        f"Source: {item['url']}"
                    )

        else:

            st.warning(
                "No relevant evidence was found."
            )

        # -----------------------------
        # Recommendation
        # -----------------------------
        st.subheader(
            "💡 AI-Generated Recommendation"
        )

        st.success(
            result["recommendation"]["recommendation"]
        )

        # -----------------------------
        # Confidence
        # -----------------------------
        st.subheader(
            "📊 Confidence Level"
        )

        confidence = result["recommendation"]["confidence"]

        if confidence == "High":
            st.success(f"Confidence: {confidence}")

        elif confidence == "Medium":
            st.warning(f"Confidence: {confidence}")

        else:
            st.error(f"Confidence: {confidence}")

        # -----------------------------
        # Explainable AI
        # -----------------------------
        st.subheader(
            "🔍 Explainable AI"
        )

        st.info(
            result["explanation"]
        )

        # -----------------------------
        # Summary
        # -----------------------------
        st.subheader(
            "📋 Investigation Summary"
        )

        st.write(
            f"**Condition:** {result['condition']}"
        )

        st.write(
            f"**Question:** {result['question']}"
        )

        st.caption(
            "Generated at: " +
            datetime.now().strftime("%d %B %Y, %I:%M %p")
        )

    else:

        st.warning(
            "Please enter both the medical condition and your question."
        )