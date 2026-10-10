from crewai import Crew, Process


from agents.planner import planner_agent
from agents.researcher import research_agent
from agents.fact_checker import fact_checker_agent
from agents.analyst import analyst_agent
from agents.writer import writer_agent


from tasks.research_tasks import create_tasks



def run_research(topic, research_data):


    tasks = create_tasks(

        planner_agent,

        research_agent,

        fact_checker_agent,

        analyst_agent,

        writer_agent,

        topic,

        research_data

    )


    crew = Crew(

        agents=[

            planner_agent,

            research_agent,

            fact_checker_agent,

            analyst_agent,

            writer_agent

        ],

        tasks=tasks,

        process=Process.sequential,

        verbose=True

    )


    result = crew.kickoff()


    return result
