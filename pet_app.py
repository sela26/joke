import streamlit as st
import requests

# set up page
st.set_page_config(page_title="Pet App",
                   page_icon="😻")

st.header("WELCOME TO MY PET APP",
          divider='rainbow')

def get_cat_image():
    url = "https://cataas.com//cat"
    # url = "https://cataas.com//cat/gif"
    contents = requests.get(url)
    # you can use whatever api you want to use for your streamlit app
    return contents.content

def get_dog_image_url():
    url = "https://random.dog/woof.json"
    # do some formatting to put it into python
    contents = requests.get(url).json()
    dog_image_url = contents['url']
    # you can use whatever api you want to use for your streamlit app
    return dog_image_url

c1, c2 = st.columns(2)

with c1:
    cat_button = st.button("Click here for a cat image")
    if cat_button:
        cat_image = get_cat_image()
        st.image(cat_image, width=300, caption="Aww, look at this cat...😍")

with c2:
    dog_button = st.button("Click here for a dog image")
    if dog_button:
        dog_image_url = get_dog_image_url()

        # if dog image is an mp4, keep looping through my definition
        while dog_image_url[-4:] == '.mp4':
            dog_image_url = get_dog_image_url()

        st.image(dog_image_url, width=300, caption="Dogs are so cute!")