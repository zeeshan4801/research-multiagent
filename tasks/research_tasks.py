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
        Plan research for:

        {topic}

        Create key questions.
        """,

        expected_output="""
        Short research plan.
        """,

        agent=planner
    )


    research_task = Task(

        description=f"""
        Research:

        {topic}

        Find important facts,
        statistics and sources.
        """,

        expected_output="""
        Research notes with findings
        and sources.
        """,

        agent=researcher
    )


    fact_task = Task(

        description="""
        Verify research information.
        Check accuracy.
        """,

        expected_output="""
        Verified research summary.
        """,

        agent=fact_checker
    )


    analysis_task = Task(

        description="""
        Analyze verified information.
        Find important insights.
        """,

        expected_output="""
        Analysis with key insights.
        """,

        agent=analyst
    )


    writing_task = Task(

        description="""
        Write final professional report.
        Keep it structured and concise.
        """,

        expected_output="""
        Complete research report.
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
