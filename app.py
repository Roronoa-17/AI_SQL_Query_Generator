import streamlit as st 
import google.generativeai as genai


genai.configure(api_key="AIzaSyCsaug0GuW8RbH3o-vCKpkFMOCDkEOoX94")

model = genai.GenerativeModel('gemini-pro')



st.set_page_config(page_title="AI SQL Query Generator")
st.markdown(
    """ 
    <div style="text-align:center;">
    <h1> SQL Query Generator using LLM </h1>
    <h3>This tool can generate SQL queries for given prompt</h3>
    <h3>With Explanation of Queries </h3>
    </div>
    """,
    unsafe_allow_html=True, 
)

text_input = st.text_area("Enter you Query here:")

submit = st.button("Generate SQL Query")

if submit:
    with st.spinner("Generating SQL Query..."):
        template = """ 
        Generate a SQL query for 
        '''
        {text_input}
        '''
        Also explain the query and concepts used in generated query.
        """
        formatted_template = template.format(text_input=text_input)
        
        # st.write(formatted_template)
        response = model.generate_content(formatted_template)
        sql_query = response.text
        st.write("Generated query with explaination: ")
        st.write(sql_query)   
    
