import os
import sys
import time


# ---------------------------------
# Streamlit Cloud import fix
# ---------------------------------

sys.path.append(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


import streamlit as st


from tools.search_tool import search_web

from crew.research_team import run_research


from utils.pdf_generator import create_pdf

from utils.source_parser import extract_sources



# ---------------------------------
# Page Configuration
# ---------------------------------

st.set_page_config(

    page_title="AI Research Assistant",

    page_icon="🧠",

    layout="wide"

)



# ---------------------------------
# Custom CSS
# ---------------------------------

st.markdown(
"""
<style>

.title {

font-size:45px;
font-weight:800;
text-align:center;
color:#0ea5e9;

}


.subtitle {

text-align:center;
font-size:18px;
color:#64748b;

}


.agent-card {

padding:15px;
border-radius:12px;
background:#f1f5f9;
margin:10px 0;
font-size:17px;

}


.report-card {

padding:20px;
border-radius:15px;
background:#ffffff;

}


</style>

""",

unsafe_allow_html=True

)



# ---------------------------------
# Header
# ---------------------------------

st.markdown(

"""
<div class="title">

🧠 AI Research Multi-Agent Assistant

</div>

<div class="subtitle">

Web Research • AI Analysis • Professional Reports

</div>

""",

unsafe_allow_html=True

)



st.divider()



# ---------------------------------
# Sidebar
# ---------------------------------

with st.sidebar:


    st.header("🤖 AI Team")


    st.markdown(
    """
    🔎 Web Research Layer

    🧠 Research Analyst

    ✍️ Report Writer

    📄 PDF Generator

    """
    )


    st.divider()


    st.info(

        "Powered by CrewAI + Groq + Tavily"

    )



# ---------------------------------
# User Input
# ---------------------------------

topic = st.text_area(

    "🔍 Enter your research topic",

    placeholder=

    """
Example:

Analyze solar energy opportunities
in California.

""",

    height=120

)



# ---------------------------------
# Main Execution
# ---------------------------------

if st.button(
    "🚀 Generate Research Report"
):


    if not topic.strip():

        st.warning(
            "Please enter a research topic."
        )

        st.stop()



    status = st.empty()


    progress = st.progress(0)



    try:


        # -------------------------
        # Step 1 Search
        # -------------------------

        status.markdown(

        """
        <div class="agent-card">

        🔎 Searching trusted sources...

        </div>

        """,

        unsafe_allow_html=True

        )


        research_data = search_web(topic)


        progress.progress(30)



        # -------------------------
        # Step 2 CrewAI
        # -------------------------


        status.markdown(

        """
        <div class="agent-card">

        🧠 Research Analyst working...

        </div>

        """,

        unsafe_allow_html=True

        )



        time.sleep(1)



        status.markdown(

        """
        <div class="agent-card">

        ✍️ Report Writer working...

        </div>

        """,

        unsafe_allow_html=True

        )



        progress.progress(70)



        # -------------------------
        # Run CrewAI with retry
        # -------------------------


        try:


            result = run_research(

                topic,

                research_data

            )


        except Exception as e:


            if "RateLimitError" in str(e):


                status.warning(

                """
                ⏳ Groq rate limit reached.
                Waiting 15 seconds...

                """

                )


                time.sleep(15)



                result = run_research(

                    topic,

                    research_data

                )


            else:

                raise e



        progress.progress(100)



        status.success(

            "✅ Research completed successfully"

        )



        st.divider()



        # -------------------------
        # Tabs
        # -------------------------

        report_tab, source_tab, pdf_tab = st.tabs(

            [

                "📄 Report",

                "🔗 Sources",

                "⬇ Download"

            ]

        )



        # -------------------------
        # Report
        # -------------------------

        with report_tab:


            st.markdown(

            """
            <div class="report-card">

            """,

            unsafe_allow_html=True

            )


            if hasattr(result, "raw"):

                st.markdown(
                    result.raw
                )

            else:

                st.markdown(
                    str(result)
                )



            st.markdown(

            "</div>",

            unsafe_allow_html=True

            )



        # -------------------------
        # Sources
        # -------------------------

        with source_tab:


            sources = extract_sources(

                research_data

            )


            if sources:


                for source in sources:

                    st.write(
                        "🔗",
                        source
                    )


            else:

                st.info(
                    "No sources found."
                )



        # -------------------------
        # PDF
        # -------------------------

        with pdf_tab:


            report_text = (

                result.raw

                if hasattr(result, "raw")

                else str(result)

            )


            pdf_file = create_pdf(

                report_text

            )


            st.download_button(

                label="📄 Download PDF Report",

                data=pdf_file,

                file_name=
                "AI_Research_Report.pdf",

                mime=
                "application/pdf"

            )



    except Exception as e:


        st.error(

            "❌ Application Error"

        )


        st.code(

            str(e)

        )


        st.info(

        """
        Check:

        1. GROQ_API_KEY in Streamlit Secrets

        2. TAVILY_API_KEY in Streamlit Secrets

        3. Groq rate limits

        4. CrewAI configuration

        """

        )
