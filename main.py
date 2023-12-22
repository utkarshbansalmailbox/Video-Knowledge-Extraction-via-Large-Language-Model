import streamlit as st
import LangchainModel as lch
import textwrap
import time


st.set_page_config(
    page_title="VideoGPT",
    # page_icon= "random",
    layout="wide",
    initial_sidebar_state="expanded",
    
)

tab1, tab2 = st.tabs(["@Data", "@About" ])

with tab1:
    with st.sidebar:
        st.title("Video Transcript LLM") 
        "An intuitive Streamlit application that revolutionizes how users engage with YouTube videos by facilitating seamless question-and-answer interactions powered by a sophisticated Language Model (LLM) "

        st.divider()
        with st.form(key='my_form'):

            submitted = st.form_submit_button(label='Submit')
            if submitted:
                #  st.write("Processing ◔ ◕")
                with st.spinner("Processing"):
                    time.sleep(90)
                    st.success("DONE")
            
            youtube_url = st.sidebar.text_area(
                label="Video URL",
                max_chars=80
                )
            query = st.sidebar.text_area(
                label="Query",
                max_chars=50,
                key="query"
                )


    if query and youtube_url:
            db = lch.create_db_from_youtube_video_url(youtube_url)
            response, docs = lch.get_response_from_query(db, query)
            st.subheader("")
            st.text(textwrap.fill(response, width=85))

with tab2:
    st.write("\n")
    container = st.container()
    Git = "GitHub: https://github.com/utkarshbansalmailbox/Video-Knowledge-Extraction-via-Large-Language-Model"
    container.write("Made with :blue_heart: & :sweat_drops:  \n Utkarsh Bansal")
    st.divider()
    container.write(Git)

    container = st.container()
    container.write("Configure Application \n")
    st.write("To access app follow the steps below: \n1. Load Project in Editor. \n 02. Under '.env' file enter your OpenAI API key")
    code = ''' OPENAI_API_KEY = 'ENTER YOUR OPENAI API KEY' '''
    st.code(code, language="markdown")
    st.write("3. Install all the required files by typing the command in Terminal mentioned below:")
    code2 = ''' pip install -r requirements.txt '''
    st.code(code2, language="python")
    st.write("4. Compile files \n > LangchainModel.py  \n > main.py \n 5. In Terminal type:")
    code3 = ''' streamlit run main.py '''
    st.code(code3, language="python")



