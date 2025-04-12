from crewai import Agent
from Tools import yt_tool
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

# Tool
search_tool = SerperDevTool(n=2)
yt_handle = "@Samvashisht_411"
topic = "AI in Healthcare"

# Agent 1
senior_research_analyst = Agent(
    role = "Senior Research Analyst",
    goal= f"Research, analyze, and synthesize comprehensive information on {topic} from youtube videos",
    backstory="You're an expert research analyst with advanced web research skills. "
                    "You excel at finding, analyzing, and synthesizing information from "
                    "across the internet using search tools. You're skilled at "
                    "distinguishing reliable sources from unreliable ones, "
                    "fact-checking, cross-referencing information, and "
                    "identifying key patterns and insights. You provide "
                    "well-organized research briefs with proper citations "
                    "and source verification. Your analysis includes both "
                    "raw data and interpreted insights, making complex "
                    "information accessible and actionable.",
    verbose = True,
    allow_delegation=False,
    tools = [search_tool,yt_tool]
    #,llm = llm
)

##create a Senior Blog Writer agent with YT tool
content_writer = Agent(
    role="Content Writer",
    goal="Transform research findings into engaging blog posts while maintaining accuracy",
    backstory="You're a skilled content writer specialized in creating "
                    "engaging, accessible content from technical research. "
                    "You work closely with the Senior Research Analyst and excel at maintaining the perfect "
                    "balance between informative and entertaining writing, "
                    "while ensuring all facts and citations from the research "
                    "are properly incorporated. You have a talent for making "
                    "complex topics approachable without oversimplifying them.",
    verbose=True,
    allow_delegation=False
    #,llm = llm
)
