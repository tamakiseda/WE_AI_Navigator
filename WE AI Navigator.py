
import streamlit as st
from streamlit_image_select import image_select

st.markdown("""
    ## Westernacher AI Navigator

#             """)
# img = image_select("Machine Learning", ["classification.png", "regression.png", "clustering.png"])
# st.write(img)
img1 = image_select("Segmentation", ["abc.png", "customer.png", "other.png"],
                    captions=["ABC/XYZ AI Clustering", "Customer AI Clustering", "Others"])
image_urls = {
    "abc.png": "https://xyz-segmentation-westernacher.streamlit.app/",
    "customer.png": "https://xyz-segmentation-westernacher.streamlit.app/",
    "other.png": "https://xyz-segmentation-westernacher.streamlit.app/"
}
url = image_urls.get(img1, "")
#st.image(img)
st.markdown(f"[Check This Link]({url})")

img2 = image_select("Demand Sensing", ["feature.png", "DataExploratoryAnalysis.png", "other.png"],
                    captions=["Feature Engineering", "Data Exploratory Analysis", "Others"])
image_urls = {
    "feature.png": "https://xyz-segmentation-westernacher.streamlit.app/",
    "DataExploratoryAnalysis.png": "https://xyz-segmentation-westernacher.streamlit.app/",
    "other.png": "https://xyz-segmentation-westernacher.streamlit.app/"
}
url = image_urls.get(img2, "")
st.markdown(f"[Check This Link]({url})")

img3 = image_select("AGI", ["PlanningBot.png", "PrivateLLM.png", "other.png"],
                    captions=["Planning Bot", "Private LLM", "Others"])
image_urls = {
    "PlanningBot.png": "https://xyz-segmentation-westernacher.streamlit.app/",
    "PrivateLLM.png": "https://xyz-segmentation-westernacher.streamlit.app/",
    "other.png": "https://xyz-segmentation-westernacher.streamlit.app/"
}
url = image_urls.get(img3, "")
st.markdown(f"[Check This Link]({url})")


# img4 = image_select(
#         label="Select a cat",
#         images=[
#             "abc.png", "customer.png", "other.png"
#         ],
#         captions=["A cat", "Another cat", "Oh look, a cat!"]
#     )


    
