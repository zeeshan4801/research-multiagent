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
        Create a detailed research strategy for:

        {topic}

        Identify:
        - Key research questions
        - Important areas to investigate
        - Required sources
        """,

        expected_output="""
        A structured research plan containing
        research objectives, questions,
        and information requirements.
        """,

        agent=planner
    )


    research_task = Task(

        description=f"""
        Research the following topic:

        {topic}

        Collect reliable information,
        important facts, statistics,
        and useful sources.
        """,

        expected_output="""
        A research document containing
        collected information, sources,
        and important findings.
        """,

        agent=researcher
    )


    fact_check_task = Task(

        description="""
        Review the collected research.

        Verify important claims,
        identify unreliable information,
        and improve accuracy.
        """,

        expected_output="""
        A fact-checking report showing
        verified information and corrections.
        """,

        agent=fact_checker
    )


    analysis_task = Task(

        description="""
        Analyze the verified research.

        Identify:
        - Trends
        - Patterns
        - Insights
        - Important conclusions
        """,

        expected_output="""
        An analytical summary explaining
        the meaning and implications
        of the research findings.
        """,

        agent=analyst
    )


    writing_task = Task(

        description="""
        Create a professional final research report.

        Organize the information clearly
        with headings, explanations,
        and recommendations.
        """,

        expected_output="""
        A complete professional research report
        suitable for presentation to users.
        """,

        agent=writer
    )


    return [

        planning_task,
        research_task,
        fact_check_task,
        analysis_task,
        writing_task

    ]
