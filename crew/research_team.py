from crewai import Crew, Process


from agents.researcher import research_agent

from agents.writer import writer_agent


from tasks.research_tasks import create_tasks



def run_research(topic, research_data):


    # Limit input size

    research_data = research_data[:2500]


    tasks = create_tasks(

        research_agent,

        writer_agent,

        topic,

        research_data

    )


    crew = Crew(

        agents=[

            research_agent,

            writer_agent

        ],

        tasks=tasks,

        process=Process.sequential,

        verbose=False,

        memory=False

    )


    return crew.kickoff()
