import os
import sys
import time


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



st.set_page_config(

    page_title="AI Research Assistant",

    page_icon="🧠",

    layout="wide"

)



st.markdown(

"""
<style>

.main-title{

font-size:45px;
font-weight:800;
text-align:center;
color:#0ea5e9;

}


.card{

padding:18px;
border-radius:15px;
background:#f8fafc;
margin-bottom:15px;

}


</style>

""",

unsafe_allow_html=True

)



st.markdown(

"""
<div class="main-title">

🧠 AI Research Assistant

</div>

""",

unsafe_allow_html=True

)



st.caption(

"Web Research • AI Analysis • Professional Reports"

)



st.divider()



topic = st.text_area(

"🔍 Research Topic",

height=100

)



if st.button(
"🚀 Generate Report"
):


    if not topic:

        st.warning(
            "Enter a topic first"
        )

        st.stop()



    status = st.empty()

    progress = st.progress(0)



    status.info(
        "🔎 Searching sources..."
    )


    research_data = search_web(topic)


    progress.progress(35)



    status.info(
        "🧠 AI Research Analyst working..."
    )


    result = run_research(

        topic,

        research_data

    )


    progress.progress(80)



    status.info(
        "✍️ Preparing final report..."
    )


    time.sleep(1)


    progress.progress(100)


    status.success(
        "✅ Completed"
    )



    report = (

        result.raw

        if hasattr(result,"raw")

        else str(result)

    )


    sources = extract_sources(

        research_data

    )



    st.divider()



    col1,col2,col3 = st.columns(3)


    with col1:

        st.metric(

            "Sources",

            len(sources)

        )


    with col2:

        st.metric(

            "AI Agents",

            "2"

        )


    with col3:

        st.metric(

            "Model",

            "GPT-OSS-20B"

        )



    tab1,tab2,tab3 = st.tabs(

        [

        "📄 Report",

        "🔗 Sources",

        "⬇ Download"

        ]

    )



    with tab1:

        st.markdown(report)



    with tab2:


        if sources:

            for s in sources:

                st.write(
                    "🔗",
                    s
                )

        else:

            st.info(
                "No sources found"
            )



    with tab3:


        pdf = create_pdf(report)


        st.download_button(

            "📄 Download PDF",

            pdf,

            "research_report.pdf",

            "application/pdf"

        )


        st.download_button(

            "📝 Download Markdown",

            report,

            "research_report.md",

            "text/markdown"

        )
