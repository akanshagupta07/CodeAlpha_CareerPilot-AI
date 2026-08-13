
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="CareerPilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CUSTOM STYLING
# ============================================================

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #f8fafc 0%,
            #eef2ff 50%,
            #f8fafc 100%
        );
    }

    /* Main container */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Hero section */
    .hero {
        padding: 2.5rem 2rem;
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            #111827,
            #312e81
        );
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 15px 40px rgba(49, 46, 129, 0.20);
    }

    .hero h1 {
        font-size: 3.2rem;
        margin-bottom: 0.5rem;
        font-weight: 800;
    }

    .hero p {
        font-size: 1.15rem;
        opacity: 0.9;
        margin-bottom: 0.5rem;
    }

    .hero-small {
        font-size: 0.95rem;
        opacity: 0.75;
    }

    /* Section cards */
    .card {
        background: white;
        padding: 1.5rem;
        border-radius: 18px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 8px 25px rgba(15, 23, 42, 0.06);
        margin-bottom: 1rem;
    }

    /* Feature cards */
    .feature {
        background: white;
        padding: 1.3rem;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        min-height: 145px;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .feature h3 {
        margin-top: 0;
        font-size: 1.05rem;
    }

    .feature p {
        color: #64748b;
        font-size: 0.9rem;
    }

    /* Metrics */
    .metric-card {
        background: white;
        border-radius: 16px;
        padding: 1.3rem;
        text-align: center;
        border: 1px solid #e5e7eb;
        box-shadow: 0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .metric-number {
        font-size: 2rem;
        font-weight: 800;
        color: #312e81;
    }

    .metric-label {
        color: #64748b;
        font-size: 0.85rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        padding-top: 2rem;
        font-size: 0.85rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <h1>🚀 CareerPilot AI</h1>

        <p>
            AI-Powered Career Intelligence Platform
        </p>

        <div class="hero-small">
            Resume Intelligence • Career Fit • Skill Gap Analysis •
            Job Readiness • Personalized Recommendations
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# INTRODUCTION
# ============================================================

st.markdown(
    """
    <div class="card">

    <h2>🎯 Navigate Your Career With Intelligence</h2>

    <p>
    CareerPilot AI analyzes your resume against a target role,
    identifies your strengths and skill gaps, and provides
    actionable recommendations to improve your job readiness.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# FEATURES
# ============================================================

st.subheader("✨ What CareerPilot AI Can Do")

feature_col1, feature_col2, feature_col3 = st.columns(3)

with feature_col1:
    st.markdown(
        """
        <div class="feature">
            <h3>📄 Resume Intelligence</h3>
            <p>
            Analyze your resume and extract career-relevant
            information for role matching.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col2:
    st.markdown(
        """
        <div class="feature">
            <h3>🎯 Career Fit Analysis</h3>
            <p>
            Compare your profile against a target job
            description and identify alignment.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col3:
    st.markdown(
        """
        <div class="feature">
            <h3>🧠 Skill Gap Detection</h3>
            <p>
            Discover missing skills and understand what
            you should improve for your target role.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")

feature_col4, feature_col5, feature_col6 = st.columns(3)

with feature_col4:
    st.markdown(
        """
        <div class="feature">
            <h3>📈 Job Readiness</h3>
            <p>
            Evaluate your current preparation and identify
            areas requiring improvement.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col5:
    st.markdown(
        """
        <div class="feature">
            <h3>💡 Recommendations</h3>
            <p>
            Receive practical recommendations based on
            your resume and target role.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with feature_col6:
    st.markdown(
        """
        <div class="feature">
            <h3>🗺️ Career Roadmap</h3>
            <p>
            Transform identified skill gaps into a structured
            career development direction.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ============================================================
# INPUT SECTION
# ============================================================

st.write("")
st.divider()

st.header("🔍 Start Your Career Analysis")

left, right = st.columns(2)

with left:

    st.markdown("### 📄 Upload Resume")

    uploaded_resume = st.file_uploader(
        "Upload your resume",
        type=["txt", "pdf"],
        help="Upload a TXT or PDF version of your resume."
    )

with right:

    st.markdown("### 🎯 Target Role")

    job_description = st.text_area(
        "Paste the target job description",
        height=220,
        placeholder=(
            "Paste the complete job description here...\n\n"
            "Example:\n"
            "Data Analyst\n"
            "Required Skills: Python, SQL, Power BI..."
        )
    )

# ============================================================
# ANALYSIS BUTTON
# ============================================================

st.write("")

analyze = st.button(
    "🚀 Analyze My Career",
    type="primary",
    use_container_width=True
)

# ============================================================
# RESULT SECTION
# ============================================================

if analyze:

    if uploaded_resume is None:

        st.warning(
            "📄 Please upload your resume before starting the analysis."
        )

    elif not job_description.strip():

        st.warning(
            "🎯 Please paste a target job description."
        )

    else:

        st.success(
            "✅ Resume and job description successfully received!"
        )

        st.divider()

        st.header("📊 Career Intelligence Dashboard")

        # Demo metrics for the current MVP
        metric1, metric2, metric3, metric4 = st.columns(4)

        with metric1:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-number">82%</div>
                    <div class="metric-label">Career Fit</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with metric2:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-number">14/18</div>
                    <div class="metric-label">Skills Matched</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with metric3:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-number">78%</div>
                    <div class="metric-label">Job Readiness</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with metric4:
            st.markdown(
                """
                <div class="metric-card">
                    <div class="metric-number">4</div>
                    <div class="metric-label">Skill Gaps</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.write("")

        # Tabs
        tab1, tab2, tab3, tab4 = st.tabs(
            [
                "🎯 Career Fit",
                "🧠 Skills",
                "💡 Recommendations",
                "🗺️ Roadmap"
            ]
        )

        with tab1:

            st.subheader("Career Fit Analysis")

            st.progress(0.82)

            st.write(
                "Your profile demonstrates strong alignment with "
                "the target role based on the submitted resume "
                "and job description."
            )

            st.info(
                "The current version demonstrates the CareerPilot "
                "analysis interface. The Langflow workflow can be "
                "connected here for live LLM-generated analysis."
            )

        with tab2:

            st.subheader("Skill Analysis")

            col1, col2 = st.columns(2)

            with col1:

                st.markdown("### ✅ Matching Skills")

                st.success("Python")
                st.success("SQL")
                st.success("Machine Learning")
                st.success("Data Analysis")
                st.success("Problem Solving")

            with col2:

                st.markdown("### ⚠️ Potential Skill Gaps")

                st.warning("Advanced Power BI")
                st.warning("Cloud Analytics")
                st.warning("Advanced Statistics")
                st.warning("Domain-specific tools")

        with tab3:

            st.subheader("Personalized Recommendations")

            st.markdown(
                """
                **1. Strengthen role-specific technical skills**

                Focus on the technologies and tools explicitly
                mentioned in the target job description.

                **2. Improve resume alignment**

                Highlight measurable achievements and keywords
                relevant to the target position.

                **3. Build one targeted portfolio project**

                Demonstrate practical application of the skills
                required by the target role.

                **4. Prepare for role-specific interviews**

                Practice technical, behavioral and
                case-based questions.
                """
            )

        with tab4:

            st.subheader("Suggested Career Roadmap")

            st.markdown(
                """
                ### Phase 1 — Foundation
                Build strong fundamentals in the missing skills.

                ### Phase 2 — Practical Application
                Complete targeted projects demonstrating those skills.

                ### Phase 3 — Resume Optimization
                Align your resume with target job requirements.

                ### Phase 4 — Interview Preparation
                Practice technical and behavioral questions.

                ### Phase 5 — Job Application
                Apply strategically to roles matching your profile.
                """
            )

# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.divider()

st.subheader("🛠️ Technology Stack")

tech1, tech2, tech3, tech4, tech5 = st.columns(5)

with tech1:
    st.markdown("**🐍 Python**")

with tech2:
    st.markdown("**⚡ Streamlit**")

with tech3:
    st.markdown("**🧠 Generative AI**")

with tech4:
    st.markdown("**🔗 Langflow**")

with tech5:
    st.markdown("**🐙 GitHub**")

# ============================================================
# PROJECT INFORMATION
# ============================================================

st.divider()

about1, about2 = st.columns(2)

with about1:

    st.markdown(
        """
        ### 📌 About the Project

        CareerPilot AI was developed as an AI-focused career
        intelligence prototype to demonstrate how Generative AI,
        structured workflows and Python applications can support
        personalized career decision-making.
        """
    )

with about2:

    st.markdown(
        """
        ### 🎓 Project Context

        Developed as part of the CodeAlpha AI internship,
        combining Python application development, LLM workflow
        orchestration and career analytics.
        """
    )

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

    🚀 <strong>CareerPilot AI</strong><br>

    AI-Powered Career Intelligence Platform<br><br>

    Built with Python • Streamlit • Generative AI • Langflow

    </div>
    """,
    unsafe_allow_html=True
)