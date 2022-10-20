import streamlit as st
from PIL import Image
import random
import db
from queries import *

def rec_table_to_posts(resp, add_index=False):
    user_signed_in = st.session_state['logged_in']
    for c, item in enumerate(resp):
            col1, col2 = st.columns([2, 2])
            with col1:
                # col_name: image
                # change this later.. need to fetch the file first
                image = Image.open('coconut.jpeg')
                new_image = image.resize((600, 400))
                st.image(new_image)
                #st.image('https://post.healthline.com/wp-content/uploads/2020/01/coconut-holding-fruit-1200x628-facebook.jpg')
            with col2:
                # col_name: name
                if add_index:
                    st.text(f'#{c + 1}. {item[1]}')
                else:
                    st.text(item[1])
                # col_name: time
                st.text(f'Prep Time: {item[4]} minutes')
                # col_name: calories
                st.text(f'Calories: {item[3]} calories')
                # col_name: cuisine
                st.text(f'Cuisine: {item[2].capitalize()}')
                # col_name: rating
                st.text(f'Rating: {random.randint(65, 100)}')
                if user_signed_in:
                    with st.form('Rate' + str(c)):
                        number = st.number_input('Rate 1-5', min_value=1, max_value=5)
                        submitted = st.form_submit_button("Rate")
                        if submitted:
                            # TODO fix the rating insert issue
                            query_string = user_add_rating.format(4, item[0], number, number)
                            db.query(query_string)
                            print(query_string)
                            st.write("Thanks for your rating!")