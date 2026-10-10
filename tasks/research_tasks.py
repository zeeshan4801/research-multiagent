from crewai import Task


def create_tasks(
        planner,
        researcher,
        fact_checker,
        analyst,
        writer,
        topic
):


    planning_task = Task(

        description=f"""
        Create a research plan for:

        {topic}

        Identify important questions.
        """,

        agent=planner

    )


    research_task = Task(

        description=f"""
        Research this topic:

        {topic}

        Collect useful information
        and sources.
        """,

        agent=researcher

    )


    fact_task = Task(

        description="""
        Verify the collected information.
        Remove unreliable claims.
        """,

        agent=fact_checker

    )


    analysis_task = Task(

        description="""
        Analyze research findings
        and extract insights.
        """,

        agent=analyst

    )


    writing_task = Task(

        description="""
        Write the final research report.
        Make it professional and structured.
        """,

        agent=writer

    )


    return [

        planning_task,
        research_task,
        fact_task,
        analysis_task,
        writing_task

    ]
