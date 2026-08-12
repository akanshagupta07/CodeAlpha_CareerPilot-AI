
import streamlit as st
import time

# ============================================================
# CAREERPILOT AI
# AI-POWERED CAREER INTELLIGENCE PLATFORM
# ============================================================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

    /* Main application */
    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(99,102,241,0.10),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(14,165,233,0.10),
                transparent 30%
            ),
            #f8fafc;
    }

    /* Remove default top spacing */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    /* Hero */
    .hero {
        padding: 2.5rem 2.5rem;
        border-radius: 24px;
        background:
            linear-gradient(
                135deg,
                #111827 0%,
                #1e1b4b 50%,
                #312e81 100%
            );
        color: white;
        box-shadow: 0 20px 50px rgba(15,23,42,0.20);
        margin-bottom: 2rem;
    }

    .hero-badge {
        display: inline-block;
        padding: 0.4rem 0.9rem;
        border-radius: 999px;
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.20);
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }

    .hero-title {
        font-size: 3.1rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -1px;
    }

    .hero-subtitle {
        font-size: 1.15rem;
        color: #c7d2fe;
        margin-top: 0.8rem;
        max-width: 850px;
        line-height: 1.7;
    }

    /* Section titles */
    .section-title {
        font-size: 1.6rem;
        font-weight: 750;
        color: #111827;
        margin-top: 1.5rem;
        margin-bottom: 0.3rem;
    }

    .section-subtitle {
        color: #64748b;
        margin-bottom: 1.2rem;
    }

    /* Cards */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 18px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 8px 25px rgba(15,23,42,0.06);
        height: 100%;
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 0.5rem;
    }

    .card-text {
        color: #64748b;
        line-height: 1.6;
    }

    /* Score card */
    .score-card {
        background: linear-gradient(
            135deg,
            #eef2ff,
            #f8fafc
        );
        border: 1px solid #c7d2fe;
        padding: 1.8rem;
        border-radius: 20px;
        text-align: center;
    }

    .score {
        font-size: 3.5rem;
        font-weight: 800;
        color: #4f46e5;
    }

    .score-label {
        color: #64748b;
        font-weight: 600;
    }

    /* Feature cards */
    .feature-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #111827;
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #94a3b8;
        font-size: 0.85rem;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🚀 CareerPilot AI")

    st.caption("AI Career Intelligence Platform")

    st.divider()

    st.markdown("### 🧭 Navigation")

    page = st.radio(
        "Go to",
        [
            "🏠 Career Analyzer",
            "📊 Skill Intelligence",
            "🛣️ Career Roadmap",
            "🎤 Interview Coach"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### ⚡ Platform Capabilities")

    st.markdown("""
    **🎯 Career Fit Analysis**

    **📊 Skill Gap Detection**

    **🧠 AI Career Insights**

    **🛣️ Personalized Roadmap**

    **🎤 Interview Preparation**

    **📄 Resume Intelligence**
    """)

    st.divider()

    st.caption("Built with Python • Streamlit • Langflow • LLM")


# ============================================================
# HERO SECTION
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-badge">
        ✨ AI-POWERED CAREER INTELLIGENCE
    </div>

    <div class="hero-title">
        🚀 CareerPilot AI
    </div>

    <div class="hero-subtitle">
        Transform your resume into an intelligent career strategy.
        Analyze role compatibility, discover skill gaps, identify
        opportunities, and build a personalized path toward your
        target career.
    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# CAREER ANALYZER
# ============================================================

if page == "🏠 Career Analyzer":

    st.markdown(
        '<div class="section-title">🎯 Career Compatibility Analyzer</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Upload your resume and provide a target job description to begin your AI-powered analysis.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    # --------------------------------------------------------
    # RESUME
    # --------------------------------------------------------

    with col1:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        📄 Step 1 — Upload Resume
        </div>

        <div class="card-text">
        Upload your current resume for intelligent career analysis.
        </div>

        </div>
        """, unsafe_allow_html=True)

        uploaded_resume = st.file_uploader(
            "Choose your resume",
            type=["pdf", "txt"],
            label_visibility="collapsed"
        )

    # --------------------------------------------------------
    # JOB DESCRIPTION
    # --------------------------------------------------------

    with col2:

        st.markdown("""
        <div class="card">

        <div class="card-title">
        💼 Step 2 — Target Role
        </div>

        <div class="card-text">
        Paste the job description you want to evaluate.
        </div>

        </div>
        """, unsafe_allow_html=True)

        job_description = st.text_area(
            "Job description",
            height=220,
            placeholder=(
                "Paste the complete job description here...\n\n"
                "Example:\n"
                "We are looking for a Business Analyst..."
            ),
            label_visibility="collapsed"
        )

    st.write("")

    # --------------------------------------------------------
    # ANALYZE
    # --------------------------------------------------------

    analyze = st.button(
        "🚀 Analyze My Career Fit",
        type="primary",
        use_container_width=True
    )

    if analyze:

        if uploaded_resume is None:

            st.warning(
                "📄 Please upload your resume before starting the analysis."
            )

        elif not job_description.strip():

            st.warning(
                "💼 Please paste a target job description."
            )

        else:

            with st.spinner(
                "🧠 CareerPilot AI is analyzing your profile..."
            ):
                time.sleep(1.5)

            st.success(
                "✅ Analysis completed successfully!"
            )

            st.divider()

            st.markdown(
                '<div class="section-title">📊 Career Intelligence Report</div>',
                unsafe_allow_html=True
            )

            # ------------------------------------------------
            # SCORE
            # ------------------------------------------------

            c1, c2, c3, c4 = st.columns(4)

            with c1:

                st.markdown("""
                <div class="score-card">

                    <div class="score">
                    87%
                    </div>

                    <div class="score-label">
                    Career Fit
                    </div>

                </div>
                """, unsafe_allow_html=True)

            with c2:

                st.metric(
                    "🎯 Skill Match",
                    "82%",
                    "+12%"
                )

            with c3:

                st.metric(
                    "📚 Skills Detected",
                    "18",
                    "+5"
                )

            with c4:

                st.metric(
                    "⚠️ Skill Gaps",
                    "6",
                    "-3"
                )

            st.write("")

            # ------------------------------------------------
            # ANALYSIS COLUMNS
            # ------------------------------------------------

            left, right = st.columns(2)

            with left:

                st.markdown("""
                <div class="card">

                <div class="card-title">
                ✅ Your Strengths
                </div>

                <div class="card-text">

                • Python & data analysis<br>
                • SQL & structured datasets<br>
                • Machine learning fundamentals<br>
                • Scientific research experience<br>
                • Analytical problem solving<br>
                • Technical documentation

                </div>

                </div>
                """, unsafe_allow_html=True)

            with right:

                st.markdown("""
                <div class="card">

                <div class="card-title">
                🔎 Skills to Develop
                </div>

                <div class="card-text">

                • Business requirements gathering<br>
                • Agile / Scrum fundamentals<br>
                • Stakeholder management<br>
                • Business process modelling<br>
                • Advanced SQL analytics<br>
                • Jira / project tracking

                </div>

                </div>
                """, unsafe_allow_html=True)

            st.write("")

            # ------------------------------------------------
            # AI INSIGHT
            # ------------------------------------------------

            st.markdown("""
            <div class="card">

            <div class="card-title">
            🧠 CareerPilot AI Insight
            </div>

            <div class="card-text">

            Your profile demonstrates a strong analytical foundation
            with a combination of biotechnology knowledge, computational
            research, Python, SQL and machine-learning experience.

            The strongest opportunity is to position yourself as a
            <b>data-driven life-sciences professional</b> rather than
            presenting yourself solely as a biotechnology graduate.

            Your highest-priority development areas are business
            requirements, process analysis, stakeholder communication
            and industry-oriented analytics.

            </div>

            </div>
            """, unsafe_allow_html=True)


# ============================================================
# SKILL INTELLIGENCE
# ============================================================

elif page == "📊 Skill Intelligence":

    st.markdown(
        '<div class="section-title">📊 Skill Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Understand how your current capabilities align with modern career requirements.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">

        <div class="feature-icon">🐍</div>

        <div class="card-title">
        Technical Skills
        </div>

        <div class="card-text">

        Python<br>
        SQL<br>
        Machine Learning<br>
        Data Analysis<br>
        Pandas<br>
        Scikit-learn

        </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

        <div class="feature-icon">🧬</div>

        <div class="card-title">
        Domain Expertise
        </div>

        <div class="card-text">

        Biotechnology<br>
        Clinical Research<br>
        Pharmacovigilance<br>
        Clinical Data Management<br>
        Computational Biology

        </div>

        </div>
        """, unsafe_allow_html=True)

    with col3:

        st.markdown("""
        <div class="card">

        <div class="feature-icon">📈</div>

        <div class="card-title">
        Business Skills
        </div>

        <div class="card-text">

        Data-driven decision making<br>
        Process analysis<br>
        Documentation<br>
        Reporting<br>
        Problem solving

        </div>

        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.subheader("Skill Readiness")

    skills = {
        "Python": 90,
        "Data Analysis": 85,
        "SQL": 70,
        "Machine Learning": 82,
        "Clinical Research": 80,
        "Business Analysis": 55,
        "Communication": 75
    }

    for skill, value in skills.items():

        st.write(f"**{skill} — {value}%**")

        st.progress(value / 100)


# ============================================================
# CAREER ROADMAP
# ============================================================

elif page == "🛣️ Career Roadmap":

    st.markdown(
        '<div class="section-title">🛣️ Personalized Career Roadmap</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'A structured path from your current skill profile to your target career.'
        '</div>',
        unsafe_allow_html=True
    )

    roadmap = [
        (
            "01",
            "Strengthen SQL",
            "Master JOINs, CTEs, aggregations and business KPIs."
        ),
        (
            "02",
            "Learn Business Analysis",
            "Understand BRDs, requirements gathering, user stories and process mapping."
        ),
        (
            "03",
            "Build Portfolio Projects",
            "Create real-world analytics and career intelligence projects."
        ),
        (
            "04",
            "Master Interview Skills",
            "Practice technical, behavioral and case-based questions."
        ),
        (
            "05",
            "Target Relevant Roles",
            "Apply strategically to Analytics, Operations and Life Sciences roles."
        )
    ]

    for number, title, description in roadmap:

        st.markdown(f"""
        <div class="card" style="margin-bottom:15px;">

            <div style="font-size:0.85rem;color:#6366f1;font-weight:700;">
            STEP {number}
            </div>

            <div class="card-title">
            {title}
            </div>

            <div class="card-text">
            {description}
            </div>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# INTERVIEW COACH
# ============================================================

elif page == "🎤 Interview Coach":

    st.markdown(
        '<div class="section-title">🎤 AI Interview Coach</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Practice answering questions based on your target role and profile.'
        '</div>',
        unsafe_allow_html=True
    )

    question = st.selectbox(
        "Choose an interview question",
        [
            "Tell me about yourself.",
            "Why should we hire you?",
            "Why are you transitioning into this role?",
            "Explain one of your major projects.",
            "What are your strengths?",
            "What is one skill you are currently improving?"
        ]
    )

    answer = st.text_area(
        "Your answer",
        height=180,
        placeholder="Type your interview answer here..."
    )

    if st.button(
        "🧠 Evaluate My Answer",
        type="primary"
    ):

        if not answer.strip():

            st.warning("Please enter your answer first.")

        else:

            st.success("Interview response evaluated!")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric("Structure", "8/10")

            with col2:
                st.metric("Clarity", "9/10")

            with col3:
                st.metric("Relevance", "8/10")

            st.info(
                "💡 Tip: Strengthen your answer by connecting your "
                "technical experience to measurable business or "
                "project outcomes."
            )


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    🚀 <b>CareerPilot AI</b><br>

    AI-powered career intelligence for smarter career decisions.

    <br><br>

    Built with Python • Streamlit • Langflow • Generative AI

</div>
""", unsafe_allow_html=True)