# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 23:15:55 2024

@author: Sreejit
"""

import streamlit as st

# Page title
st.title("When we first Hugged thik kore")

# Image and text side by side
col1, col2 = st.columns(2)

# Image on the left
image_path = "img2.jpeg"  # Replace with the actual path to your image
col1.image(image_path, use_column_width=True, caption="Our First Proper Hug!!!")

# Text on the right
# Text on the right
col2.write("""
It was our first "date" date, and we did all the things that typical couples do. We looked so perfect that day. You had never been to Victoria Memorial, and although I had been there a few times, going there with you is how I remember Victoria now. 

We talked for hours; you made me a grass ring and placed a flower behind my ear. We joked about how we were making the family sitting in front of us uncomfortable, but at the end of the day, we didn't care. And then... and then we hugged.""")

st.write("""To this day, my heart sinks, my brain stops working, my limbs freeze, and my legs shake, remembering the way you hugged me. I have never felt so loved. You held me so tightly, so close; our hearts touched, and it seemed like we were one. The best part is, even today, when you grab my hands, kiss me, hold me, call my name, or even look at me, I get the exact same feeling.

I want to give you the world because you gave me the world. You're not just a part of my world; you are my world.

Love,
Pookie
""")

st.header("[When we first spent Durga puja and Christmas together](https://rmomumburzxcxjthra9dht.streamlit.app/)")
