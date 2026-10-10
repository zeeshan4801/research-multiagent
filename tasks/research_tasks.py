from crewai import Task



def create_tasks(

    researcher,

    writer,

    topic,

    research_data

):


    research_task = Task(

        description=f"""

Analyze:

{topic}


Research notes:

{research_data}


Extract only:

- 5 important facts
- 3 insights

""",

        expected_output="""

Short research summary.

""",

        agent=researcher

    )



    writing_task = Task(

        description="""

Create a concise professional report.

Maximum:

600 words.

Include:

- Introduction
- Key Findings
- Conclusion
- Recommendations

""",

        expected_output="""

Professional short report.

""",

        agent=writer

    )


    return [

        research_task,

        writing_task

    ]
