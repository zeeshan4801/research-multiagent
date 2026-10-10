import os
import sys


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



# ---------- CSS ----------


st.markdown(
"""
<style>

.title {

font-size:45px;
font-weight:800;
text-align:center;

}


.subtitle {

text-align:center;
color:#64748b;

}


.card {

padding:20px;

border-radius:15px;

background:#f8fafc;

margin:10px;

}


</style>
""",

unsafe_allow_html=True
)



# ---------- Header ----------


st.markdown(

"""
<div class="title">

🧠 AI Research Assistant

</div>

<div class="subtitle">

Autonomous Research • Analysis • Professional Reports

</div>

""",

unsafe_allow_html=True

)



st.divider()



topic = st.text_area(

    "🔍 Enter Research Topic",

    placeholder=
    "Example: Future of solar energy market in USA",

    height=120

)



if st.button(
    "🚀 Generate Research Report"
):


    if not topic:

        st.warning(
            "Please enter a topic"
        )

        st.stop()



    progress = st.progress(0)


    status = st.empty()



    # Search


    status.info(
        "🔎 Searching trusted sources..."
    )


    research_data = search_web(topic)


    progress.progress(30)



    # Agents


    status.info(
        "🧠 Research Analyst working..."
    )


    result = run_research(

        topic,

        research_data

    )


    progress.progress(80)



    status.info(
        "✍️ Preparing final report..."
    )


    progress.progress(100)



    st.success(
        "Research completed successfully!"
    )



    tabs = st.tabs(

        [
            "📄 Report",
            "🔗 Sources",
            "⬇ Download"
        ]

    )



    # Report Tab


    with tabs[0]:


        st.markdown(

            result.raw

            if hasattr(result,"raw")

            else str(result)

        )



    # Sources Tab


    with tabs[1]:


        sources = extract_sources(

            str(research_data)

        )


        if sources:


            for s in sources:

                st.write(
                    "🔗 ",
                    s
                )


        else:

            st.info(
                "No sources detected"
            )



    # Download Tab


    with tabs[2]:


        report_text = (

            result.raw

            if hasattr(result,"raw")

            else str(result)

        )


        pdf = create_pdf(
            report_text
        )


        st.download_button(

            label="📄 Download PDF Report",

            data=pdf,

            file_name="AI_Research_Report.pdf",

            mime="application/pdf"

        )
