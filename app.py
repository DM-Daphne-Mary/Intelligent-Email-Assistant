import streamlit as st

from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import generate_summary
from utils import save_reply


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Intelligent Email Assistant",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ---------- MAIN PAGE ---------- */

.stApp {
    background:
        radial-gradient(circle at top right,
        rgba(139, 92, 246, 0.18),
        transparent 28%),
        radial-gradient(circle at bottom left,
        rgba(59, 130, 246, 0.10),
        transparent 30%),
        linear-gradient(135deg, #f8faff 0%, #f3f0ff 100%);
}

.block-container {
    max-width: 1350px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}


/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #111936 0%,
            #172554 55%,
            #111936 100%
        );
}

[data-testid="stSidebar"] * {
    color: white;
}

.sidebar-logo {
    text-align: center;
    font-size: 55px;
    margin-top: 10px;
}

.sidebar-title {
    text-align: center;
    font-size: 25px;
    font-weight: 800;
    line-height: 1.25;
}

.sidebar-subtitle {
    text-align: center;
    color: #cbd5e1 !important;
    font-size: 13px;
    line-height: 1.6;
    margin-top: 10px;
    margin-bottom: 20px;
}

.sidebar-heading {
    font-size: 17px;
    font-weight: 800;
    margin-bottom: 10px;
}

.sidebar-feature {
    padding: 11px 13px;
    margin: 7px 0;
    border-radius: 11px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.08);
    font-size: 14px;
}

.sidebar-feature:hover {
    background: rgba(139,92,246,0.25);
}

.ollama-box {
    margin-top: 22px;
    padding: 18px 12px;
    text-align: center;
    border-radius: 16px;
    background:
        linear-gradient(
            135deg,
            rgba(124,58,237,0.32),
            rgba(37,99,235,0.22)
        );
    border: 1px solid rgba(255,255,255,0.15);
}

.ollama-icon {
    font-size: 42px;
}

.ollama-title {
    font-size: 16px;
    font-weight: 800;
    margin-top: 5px;
}

.ollama-text {
    color: #cbd5e1 !important;
    font-size: 12px;
    line-height: 1.5;
    margin-top: 8px;
}


/* ---------- HERO ---------- */

.hero {
    padding: 35px 40px;
    margin-bottom: 28px;
    border-radius: 24px;

    background:
        linear-gradient(
            120deg,
            #ffffff 0%,
            #f5f3ff 55%,
            #eef2ff 100%
        );

    border: 1px solid #e2e8f0;

    box-shadow:
        0 15px 40px rgba(79,70,229,0.10);
}

.hero-badge {
    display: inline-block;
    background: #dcfce7;
    color: #15803d;
    padding: 7px 14px;
    border-radius: 30px;
    font-size: 12px;
    font-weight: 800;
    margin-bottom: 15px;
}

.hero-title {
    color: #172554;
    font-size: 40px;
    line-height: 1.2;
    font-weight: 900;
}

.hero-title span {
    color: #6d28d9;
}

.hero-text {
    color: #64748b;
    font-size: 17px;
    line-height: 1.6;
    margin-top: 12px;
}

.hero-small {
    color: #7c3aed;
    font-size: 13px;
    font-weight: 700;
    margin-top: 15px;
}


/* ---------- SECTION HEADINGS ---------- */

.section-title {
    color: #172554;
    font-size: 25px;
    font-weight: 900;
    margin-top: 8px;
}

.section-subtitle {
    color: #64748b;
    font-size: 14px;
    margin-top: 3px;
    margin-bottom: 17px;
}


/* ---------- STREAMLIT INPUTS ---------- */

.stTextInput label,
.stTextArea label,
.stSelectbox label {
    color: #1e293b !important;
    font-weight: 700 !important;
    font-size: 14px !important;
}

.stTextInput input {
    border-radius: 11px !important;
    border: 1px solid #cbd5e1 !important;
    background: white !important;
    color: #0f172a !important;
}

