import streamlit as st
import time


from crew.research_team import run_research



st.set_page_config(

    page_title="AI Research Team",

    page_icon="🧠",

    layout="wide"

)



st.markdown(
"""
<style>

.title{

font-size:45px;
font-weight:800;
color:#38bdf8;

}


.card{

padding:20px;
border-radius:15px;
background:#111827;

}


</style>

""",

unsafe_allow_html=True
)



st.markdown(

"<div class='title'>🧠 AI Research Multi Agent Team</div>",

unsafe_allow_html=True

)


st.write(
"""
Your autonomous AI research department.
Multiple agents collaborate to create reports.
"""
)



topic = st.text_input(

"Enter your research topic"

)



agents=[

"📋 Research Planner",

"🔎 Research Collector",

"✅ Fact Checker",

"📊 Data Analyst",

"✍️ Report Writer"

]



if st.button("🚀 Start Research"):


    status=st.empty()


    for agent in agents:

        status.info(
            f"Currently working: {agent}"
        )

        time.sleep(1)



    with st.spinner(
        "AI team preparing report..."
    ):


        result=run_research(topic)



    st.success(
        "Research completed!"
    )


    st.markdown(
        result
    )
