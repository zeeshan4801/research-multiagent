import os
import sys


sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)


import streamlit as st
import time


from tools.search_tool import web_search

from crew.research_team import run_research



st.set_page_config(

    page_title="AI Research Team",

    page_icon="🧠",

    layout="wide"

)



st.title("🧠 AI Research Multi Agent Team")


st.write(
"Research Planner + Web Research + Analysis + Report Writing"
)



topic = st.text_area(
    "Enter research topic"
)



if st.button("🚀 Start Research"):


    if not topic:

        st.warning(
            "Please enter a topic"
        )

        st.stop()



    with st.spinner(
        "🔎 Collecting web research..."
    ):

        research_data = web_search(topic)



    agents = [

        "📋 Planner",

        "🔎 Research Analyst",

        "✅ Fact Checker",

        "📊 Analyst",

        "✍️ Writer"

    ]


    progress = st.progress(0)

    status = st.empty()



    for i,a in enumerate(agents):

        status.info(
            f"Working: {a}"
        )

        progress.progress(
            int((i+1)/len(agents)*100)
        )

        time.sleep(0.5)



    try:

        with st.spinner(
            "Generating final report..."
        ):

            result = run_research(
                topic,
                research_data
            )


        st.success(
            "Research completed!"
        )


        st.write(result)



    except Exception as e:


        st.error(
            "Application Error"
        )

        st.code(
            str(e)
        )
