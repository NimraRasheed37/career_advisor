import os
from dotenv import load_dotenv, find_dotenv
from agents import function_tool, RunContextWrapper, AsyncOpenAI

load_dotenv(find_dotenv())

api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@function_tool
async def get_career_roadmap():
    try:
        prompt = (
            f"I'm interested in becoming a {input['career_field']}.\n"
            "Please provide a step-by-step skill roadmap that includes beginner, intermediate, and advanced level skills.\n"
            "Format the response clearly using bullet points or numbered steps."
        )
        
        response = await client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}]
        )
        
        output = response.choices[0].message.content
        
        return {
            "skill_roadmap": output.strip()
        }
        
    except Exception as e:
        print("❌ Exception in get_career_roadmap tool:", str(e))
        return {
            "error": f"❌ Exception in get_career_roadmap tool: {str(e)}"
        }