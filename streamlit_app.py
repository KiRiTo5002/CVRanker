import streamlit as st

from src.parser import extract_text_from_pdf
from src.extractor import extract_resume, extract_jd
from src.scorer import score_candidate
from src.ranker import rank_candidates


# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="CVRanker",
    page_icon="📄",
    layout="wide",
)


# ---------------- Helper Functions ---------------- #

def render_header():
    st.title("📄 CVRanker")
    st.caption(
        "AI-powered Resume Ranking using LLMs, Pydantic and Rule-based Scoring"
    )


def render_upload_section():

    with st.container(border=True):

        st.subheader("📂 Upload Documents")

        job_description = st.file_uploader(
            "Job Description",
            type=["pdf"],
        )

        resumes = st.file_uploader(
            "Candidate Resumes",
            type=["pdf"],
            accept_multiple_files=True,
        )

        st.divider()

        left, center, right = st.columns([2, 1, 2])

        with center:
            run = st.button(
                "🚀 Rank Candidates",
                use_container_width=True,
            )

    return job_description, resumes, run


def render_uploaded_files(job_file, resumes):

    if job_file:

        st.success(f"Job Description: **{job_file.name}**")

    if resumes:

        st.info(f"Uploaded **{len(resumes)}** resume(s)")

        with st.expander("View Uploaded Resumes"):

            for file in resumes:
                st.write(f"• {file.name}")


def render_candidate_card(rank, resume, match):

    medals = {
        1: "🥇",
        2: "🥈",
        3: "🥉",
    }

    icon = medals.get(rank, "⭐")

    with st.container(border=True):

        col1, col2 = st.columns([4, 1])

        with col1:

            st.subheader(f"{icon} {resume.name}")

            st.progress(match.overall_score / 100)

        with col2:

            st.metric(
                "Overall Match",
                f"{match.overall_score:.1f}%",
            )

        score1, score2, score3, score4 = st.columns(4)

        score1.metric("Skills", f"{match.skills_score:.0f}%")
        score2.metric("Experience", f"{match.experience_score:.0f}%")
        score3.metric("Education", f"{match.education_score:.0f}%")
        score4.metric("Certificates", f"{match.certification_score:.0f}%")

        with st.expander("View Match Details"):

            left, right = st.columns(2)

            with left:

                st.markdown("### ✅ Matched Skills")

                if match.matched_required_skills:

                    for skill in match.matched_required_skills:
                        st.write(f"• {skill}")

                else:
                    st.write("None")

            with right:

                st.markdown("### ❌ Missing Skills")

                if match.missing_required_skills:

                    for skill in match.missing_required_skills:
                        st.write(f"• {skill}")

                else:
                    st.write("None")


# ---------------- Main Application ---------------- #

render_header()

job_file, resume_files, run = render_upload_section()

render_uploaded_files(job_file, resume_files)


if run:

    if job_file is None:

        st.error("Please upload a Job Description.")
        st.stop()

    if not resume_files:

        st.error("Please upload at least one Resume.")
        st.stop()

    with st.spinner("Ranking Candidates..."):

        jd_text = extract_text_from_pdf(job_file)

        job_description = extract_jd(jd_text)

        candidates = []

        progress = st.progress(0)

        for index, resume_file in enumerate(resume_files):

            resume_text = extract_text_from_pdf(resume_file)

            resume = extract_resume(resume_text)

            match = score_candidate(
                resume,
                job_description,
            )

            candidates.append(
                (
                    resume,
                    match,
                )
            )

            progress.progress((index + 1) / len(resume_files))

        ranked = rank_candidates(candidates)

    progress.empty()

    st.divider()

    st.header("🏆 Ranking Results")

    for rank, (resume, match) in enumerate(
        ranked,
        start=1,
    ):

        render_candidate_card(
            rank,
            resume,
            match,
        )