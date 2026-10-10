from crewai import Task



def create_tasks(
    researcher,
    writer,
    topic,
    research_data
):


    research_task = Task(

        description=f"""

Analyze this topic:

{topic}


Use this collected information:

{research_data}


Extract:

- Important facts
- Key points
- Useful insights

Keep it concise.

""",

        expected_output="""

A concise research summary.

""",

        agent=researcher

    )


    writing_task = Task(

        description="""

Create a professional final report
from the research summary.

Include:

- Introduction
- Main points
- Conclusion
- Recommendations

Keep it concise.

""",

        expected_output="""

A professional research report.

""",

        agent=writer

    )


    return [

        research_task,

        writing_task

    ]
