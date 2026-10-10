import os
import sys


sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)


import streamlit as st
import time


from tools.search_tool import search_web

from crew.research_team import run_research



st.set_page_config(

    page_title="AI Research Multi Agent",

    page_icon="🧠",

    layout="wide"

)



st.title("🧠 AI Research Multi Agent Team")


st.write(
"""
Autonomous research system powered by:

- CrewAI
- Groq
- Streamlit
- Web Research
"""
)



topic = st.text_area(

    "Enter research topic",

    placeholder=
    "Example: Future of Artificial Intelligence from 2025 to 2030"

)



if st.button("🚀 Start Research"):


    if not topic.strip():

        st.warning(
            "Please enter a topic"
        )

        st.stop()



    status = st.empty()

    progress = st.progress(0)



    try:


        # Step 1: Web research

        status.info(
            "🔎 Collecting web research..."
        )


        research_data = search_web(topic)


        progress.progress(25)



        # Step 2: CrewAI agents

        agents = [

            "📋 Research Planner",

            "🔎 Research Analyst",

            "✅ Fact Checker",

            "📊 Data Analyst",

            "✍️ Report Writer"

        ]



        for index, agent in enumerate(agents):

            status.info(
                f"⚙️ Working: {agent}"
            )


            progress.progress(
                25 + int((index+1)/len(agents)*75)
            )


            time.sleep(0.5)



        with st.spinner(
            "Generating final report..."
        ):


            result = run_research(

                topic,

                research_data

            )



        st.success(
            "✅ Research completed"
        )


        st.divider()


        st.subheader(
            "📄 Final Report"
        )


        st.write(result)



    except Exception as e:


        st.error(
            "❌ Application Error"
        )


        st.code(
            str(e)
        )
