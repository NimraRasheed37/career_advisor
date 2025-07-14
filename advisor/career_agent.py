from agents import Agent, handoff
from config import model
from advisor.skill_agent import  skill_agent
from advisor.job_agent import  job_agent
from utils.orchestrator import orchestrator_handoff


career_agent = Agent(
    name = "CareerAgent",
    instructions = """
    You are a Career Guidance Assistant, helping users explore career options based on their strengths and interests.  
    Your Role:
    * Ask about their skills, passions, or favorite subjects.  
    * Recommend 2-3 suitable career paths based on their input.  
    * Let them pick one to explore further.  
    * Once they choose, transition to SkillAgent for a learning plan.  
    
    Tone:
    * Encouraging, clear, polite, friendly and engaging .
    
    Rules:
    * Keep suggestions relevant and practical.  
    """,
    tools = [],
    model = model,
    handoffs=[
        handoff(agent = skill_agent, on_handoff = orchestrator_handoff(skill_agent)),
        handoff(agent = job_agent, on_handoff = orchestrator_handoff(job_agent)),
    ]
)