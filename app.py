
import streamlit as st

from nlp_processor import (
    extract_keywords,
    summarize_text,
    extract_entities
)


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Text Analyzer",
    page_icon="🧠",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0F172A,
        #172554,
        #0F172A
    );
    color: white;
}


/* Main container */

.block-container {
    padding-top: 2rem;
    padding-bottom: 1rem;
}


/* Header */

.header-box {
    text-align: center;
    padding: 35px 20px;
    border-radius: 20px;
    background: linear-gradient(
        135deg,
        #1E3A8A,
        #2563EB
    );
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

.header-box h1 {
    color: white;
    font-size: 42px;
    margin-bottom: 8px;
}

.header-box p {
    color: #DBEAFE;
    font-size: 17px;
}


/* About section */

.about-box {
    background: rgba(30, 41, 59, 0.85);
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #334155;
    margin-bottom: 25px;
}

.about-box h3 {
    color: #60A5FA;
}

.about-box p {
    color: #CBD5E1;
    line-height: 1.6;
}


/* Section titles */

.section-title {
    color: #60A5FA;
    font-size: 25px;
    font-weight: bold;
    margin-top: 25px;
    margin-bottom: 12px;
}


/* Input */

.stTextArea textarea {
    background-color: #1E293B !important;
    color: white !important;
    border: 1px solid #475569 !important;
    border-radius: 12px !important;
}


/* Button */

.stButton button {
    width: 100%;
    background: linear-gradient(
        90deg,
        #2563EB,
        #3B82F6
    );
    color: white;
    border: none;
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
    font-weight: bold;
}

.stButton button:hover {
    background: linear-gradient(
        90deg,
        #1D4ED8,
        #2563EB
    );
}


/* Statistics cards */

[data-testid="stMetric"] {
    background: rgba(30, 41, 59, 0.9);
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #334155;
    text-align: center;
}

[data-testid="stMetricLabel"] {
    color: #94A3B8;
}

[data-testid="stMetricValue"] {
    color: #60A5FA;
}


/* Result boxes */

.result-box {
    background: rgba(30, 41, 59, 0.9);
    border: 1px solid #334155;
    border-radius: 15px;
    padding: 22px;
    margin-bottom: 20px;
    line-height: 1.7;
}


/* Keyword chips */

.keyword {
    display: inline-block;
    background: #1D4ED8;
    color: white;
    padding: 7px 13px;
    margin: 5px;
    border-radius: 20px;
    font-size: 14px;
}


/* Entity cards */

.entity {
    display: inline-block;
    background: #0F766E;
    color: white;
    padding: 8px 14px;
    margin: 5px;
    border-radius: 10px;
}

.entity-label {
    color: #99F6E4;
    font-size: 12px;
}


/* Footer */

.footer {
    text-align: center;
    margin-top: 50px;
    padding: 25px;
    border-top: 1px solid #334155;
    color: #94A3B8;
    font-size: 14px;
}

.footer strong {
    color: #60A5FA;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("""
<div class="header-box">

<h1>🧠 AI Text Analyzer</h1>

<p>
Transform long text into meaningful insights using
Natural Language Processing
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# ABOUT WEBSITE
# --------------------------------------------------

st.markdown("""
<div class="about-box">

<h3>✨ About Our Website</h3>

<p>
AI Text Analyzer is an NLP-powered web application that
analyzes articles and paragraphs automatically. It can
generate a concise summary, identify important keywords,
and detect named entities such as people, organizations,
locations, and dates.
</p>

</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TEXT INPUT
# --------------------------------------------------

st.markdown(
    '<div class="section-title">📝 Enter Your Text</div>',
    unsafe_allow_html=True
)

text = st.text_area(
    "Paste your article or paragraph below:",
    height=280,
    placeholder="Paste your article, paragraph, news content, or any text here..."
)


# --------------------------------------------------
# SUMMARY SETTINGS
# --------------------------------------------------

number_of_sentences = st.slider(
    "Number of sentences in summary:",
    min_value=1,
    max_value=10,
    value=3
)


# --------------------------------------------------
# ANALYZE BUTTON
# --------------------------------------------------

if st.button("🔍 Analyze Text"):

    if text.strip() == "":
        st.warning("Please enter some text before analyzing.")

    else:

        # NLP processing

        keywords = extract_keywords(
            text,
            10
        )

        summary = summarize_text(
            text,
            number_of_sentences
        )

        entities = extract_entities(
            text
        )


        # --------------------------------------------------
        # STATISTICS
        # --------------------------------------------------

        original_words = len(text.split())
        summary_words = len(summary.split())


        st.markdown(
            '<div class="section-title">📊 Text Statistics</div>',
            unsafe_allow_html=True
        )


        col1, col2, col3 = st.columns(3)


        with col1:

            st.metric(
                "Original Words",
                original_words
            )


        with col2:

            st.metric(
                "Summary Words",
                summary_words
            )


        with col3:

            st.metric(
                "Keywords",
                len(keywords)
            )


        # --------------------------------------------------
        # SUMMARY
        # --------------------------------------------------

        st.markdown(
            '<div class="section-title">📝 Generated Summary</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="result-box">
            {summary}
            </div>
            """,
            unsafe_allow_html=True
        )


        # --------------------------------------------------
        # KEYWORDS
        # --------------------------------------------------

        st.markdown(
            '<div class="section-title">🔑 Important Keywords</div>',
            unsafe_allow_html=True
        )


        if keywords:

            keyword_html = ""

            for keyword in keywords:

                keyword_html += (
                    f'<span class="keyword">{keyword}</span>'
                )

            st.markdown(
                keyword_html,
                unsafe_allow_html=True
            )

        else:

            st.info("No keywords found.")


        # --------------------------------------------------
        # NAMED ENTITIES
        # --------------------------------------------------

        st.markdown(
            '<div class="section-title">🏷️ Named Entities</div>',
            unsafe_allow_html=True
        )


        if entities:

            entity_html = ""

            for entity, label in entities:

                entity_html += f"""
                <span class="entity">
                    {entity}
                    <span class="entity-label">
                        ({label})
                    </span>
                </span>
                """

            st.markdown(
                entity_html,
                unsafe_allow_html=True
            )

        else:

            st.info(
                "No named entities were detected in this text."
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("""
<div class="footer">

<p>
<strong>“Turning text into insights with the power of NLP.”</strong>
</p>

<p>
🧠 AI Text Analyzer &nbsp; • &nbsp;
Built with Python, NLP & Streamlit
</p>

<p>
© 2026 AbiNLP • AI Text Analysis Project
</p>

</div>
""", unsafe_allow_html=True)