.stTextArea textarea {
    border-radius: 11px !important;
    border: 1px solid #cbd5e1 !important;
    background: white !important;
    color: #0f172a !important;
}

.stSelectbox [data-baseweb="select"] > div {
    border-radius: 11px !important;
    background: white !important;
}


/* ---------- BUTTON ---------- */

.stButton > button {
    width: 100%;
    min-height: 52px;

    border: none;
    border-radius: 12px;

    background:
        linear-gradient(
            90deg,
            #4338ca,
            #7c3aed,
            #9333ea
        );

    color: white !important;

    font-size: 16px;
    font-weight: 800;

    box-shadow:
        0 8px 22px rgba(124,58,237,0.25);

    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);

    box-shadow:
        0 12px 28px rgba(124,58,237,0.35);

    border: none;
}


/* ---------- FEATURE CARDS ---------- */

.feature-card {
    min-height: 155px;
    padding: 20px;
    border-radius: 18px;
    background: white;
    border: 1px solid #e2e8f0;

    box-shadow:
        0 7px 20px rgba(15,23,42,0.06);
}

.feature-icon {
    font-size: 31px;
}

.feature-title {
    color: #172554;
    font-size: 16px;
    font-weight: 800;
    margin-top: 9px;
}

.feature-text {
    color: #64748b;
    font-size: 13px;
    line-height: 1.5;
    margin-top: 7px;
}


/* ---------- RESULTS ---------- */

.results-title {
    color: #172554;
    font-size: 29px;
    font-weight: 900;
    margin-top: 35px;
    margin-bottom: 15px;
}

.result-section-title {
    color: #172554;
    font-size: 21px;
    font-weight: 800;
    margin-top: 22px;
    margin-bottom: 8px;
}


/* ---------- METRIC ---------- */

[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 18px;

    box-shadow:
        0 6px 18px rgba(15,23,42,0.06);
}

[data-testid="stMetricLabel"] {
    color: #64748b;
}

[data-testid="stMetricValue"] {
    color: #5b21b6;
}


/* ---------- EXPANDER ---------- */

[data-testid="stExpander"] {
    background: white;
    border: 1px solid #e2e8f0 !important;
    border-radius: 15px !important;
}


/* ---------- SUCCESS ---------- */

