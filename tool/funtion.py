import re
import ast
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent

def is_valid_code(code_str : str) -> bool:
    "Check data must be in python format"
    try:
        ast.parse(code_str)
        return True
    except SyntaxError:
        return False
    
    
def combine_llm(llm , data):
    "combine model with data"
    agent = create_pandas_dataframe_agent(
        llm,
        data,
        agent_type="tool-calling",
        verbose=True,
        allow_dangerous_code=True,
        return_intermediate_steps=True
    )
    return agent

def remove_print_function(code : str) -> str:
    'delete extra characters'
    if 'print' in code:
        clean_code = code.replace('print(' , "")
        clean_code = re.sub(r'\)$', '', clean_code)
        return clean_code
    return code

def process_query(agent, query : str) -> str:
    'response to question'
    text = 'just show the code no need to explain further'
    answer = agent(f'{query} {text}')
    result = answer['output']
    result = result.replace("python", "").replace("Python", "").replace("```", "")
    return result

def plt_code(code: str, df: pd.DataFrame):
    try:
        compiled_code = compile(code, '<string>', 'exec')

        local_vals = {"plt": plt, "df": df}
        exec(compiled_code, globals(), local_vals)
        return plt.gcf()   
    except Exception as e:
        st.error(f'{e}')
        return None
    
def display_chat_history():
    st.markdown("## Chat History: ")
    for i, (q, r) in enumerate(st.session_state.history):
        st.markdown(f"**Query: {i+1}:** {q}")
        st.markdown(f"**Response: {i+1}:** {r}")
        st.markdown("---")
    





