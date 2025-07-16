import asyncio
from team.math_team import math_team
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import streamlit as st

st.set_page_config(page_title="Math Solver",page_icon="➕➖✖️➗")
st.title("Math Solver using Autogen")
task = st.chat_input("Enter your math question")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# for message in st.session_state.chat_history:
#     with st.chat_message(message['role']):
#         st.markdown(message['content'])

async def run_analysis(team,task):
    try:
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                msg = f"{message.source}: {message.content}"
                yield {"type": "message", "content": msg}
            elif isinstance(message, TaskResult):
                # Save the team state after task completion
                st.session_state.autogen_team_state = team._runtime.state if hasattr(team, '_runtime') else None
                yield {"type": "result", "content": f"Analysis completed! {message.stop_reason}"}
                break

    except Exception as e:
        yield {"type":"error","content":f"Error{str(e)}"}

if task:
    async def collect_message():
        team = math_team()
        try:
            async for response in run_analysis(team, task):
                if response["type"] == "message":
                    with st.chat_message("assistant"):
                        st.markdown(response["content"])
                    st.session_state.chat_history.append({"role": "assistant", "content": response["content"]})
                elif response["type"] == "result":
                    with st.chat_message("assistant"):
                        st.markdown(response["content"])
                    st.session_state.chat_history.append({"role": "assistant", "content": response["content"]})
                elif response["type"] == "error":
                    with st.chat_message("assistant"):
                        st.error(response["content"])
                    st.session_state.chat_history.append({"role": "assistant", "content": response["content"]})
        except Exception as e:
            print(f"Error : {str(e)}")
        finally:
            print("Task Completed")

        
    asyncio.run(collect_message())
        
    