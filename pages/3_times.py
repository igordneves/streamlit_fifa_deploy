import streamlit as st

st.set_page_config(layout="wide")

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index 

club = st.sidebar.selectbox("Clube",clubes)

dt_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

columns = ["Age","Photo","Flag","Overall","Value(£)","Wage(£)","Joined","Height(cm.)","Weight(lbs.)","Contract Valid Until","Release Clause(£)"]

st.dataframe(dt_filtered[columns], 
              column_config={"Photo":st.column_config.ImageColumn("Foto"),
                             "Flag":st.column_config.ImageColumn("Pais"),
                             "Overall":st.column_config.ProgressColumn("Overall",min_value=0,max_value=100, format="%d"), 
                             "Wage(£)":st.column_config.ProgressColumn("Weekly Wage",min_value=0,max_value=dt_filtered["Wage(£)"].max(), format="£%f") 

                             
})