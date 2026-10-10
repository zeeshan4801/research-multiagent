import sys
import os

# Fix imports on Streamlit Cloud
sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)


import streamlit as st
import time


from crew.research_team import run_research



# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(

    page_title="AI Research Multi Agent",

    page_icon="🧠",

    layout="wide",

    initial_sidebar_state="expanded"

)



# -----------------------------
# Custom CSS
# -----------------------------

st.markdown(
"""
<style>

body {

    background-color:#0f172a;

}


.main-title {

    font-size:45px;

    font-weight:800;

    color:#38bdf8;

    text-align:center;

}


.subtitle {

    font-size:18px;

    color:#94a3b8;

    text-align:center;

}



.agent-card {

    padding:15px;

    border-radius:12px;

    background:#1e293b;

    color:white;

    margin-bottom:10px;

}


.stButton button {

    width:100%;

    height:50px;

    border-radius:12px;

    font-size:18px;

    font-weight:bold;

}


</style>

""",

unsafe_allow_html=True
)



# -----------------------------
# Header
# -----------------------------


st.markdown(

"""
<div class="main-title">
🧠 AI Research Multi-Agent Team
</div>

<br>

<div class="subtitle">

Autonomous AI researchers working together
to create professional reports

</div>

""",

unsafe_allow_html=True

)



st.write("")



# -----------------------------
# Sidebar
# -----------------------------


with st.sidebar:


    st.header("⚙️ System Information")


    st.write(

    """
    **AI Team Members**

    📋 Research Planner

    🔎 Research Collector

    ✅ Fact Checker

    📊 Data Analyst

    ✍️ Report Writer

    """

    )


    st.divider()


    st.info(

        "Powered by CrewAI + Groq + Streamlit"

    )



# -----------------------------
# User Input
# -----------------------------


topic = st.text_area(

    "🔍 Enter your research topic",

    placeholder=
    """
    Example:

    Impact of Artificial Intelligence
    on education in 2026

    """,

    height=120

)



# -----------------------------
# Agents Display
# -----------------------------


agents = [

    "📋 Research Planner",

    "🔎 Research Collector",

    "✅ Fact Checker",

    "📊 Data Analyst",

    "✍️ Report Writer"

]



# -----------------------------
# Run Research
# -----------------------------


if st.button("🚀 Start AI Research"):


    if not topic.strip():

        st.warning(
            "Please enter a research topic first."
        )

        st.stop()



    st.subheader(
        "🤖 Agent Activity"
    )


    status_box = st.empty()


    progress = st.progress(0)



    for index, agent in enumerate(agents):


        status_box.markdown(

        f"""
        <div class="agent-card">

        ⚡ Currently working:

        <b>{agent}</b>

        </div>

        """,

        unsafe_allow_html=True

        )


        progress.progress(

            int(
                ((index+1)/len(agents))*100
            )

        )


        time.sleep(1)



    status_box.success(

        "All agents completed their tasks. Generating final report..."

    )



    try:


        with st.spinner(

            "🧠 AI team is preparing your research report..."

        ):


            result = run_research(topic)



        st.success(

            "✅ Research Completed Successfully"

        )


        st.divider()


        st.subheader(

            "📄 Final Research Report"

        )


        st.write(result)



    except Exception as e:


        st.error(

            "❌ Application Error"

        )


        st.code(

            str(e)

        )


        st.info(

        """
        Please check:

        1. GROQ_API_KEY is added in Streamlit Secrets

        2. requirements.txt versions

        3. CrewAI imports

        """

        )
