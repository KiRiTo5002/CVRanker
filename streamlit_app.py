import streamlit as st

from src.extractor import extract_jd, extract_resume
from src.parser import extract_text_from_pdf
from src.ranker import rank_candidates
from src.scorer import score_candidate

st.set_page_config(
    page_title="CVRanker",
    page_icon="📄",
    layout="wide",
)


def render_header() -> None:
    st.title("📄 CVRanker")
    st.caption("AI-powered Resume Ranking using LLMs, Pydantic and Rule-based Scoring")


def render_upload_section():

    with st.container(border=True):

        st.subheader("📂 Upload Documents")

        job_file = None
        jd_text = ""

        tab1, tab2 = st.tabs(
            [
                "📄 Upload PDF",
                "✍️ Paste Job Description",
            ]
        )

        with tab1:

            uploaded_pdf = st.file_uploader(
                "Job Description PDF",
                type=["pdf"],
                key="jd_pdf",
            )

            if uploaded_pdf is not None:
                job_file = uploaded_pdf

        with tab2:

            pasted_text = st.text_area(
                "Paste Job Description",
                height=250,
                placeholder="Paste the complete job description here...",
                key="jd_text",
            )

            if pasted_text.strip():
                jd_text = pasted_text

                st.caption(f"{len(jd_text):,} characters")

        resumes = st.file_uploader(
            "Candidate Resumes",
            type=["pdf"],
            accept_multiple_files=True,
        )

        st.divider()

        _, center, _ = st.columns([2, 1, 2])

        with center:

            run = st.button(
                "🚀 Rank Candidates",
                use_container_width=True,
            )

    return job_file, jd_text, resumes, run

def render_uploaded_files(
    job_file,
    jd_text,
    resumes,
):

    if job_file:

        st.success(f"✅ Uploaded Job Description: **{job_file.name}**")

    elif jd_text.strip():

        st.success("✅ Job Description pasted successfully.")

    if resumes:

        st.info(f"📂 Uploaded **{len(resumes)}** resume(s)")

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


def main():

    render_header()

    job_file, jd_text, resume_files, run = render_upload_section()

    render_uploaded_files(
        job_file,
        jd_text,
        resume_files,
    )

    if not run:
        return

    if job_file is None and not jd_text.strip():

        st.error("Please upload a Job Description PDF or paste a Job Description.")

        return

    if not resume_files:

        st.error("Please upload at least one Resume.")

        return

    with st.spinner("Analyzing resumes with AI..."):

        if job_file:

            job_description_text = extract_text_from_pdf(job_file)

        else:

            job_description_text = jd_text

        job_description = extract_jd(job_description_text)

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

        progress.empty()

    ranked = rank_candidates(candidates)

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


if __name__ == "__main__":
    main()
