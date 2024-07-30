import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer

def main():
    st.set_page_config(
        page_title=" Interactive Visualization Tool", layout="wide"
    )

    
    
    st.header(":blue[Interactive Visualization] :sunglasses:")
    st.write("### Welcome to interactive visualization tool. Please enjoy !")


    if st.session_state.get("df") is not None:
        pyg_app = StreamlitRenderer(st.session_state.df)
        pyg_app.explorer()
    else:
        st.info('Please upload data')
        
        
if __name__ == "__main__":
    main()