[data-testid="stAlert"] {
    border-radius: 13px;
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 12px;
    line-height: 1.8;
    margin-top: 45px;
    padding-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        '<div class="sidebar-logo">📧</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-title">Intelligent<br>Email Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-subtitle">'
        'AI-Powered Customer Email<br>'
        'Analysis & Reply Generation'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        '<div class="sidebar-heading">🚀 Features</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">🎯 Intent Detection</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">🔍 Similar Email Retrieval</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">🤖 AI Reply Generation</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">🎨 Tone Improvement</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">📝 Conversation Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-feature">💾 Reply Saving</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
<div class="ollama-box">
<div class="ollama-icon">🦙</div>
<div class="ollama-title">Ollama-Inspired AI</div>
<div class="ollama-text">
Intelligent customer support workflow using
large language model capabilities.
</div>
</div>
""",
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.caption(
        "24CS2506\n\nBuilding Applications using GPT-4"
    )


# =========================================================
# HERO SECTION
# =========================================================

st.markdown(
    """
<div class="hero">
<div class="hero-badge">● AI SYSTEM READY</div>
<div class="hero-title">
Welcome to <span>Intelligent Email Assistant</span> ✨
</div>
<div class="hero-text">
Analyze customer emails, understand their intent,
retrieve similar previous conversations and generate
professional context-aware responses.
</div>
<div class="hero-small">
🦙 Intelligent LLM-based Customer Support Assistant
</div>
</div>
""",
    unsafe_allow_html=True
)


# =========================================================
# CUSTOMER INPUT SECTION
# =========================================================

st.markdown(
    '<div class="section-title">👤 Customer Email Details</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-subtitle">'
    'Enter the customer information and email content below.'
    '</div>',
    unsafe_allow_html=True
)


col1, col2 = st.columns(2)


with col1:

    customer_name = st.text_input(
        "👤 Customer Name",
        placeholder="e.g. John Doe"
    )


with col2:

    subject = st.text_input(
        "✉️ Email Subject",
        placeholder="e.g. Delivery Delay"
    )


customer_email = st.text_area(
    "💬 Customer Email",
    placeholder=(
        "Type the customer's email here...\n\n"
        "Example: My order has not arrived yet "
        "and I would like an update."
    ),
    height=145
)


tone = st.selectbox(
    "✨ Select Reply Tone",
    [
        "Friendly",
        "Formal",
        "Empathetic"
    ]
)


generate_button = st.button(
    "✈️ Analyze Email & Generate Reply",
    use_container_width=True
)


# =========================================================
# FEATURE CARDS
# =========================================================

st.markdown("<br>", unsafe_allow_html=True)


f1, f2, f3, f4 = st.columns(4)


with f1:

    st.markdown(
        """
<div class="feature-card">
<div class="feature-icon">🎯</div>
<div class="feature-title">Smart Intent Detection</div>
<div class="feature-text">
Automatically understand the main purpose of the
customer's email.
</div>
</div>
""",
        unsafe_allow_html=True
    )


with f2:

    st.markdown(
        """
<div class="feature-card">
<div class="feature-icon">🔍</div>
<div class="feature-title">Similar Email Retrieval</div>
<div class="feature-text">
Search previous customer interactions and retrieve
the most relevant conversation.
</div>
</div>
""",
        unsafe_allow_html=True
    )


with f3:

    st.markdown(
        """
<div class="feature-card">
<div class="feature-icon">🤖</div>
<div class="feature-title">AI Reply Generation</div>
<div class="feature-text">
Generate a professional response using customer
context and historical replies.
</div>
</div>
""",
        unsafe_allow_html=True
    )


with f4:

    st.markdown(
        """
<div class="feature-card">
<div class="feature-icon">📝</div>
<div class="feature-title">Summarize & Save</div>
<div class="feature-text">
Create a short conversation summary and save the
final customer response.
</div>
</div>
""",
        unsafe_allow_html=True
    )


# =========================================================
# PROCESS CUSTOMER EMAIL
# =========================================================

if generate_button:

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not customer_name.strip():

        st.warning(
            "⚠️ Please enter the Customer Name."
        )

    elif not subject.strip():

        st.warning(
            "⚠️ Please enter the Email Subject."
        )

    elif not customer_email.strip():

        st.warning(
            "⚠️ Please enter the Customer Email."
        )

    else:

        try:

            st.markdown("<br>", unsafe_allow_html=True)

            progress_bar = st.progress(0)

            status_message = st.empty()


            # =================================================
            # STEP 1 - INTENT
            # =================================================

            status_message.info(
                "🎯 Step 1 of 5 — Detecting customer intent..."
            )

            intent = detect_intent(
                customer_email
            )

            progress_bar.progress(20)


            # =================================================
            # STEP 2 - RETRIEVAL
            # =================================================

            status_message.info(
                "🔍 Step 2 of 5 — Searching similar previous emails..."
            )

            previous_email, previous_reply = (
                retrieve_similar_email(
                    customer_email
                )
            )

            progress_bar.progress(40)


            # =================================================
            # STEP 3 - GENERATE REPLY
            # =================================================

            status_message.info(
                "🤖 Step 3 of 5 — Generating professional AI reply..."
            )

            generated_reply = generate_reply(
                customer_name,
                customer_email,
                previous_reply,
                intent
            )

            progress_bar.progress(60)


            # =================================================
            # STEP 4 - TONE
            # =================================================

            status_message.info(
                f"🎨 Step 4 of 5 — Applying {tone} tone..."
            )

            improved_reply = improve_tone(
                generated_reply,
                tone
            )

            progress_bar.progress(80)


            # =================================================
            # STEP 5 - SUMMARY
            # =================================================

            status_message.info(
                "📝 Step 5 of 5 — Generating conversation summary..."
            )

            summary = generate_summary(
                customer_email
            )

            progress_bar.progress(100)


            # =================================================
            # SAVE
            # =================================================

            save_reply(
                customer_email,
                improved_reply,
                intent
            )


            status_message.empty()
            progress_bar.empty()


            st.success(
                "✅ Email analyzed and reply generated successfully!"
            )


            # =================================================
            # RESULTS HEADER
            # =================================================

            st.markdown(
                '<div class="results-title">'
                '📊 AI Analysis Results'
                '</div>',
                unsafe_allow_html=True
            )


            # =================================================
            # METRICS
            # =================================================

            metric1, metric2, metric3 = st.columns(3)


            with metric1:

                st.metric(
                    "🎯 Detected Intent",
                    intent
                )


            with metric2:

                st.metric(
                    "🎨 Selected Tone",
                    tone
                )


            with metric3:

                st.metric(
                    "⚡ Processing Status",
                    "Completed"
                )


            # =================================================
            # SUMMARY
            # =================================================

            st.markdown(
                '<div class="result-section-title">'
                '📝 Conversation Summary'
                '</div>',
                unsafe_allow_html=True
            )

            st.info(summary)


            # =================================================
            # SIMILAR INTERACTION
            # =================================================

            st.markdown(
                '<div class="result-section-title">'
                '🔍 Most Similar Previous Interaction'
                '</div>',
                unsafe_allow_html=True
            )


            with st.expander(
                "📂 View Retrieved Historical Conversation",
                expanded=True
            ):

                st.markdown(
                    "#### 📩 Previous Customer Email"
                )

                st.write(
                    previous_email
                )

                st.markdown(
                    "#### 💬 Previous Support Reply"
                )

                st.write(
                    previous_reply
                )


            # =================================================
            # ORIGINAL AI REPLY
            # =================================================

            st.markdown(
                '<div class="result-section-title">'
                '🤖 AI Generated Reply'
                '</div>',
                unsafe_allow_html=True
            )

            st.text_area(
                "Original AI Response",
                value=generated_reply,
                height=230,
                disabled=True
            )


            # =================================================
            # FINAL TONE IMPROVED REPLY
            # =================================================

            st.markdown(
                f'<div class="result-section-title">'
                f'✨ Final {tone} Reply'
                f'</div>',
                unsafe_allow_html=True
            )

            final_reply = st.text_area(
                "Final Customer Response",
                value=improved_reply,
                height=270
            )


            # =================================================
            # SAVED MESSAGE
            # =================================================

            st.success(
                "💾 Final reply saved successfully to "
                "outputs/generated_reply.txt"
            )


            # =================================================
            # CUSTOMER DETAILS
            # =================================================

            with st.expander(
                "👤 View Original Customer Details"
            ):

                detail1, detail2 = st.columns(2)

                with detail1:

                    st.write(
                        "**Customer Name:**"
                    )

                    st.write(
                        customer_name
                    )

                with detail2:

                    st.write(
                        "**Email Subject:**"
                    )

                    st.write(
                        subject
                    )

                st.write(
                    "**Customer Email:**"
                )

                st.write(
                    customer_email
                )


        # =====================================================
        # ERROR HANDLING
        # =====================================================

        except Exception as error:

            st.error(
                "❌ An error occurred while processing "
                "the customer email."
            )

            st.error(
                str(error)
            )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
<div class="footer">
Intelligent Email Assistant • Experiment 3<br>
24CS2506 – Building Applications using GPT-4
</div>
""",
    unsafe_allow_html=True
)