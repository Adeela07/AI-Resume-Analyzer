import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.text_similarity import calculate_similarity
from utils.skill_recommendations import get_recommendation


# ==========================================
# PAGE SETTINGS
# ==========================================

st.set_page_config(
    page_title="AI Job & Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ==========================================
# TITLE
# ==========================================

st.title("📄 AI Job & Resume Analyzer")

st.write(
    "Upload your resume and compare it with a job description "
    "to identify matching skills, missing skills, and text similarity."
)


# ==========================================
# INPUT FORM
# ==========================================

with st.form("resume_analysis_form"):

    st.subheader("📄 Upload Resume")

    resume = st.file_uploader(
        "Upload your resume PDF",
        type=["pdf"]
    )

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=300
    )

    analyze = st.form_submit_button(
        "🔍 Analyze Resume",
        use_container_width=True
    )


# ==========================================
# ANALYSIS
# ==========================================

if analyze:

    # --------------------------------------
    # Show that the button was clicked
    # --------------------------------------

    st.info("Analysis started...")


    # --------------------------------------
    # Check resume
    # --------------------------------------

    if resume is None:

        st.error(
            "❌ Please upload your resume PDF."
        )

        st.stop()


    # --------------------------------------
    # Check job description
    # --------------------------------------

    if not job_description.strip():

        st.error(
            "❌ Please paste a job description."
        )

        st.stop()


    try:

        # ==================================
        # STEP 1: EXTRACT RESUME TEXT
        # ==================================

        with st.spinner("Reading your resume..."):

            resume_text = extract_text_from_pdf(
                resume
            )


        if not resume_text.strip():

            st.error(
                "❌ No readable text was found in the PDF."
            )

            st.stop()


        # ==================================
        # STEP 2: EXTRACT SKILLS
        # ==================================

        with st.spinner("Extracting skills..."):

            resume_skills = extract_skills(
                resume_text
            )

            job_skills = extract_skills(
                job_description
            )


        # ==================================
        # STEP 3: CREATE SETS
        # ==================================

        resume_skill_set = set(
            resume_skills
        )

        job_skill_set = set(
            job_skills
        )


        # ==================================
        # STEP 4: MATCHING SKILLS
        # ==================================

        matched_skills = (
            resume_skill_set
            .intersection(job_skill_set)
        )


        # ==================================
        # STEP 5: MISSING SKILLS
        # ==================================

        missing_skills = (
            job_skill_set
            - resume_skill_set
        )


        # ==================================
        # STEP 6: SKILL MATCH SCORE
        # ==================================

        if job_skill_set:

            skill_match = (
                len(matched_skills)
                / len(job_skill_set)
            ) * 100

        else:

            skill_match = 0


        # ==================================
        # STEP 7: TEXT SIMILARITY
        # ==================================

        with st.spinner(
            "Calculating text similarity..."
        ):

            similarity_score = calculate_similarity(
                resume_text,
                job_description
            )


        # ==================================
        # RESULTS
        # ==================================

        st.success(
            "✅ Resume analysis completed!"
        )

        st.divider()

        st.header("📊 Resume Analysis")


        # ==================================
        # SCORES
        # ==================================

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Skill Match",
                f"{skill_match:.2f}%"
            )

        with col2:

            st.metric(
                "Text Similarity",
                f"{similarity_score:.2f}%"
            )


        # ==================================
        # MATCHING SKILLS
        # ==================================

        st.subheader(
            "✅ Matching Skills"
        )

        if matched_skills:

            for skill in sorted(
                matched_skills
            ):

                st.success(
                    skill.upper()
                )

        else:

            st.info(
                "No matching skills were detected."
            )


        # ==================================
        # MISSING SKILLS
        # ==================================

        st.subheader(
            "⚠️ Missing Skills"
        )

        if missing_skills:

            for skill in sorted(
                missing_skills
            ):

                st.warning(
                    skill.upper()
                )

        else:

            st.success(
                "No missing skills were detected!"
            )


        # ==================================
        # RECOMMENDATIONS
        # ==================================

        st.subheader(
            "💡 Skill Recommendations"
        )

        if missing_skills:

            for skill in sorted(
                missing_skills
            ):

                st.write(
                    f"### {skill.upper()}"
                )

                recommendation = (
                    get_recommendation(skill)
                )

                st.info(
                    recommendation
                )

        else:

            st.success(
                "No additional skills to recommend."
            )


        # ==================================
        # SKILL GAP SUMMARY
        # ==================================

        st.subheader(
            "📌 Skill Gap Summary"
        )

        st.write(
            f"Your resume is missing "
            f"**{len(missing_skills)} skill(s)** "
            "detected in the job description."
        )


        # ==================================
        # SCORE EXPLANATION
        # ==================================

        st.subheader(
            "📈 Skill Match Calculation"
        )

        st.write(
            f"Matched skills: "
            f"**{len(matched_skills)}**"
        )

        st.write(
            f"Required skills detected: "
            f"**{len(job_skill_set)}**"
        )

        if job_skill_set:

            st.write(
                f"Skill Match = "
                f"({len(matched_skills)} / "
                f"{len(job_skill_set)}) × 100"
            )


        # ==================================
        # TF-IDF EXPLANATION
        # ==================================

        st.subheader(
            "🧠 Text Similarity Analysis"
        )

        st.write(
            "TF-IDF converts the resume and job "
            "description into numerical vectors. "
            "Cosine similarity compares these "
            "vectors based on their vocabulary."
        )

        st.info(
            "Text similarity and skill matching "
            "measure different things. A low text "
            "similarity does not necessarily mean "
            "that the required skills are missing."
        )


        # ==================================
        # RESUME TEXT
        # ==================================

        with st.expander(
            "📄 View Extracted Resume Text"
        ):

            st.text(
                resume_text
            )


        # ==================================
        # JOB DESCRIPTION
        # ==================================

        with st.expander(
            "💼 View Job Description"
        ):

            st.text(
                job_description
            )


    # ======================================
    # ERROR HANDLING
    # ======================================

    except Exception as e:

        st.error(
            "❌ Something went wrong during analysis."
        )

        st.exception(e)


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "AI Job & Resume Analyzer | "
    "Python • Streamlit • NLP • Machine Learning"
)