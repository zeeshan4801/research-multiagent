import os
import sys
import time


# --------------------------------
# Fix Streamlit Cloud imports
# --------------------------------

sys.path.append(
    os.path.dirname(os.path.abspath(__file__))
)


import streamlit as st


from crew.research_team import run_research



# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(

    page_title="AI Research Multi Agent",

    page_icon="🧠",

    layout="wide"

)



# --------------------------------
# Custom CSS
# --------------------------------

st.markdown(
"""
<style>

.main-title {

    font-size:48px;
    font-weight:800;
    text-align:center;
    color:#38bdf8;

}


.subtitle {

    text-align:center;
    font-size:18px;
    color:#64748b;

}


.agent-box {

    padding:15px;

    border-radius:12px;

    background:#f1f5f9;

    margin:10px 0;

    font-size:18px;

}


.report-box {

    padding:20px;

    border-radius:15px;

    background:#ffffff;

}


.stButton button {

    width:100%;

    height:50px;

    font-size:18px;

    border-radius:10px;

}


</style>

""",

unsafe_allow_html=True

)



# --------------------------------
# Header
# --------------------------------


st.markdown(

"""
<div class="main-title">

🧠 AI Research Multi-Agent Team

</div>

<div class="subtitle">

Autonomous AI researchers creating professional reports

</div>

""",

unsafe_allow_html=True

)


st.write("")



# --------------------------------
# Sidebar
# --------------------------------


with st.sidebar:


    st.header("🤖 AI Team")


    st.markdown(
    """
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



# --------------------------------
# Input
# --------------------------------


topic = st.text_area(

    "🔍 Enter your research topic",

    placeholder="""
Example:

Analyze the future of Artificial Intelligence
in healthcare from 2025 to 2030.
""",

    height=120

)



# --------------------------------
# Agents
# --------------------------------


agents = [

    "📋 Research Planner",

    "🔎 Research Collector",

    "✅ Fact Checker",

    "📊 Data Analyst",

    "✍️ Report Writer"

]



# --------------------------------
# Run System
# --------------------------------


if st.button("🚀 Start AI Research"):


    if not topic.strip():

        st.warning(
            "Please enter a research topic."
        )

        st.stop()



    st.subheader(
        "⚙️ Agent Activity"
    )


    status = st.empty()

    progress = st.progress(0)



    try:


        # Visual agent progress

        for index, agent in enumerate(agents):


            status.markdown(

            f"""
            <div class="agent-box">

            ⚡ Working:

            <b>{agent}</b>

            </div>
            """,

            unsafe_allow_html=True

            )


            progress.progress(
                int(
                    ((index + 1) / len(agents)) * 100
                )
            )


            time.sleep(0.7)



        status.info(
            "🧠 CrewAI agents are generating final report..."
        )


        # Actual CrewAI execution

        result = run_research(topic)



        status.success(
            "✅ Research completed successfully!"
        )


        st.divider()


        st.subheader(
            "📄 Final Research Report"
        )


        st.markdown(

            f"""
            <div class="report-box">

            {result}

            </div>
            """,

            unsafe_allow_html=True

        )



    except Exception as e:


        error_message = str(e)


        if "RateLimitError" in error_message:


            st.warning(

            """
            ⏳ Groq rate limit reached.

            The AI team generated too many tokens
            in a short time.

            Please wait 10 seconds and try again.
            """

            )


            time.sleep(10)


            try:

                result = run_research(topic)


                st.success(
                    "Research completed after retry."
                )


                st.write(result)


            except Exception as retry_error:


                st.error(
                    "Retry failed."
                )

                st.code(
                    str(retry_error)
                )



        else:


            st.error(
                "❌ Application Error"
            )


            st.code(
                error_message
            )


            st.info(
            """
            Check:

            1. GROQ_API_KEY in Streamlit Secrets

            2. requirements.txt versions

            3. CrewAI configuration

            """
            )
