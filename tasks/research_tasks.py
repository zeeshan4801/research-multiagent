from crewai import Task



def create_tasks(
    planner,
    researcher,
    fact_checker,
    analyst,
    writer,
    topic,
    research_data
):


    planning_task = Task(

        description=f"""
Create a research plan for:

{topic}

Research areas:
- Key questions
- Important facts
- Required analysis
""",

        expected_output="""
A structured research plan.
""",

        agent=planner

    )


    research_task = Task(

        description=f"""
Analyze this collected research:

{research_data}

Organize:
- Facts
- Statistics
- Important points
""",

        expected_output="""
Structured research notes.
""",

        agent=researcher

    )


    fact_task = Task(

        description="""
Verify the research notes.
Identify unreliable information.
""",

        expected_output="""
Verified research summary.
""",

        agent=fact_checker

    )


    analysis_task = Task(

        description="""
Analyze verified information.
Create insights and conclusions.
""",

        expected_output="""
Research analysis report.
""",

        agent=analyst

    )


    writing_task = Task(

        description="""
Write the final professional report.
Use headings and recommendations.
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
