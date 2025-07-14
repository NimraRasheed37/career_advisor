import chainlit as cl
from agents import Runner
from agents.run import RunConfig
from advisor.career_agent import career_agent
from advisor.skill_agent import skill_agent
from advisor.job_agent import job_agent
from config import model, external_client, gemini_config

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message("🎓 Hey there! Let us discover the right path for you. What subjects or hobbies do you enjoy?").send()

@cl.on_message
async def handle(msg: cl.Message):
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": msg.content})

    thinking = cl.Message("💡Thinking...")
    await thinking.send()

    try:
        result = await Runner.run(
            career_agent,
            history,
            run_config=gemini_config
        )
        output = result.final_output

        thinking.content = output
        await thinking.update()

        history = result.to_input_list()
        cl.user_session.set("history", history)

    except Exception as e:
        thinking.content = f"❌ Error: {e}"
        await thinking.update()
