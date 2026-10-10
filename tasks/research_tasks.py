from crewai import Task



def create_tasks(
    researcher,
    writer,
    topic,
    research_data
):


    research_task = Task(

        description=f"""

Analyze this research topic:

{topic}


Collected research:

{research_data}


Extract:

- Important facts
- Key statistics
- Main insights
- Source references


Keep the analysis concise.

""",

        expected_output="""

A structured research summary with
important facts and source references.

""",

        agent=researcher

    )



    writing_task = Task(

        description="""

Create a professional research report.

Structure:

1. Executive Summary

2. Key Findings

3. Analysis

4. Recommendations

5. Sources


Mention sources where relevant.


Keep the report under 700 words.

""",

        expected_output="""

A professional research report
with citations and recommendations.

""",

        agent=writer

    )


    return [

        research_task,

        writing_task

    ]
