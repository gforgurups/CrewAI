from crewai import Crew, Process
from Agents import senior_research_analyst, content_writer, topic
from Tasks import research_tasks, writing_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
    agents= [senior_research_analyst, content_writer],
    tasks= [research_tasks, writing_task],
    verbose = True
)
print(senior_research_analyst.allow_delegation)
print(content_writer.allow_delegation)
## start the task execution process with enhanced feedback
result=crew.kickoff(inputs={'topic':topic})
print(result)
