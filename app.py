import pandas as pd
import seaborn as sns
import streamlit as st
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from tool.model import model_llm
from tool.funtion import combine_llm , process_query ,plt_code , remove_print_function, is_valid_code, display_chat_history

load_dotenv()

def main():
    st.set_page_config(
        page_title= 'Data analysis',
        layout= 'centered'
    )
    llm = model_llm()
    

    st.header(":blue[Interactive Visualization AI] :sunglasses:")
    st.write("### Welcome to interactive visualization tool")
    
    
    with st.sidebar:
        st.title(":blue[Upload file here] :sunglasses:")
        uploade_file = st.file_uploader("" , type='csv')
    
    if 'history' not in st.session_state:
        st.session_state.history = []
    if uploade_file:
        st.session_state.df = pd.read_csv(uploade_file)
        st.write(st.session_state.df.head())
        df = st.session_state.df
        agent = combine_llm(llm , df)
        text_input = st.text_input("")
        btn = st.button("Send")
        
        if btn:
            with st.spinner("Prosessing..."):
                reponse = process_query(agent , text_input)
                if 'plot' in reponse.lower():
                    fig = plt_code(reponse, df=st.session_state.df)
                    if fig:
                        st.pyplot(fig)
                        
                else:
                    st.session_state.history.append((text_input, reponse))
                    if is_valid_code(reponse):
                    
                        st.write(eval(remove_print_function(reponse), {"df": df}))
                    else:
                        st.write(reponse)
                    
                st.write("** Executed code:**")
                st.code(reponse)
        st.divider()
        display_chat_history()
                
if __name__ == "__main__":
    main()