# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col 

cnx=st.connection("snowflake")
session = cnx.session()
option =st.selectbox('how you want to be contacted',('Email','Phone','Home phone'))
st.write('you selected :', option)

name_on_order = st.text_input('Name on smooth')
st.write('name is :', name_on_order)


my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)


ing_list =st.multiselect('chosse up to 5 ing .',
                         my_dataframe,max_selections=5)

if  ing_list :
   # st.write(ing_list)
   # st.text(ing_list)

    ing_strg=''

    for fruit_chosen in ing_list :
        ing_strg+=fruit_chosen
    #st.write(ing_strg)

    my_insert_stmt = """ insert into smoothies.public.orders(ingredients,name_on_order)
            values ('""" + ing_strg + """','"""+name_on_order+"""' )"""

    #st.write(my_insert_stmt)
    #st.stop()
    time_to_insert=st.button('submit')
    #st.write(my_insert_stmt)
    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!', icon="✅")



        


