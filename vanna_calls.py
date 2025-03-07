import streamlit as st
#from vanna.remote import VannaDefault
import amb_vanna
from AnaliticaBOT.amb_vanna import AmbVanna


@st.cache_resource(ttl=3600)
def setup_vanna():
    config = {
    "connection_string": "postgresql://postgres.spdwbcfeoefxnlfdhlgi:${{secrets.DBPW}}@aws-0-eu-central-1.pooler.supabase.com:6543/postgres?options=-csearch_path=vector_store",
    "model_name_or_path": "deepseek-ai/DeepSeek-R1-Distill-Llama-8B"
    }
    vn = AmbVanna(config)
    # Me conecto a la base de datos donde esta las tablas con la analitica web del geoportar del AMB
    vn.connect_to_postgres(host='aws-0-eu-central-1.pooler.supabase.com', 
                                  dbname='postgres', 
                                  user='postgres.spdwbcfeoefxnlfdhlgi', 
                                  password='chatbot2025', 
                                  port='6543')



    
    return vn

@st.cache_data(show_spinner="Generating sample questions ...")
def generate_questions_cached():
    vn = setup_vanna()
    return vn.generate_questions()


@st.cache_data(show_spinner="Generating SQL query ...")
def generate_sql_cached(question: str):
    vn = setup_vanna()
    return vn.generate_sql(question=question, allow_llm_to_see_data=True)

@st.cache_data(show_spinner="Checking for valid SQL ...")
def is_sql_valid_cached(sql: str):
    vn = setup_vanna()
    return vn.is_sql_valid(sql=sql)

@st.cache_data(show_spinner="Running SQL query ...")
def run_sql_cached(sql: str):
    vn = setup_vanna()
    return vn.run_sql(sql=sql)

@st.cache_data(show_spinner="Checking if we should generate a chart ...")
def should_generate_chart_cached(question, sql, df):
    vn = setup_vanna()
    return vn.should_generate_chart(df=df)

@st.cache_data(show_spinner="Generating Plotly code ...")
def generate_plotly_code_cached(question, sql, df):
    vn = setup_vanna()
    code = vn.generate_plotly_code(question=question, sql=sql, df=df)
    return code


@st.cache_data(show_spinner="Running Plotly code ...")
def generate_plot_cached(code, df):
    vn = setup_vanna()
    return vn.get_plotly_figure(plotly_code=code, df=df)


@st.cache_data(show_spinner="Generating followup questions ...")
def generate_followup_cached(question, sql, df):
    vn = setup_vanna()
    return vn.generate_followup_questions(question=question, sql=sql, df=df)

@st.cache_data(show_spinner="Generating summary ...")
def generate_summary_cached(question, df):
    vn = setup_vanna()
    return vn.generate_summary(question=question, df=df)
