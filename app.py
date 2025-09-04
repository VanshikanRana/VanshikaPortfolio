import streamlit as st
import time
import random
import requests
import json
import base64
from streamlit_lottie import st_lottie

def custom_button(url,color,name):
    st.markdown(f"""
        <style>
        .btn {{
            padding: 10px 25px;
            font-weight: bold;
            border-radius: 6px;
            text-decoration: none !important;
            color: white !important;
            margin: 5px;
        }}
        .btn:hover {{opacity: 0.85;}}
        </style>

        <a href="{url}" class="btn" style="background-color: {color};" target="_blank">{name}</a>
        """, unsafe_allow_html=True)

c,s,c_=st.columns([1,0.01,6])
with c:
    st.write("")
    st.image("VanshikaCodeTrip_Logo.png",width=100)

with c_:
    st.title("Welcome! Hello, I am ")
name="Vanshika"
placeholder=st.empty()
typed=" "
for char in name:
    typed+=char
    placeholder.markdown(f"<h1 stylestyle='text-align: center; color:#FF4B4B;'>{typed}</h1>", unsafe_allow_html=True)
    time.sleep(0.2)
st.markdown("<p style='font-size:25px;'>Currently exploring Data Science, AI & ML ✨</p>", unsafe_allow_html=True)
with open("Welcome.json","r") as f:
    welcome=json.load(f)
st_lottie(welcome,height=400)

st.markdown("# About Me")
st.write("")
st.write("")
st.markdown("I am a Computer Science enthusiast exploring Data Science, AI, and ML. I am passionate about solving problems with Python and data visualization. Open to learning opportunities and internships to grow my skills further.")

col1,col2=st.columns(2)
with col1:
    st.subheader("Personal Information")
    st.markdown("""
**Name:** Vanshika\n
**Education:** Pursuing Btech\n
**Major:** Computer  Science & Engineering\n
**Address:** Ambala,India\n
""")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    c1,c2=st.columns(2)
    with c1:
        custom_button("https://www.linkedin.com/in/ranavanshika2737","#0077B5","LinkedIn")
    with c2:
        custom_button("https://github.com/VanshikanRana","#333333","GitHub")
    st.write("")
    st.write("")
    st.write("")
    col_left, col_center, col_right = st.columns([1,1.5,1])
    with col_center:
        custom_button("mailto:ranavanshika191@gmail.com", "#0F9D58","Email")  # professional green

with col2:
    st.subheader("Skills & Tools")
    st.write("Python")
    st.progress(85)
    st.write("Data Visualization")
    st.progress(90)
    st.write("SQL")
    st.progress(70)
    st.write("Tableau")
    st.progress(60)
    st.write("Power BI")
    st.progress(60)


st.write("")
st.write("")

st.markdown("# Resume")
st.write("")

st.markdown("""
    <div style= 'text-align: justify;'>
            Learning and growing as a Data Scientist with strong skills in Python, AI, and machine learning. Experienced in working on diverse projects involving data analysis and predictive modeling. Eager to keep expanding knowledge and applying it to solve real-world challenges.
    </div>
""",unsafe_allow_html=True)
st.markdown("""<h2 style='text-align: center;'>Trainings</h2>
            <hr style='border: 1px solid #d3d3d3; width: 100%; margin: 1px auto 0 auto;'>""",unsafe_allow_html=True)
st.write("")
st.markdown("""
<style>
.card {
    background-color:#897EBF; 
    color: white;
    padding: 20px;
    border-radius: 12px;
    margin: 10px 15px 10px 15px;
    width: 45%;
    display: inline-block;
    vertical-align: top;
    transition: transform 0.3s ease, box-shadow 0.3s ease; 
}
.card:hover {
    transform: scale(1.05);  /* Slightly increase the size */
    box-shadow: 0 0 20px #6D62A8;  /* Glow effect with light purple */
}
            
.card h3 {
    color: #463973;  /* Dark  Purple for date */
    margin-bottom: 5px;
}

.card h4 {
    margin: 5px 0;
    font-weight: bold;
}

.card h5 {
    margin: 5px 0;
    font-weight: normal;
    color: #aaa;
}

.card ul {
    margin: 10px 0 0 20px;
}
</style>

<div class="card">
    <h3>July–August 2025</h3>
    <h4>The Ultimate Python Bootcamp</h4>
    <h5>Udemy</h5>
    <ul>
        <li>Completed 50+ Python mini projects with practical applications.</li>
        <li>Gained exposure to different coding concepts</li>
        <li>Strengthened coding skills.</li>
        <li>Improved problem-solving mindset.</li>
    </ul>
</div>

<div class="card">
    <h3>July–August 2024</h3>
    <h4>Python and AI</h4>
    <h5>Excellence Technology</h5>
    <ul>
        <li>Covered Python libraries: NumPy, Pandas, Matplotlib, Seaborn.</li>
        <li>Briefly introduced to Scikit-learn.</li>
        <li>Developed a project: CardioVision – Analytical Forecast for Heart Health using Logistic Regression.</li>
        <li>Strengthened skills in EDA, feature engineering, and basic predictive modeling.</li>
    </ul>
</div>
            
<div class="card">
    <h3>August 2023</h3>
    <h4>Artificial Intelligence</h4>
    <h5>Codroid Hub Pvt Ltd</h5>
    <ul>
        <li>Learned Python basics and its applications.</li>
        <li>Explored no-code approaches: Landbot, Teachable Machine.</li>
        <li>Gained exposure to Orange (data mining tool).</li>
        <li>Built a chatbot project using TensorFlow & NLP (with guidance).</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")
st.markdown("""<h2 style='text-align: center;'>Education</h2>
            <hr style='border: 1px solid #d3d3d3; width: 100%; margin: 1px auto 0 auto;'>""",unsafe_allow_html=True)
st.write("")

st.markdown("""
<style>
.card {
    background-color:#897EBF; 
    color: white;
    padding: 20px;
    border-radius: 12px;
    margin: 10px 15px 10px 15px;
    width: 45%;
    display: inline-block;
    vertical-align: top;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.card:hover {
    transform: scale(1.05);  /* Slightly increase the size */
    box-shadow: 0 0 20px #6D62A8;  /* Glow effect with light purple */
}
            
.card h3 {
    color: #463973;  /* Dark  Purple for date */
    margin-bottom: 5px;
}

.card h4 {
    margin: 5px 0;
    font-weight: bold;
}

.card h5 {
    margin: 5px 0;
    font-weight: normal;
    color: #aaa;
}

.school-gap h5 {
    margin-bottom: 35px;  /* adds a line gap after h5 */
}

.card p{
    margin: 10px 0 0 20px;
}
</style>
<div class="card">
    <h3>2022-2026</h3>
    <h4>Bachelor of Engineering</h4>
    <h5>AMABALA COLLEGE OF ENGINEERING AND APPLIED RESEARCH</h5>
    <p>Grade: First Class with Distinction</p>
</div>

<div class="card school-gap">
    <h3>2021-2022</h3>
    <h4>Higher Secondary School</h4>
    <h5>NAND LAL GEETA VIDYA MANDIR SCHOOL</h5>
    <p>Grade: First Class with Distinction</p>
</div>
            
""", unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

with open("_Vanshika_Resume_.pdf", "rb") as file:
    pdf_bytes = file.read()

b64 = base64.b64encode(pdf_bytes).decode()

# HTML button with full styling
st.markdown(f"""
<div style="display: flex; justify-content: center; margin-top: 20px;">
    <a href="data:application/pdf;base64,{b64}" download="Vanshika_Resume.pdf">
        <button style="
            background-color: #897EBF;  /* Purple */
            color: white;               /* White text */
            font-weight: bold;          /* Bold text */
            border-radius: 18px;        /* More curved edges */
            border: none;               /* Remove black border */
            padding: 15px 40px;         /* Larger button */
            font-size: 18px;            /* Bigger text */
            cursor: pointer;
            transition: all 0.3s ease;
        " onmouseover="this.style.backgroundColor='#6D62A8'" 
           onmouseout="this.style.backgroundColor='#897EBF'">
           Download CV
        </button>
    </a>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown("# Projects")
st.write("")

st.write("Below are the sample Data Analytics projects.")

def project_button(title,github_link):
    st.markdown(
        f"""
        <style>
        a.project-link {{
            text-decoration: none !important;
            color: black !important;
            font-weight: 600;
            font-size: 18px;
        }}
        a.project-link:hover {{
            color: #808080 !important;
            text-decoration: underline !important;
        }}
        </style>
        <a class="project-link" href="{github_link}" target="_blank">{title}</a>
        """,
        unsafe_allow_html=True
    )


col3,col4,col5=st.columns(3)

with col3:
    with open("Heart.json","r") as f:
        cardio=json.load(f)
    st_lottie(cardio,height=200)
    project_button("CARDIOVISION","https://github.com/VanshikanRana/CardioVision_Analytical-Forecasts-for-Heart-Health")

with col4:
    with open("B2B.json","r") as f:
        b2b=json.load(f)
    st_lottie(b2b,height=200)
    project_button("B2B LEAD SCORING SYSTEM","https://github.com/VanshikanRana")

with col5:
    with open("Diwali.json","r") as f:
        diwali=json.load(f)
    st_lottie(diwali,height=200)
    project_button("DIWALI SALES ANALYSIS","https://github.com/VanshikanRana/Diwali-Sales-Analysis")

st.write("")
spacer1,col6,spacer2=st.columns([1,1,1])

with col6:
    with open("PowerBI.json","r") as f:
        powerBi=json.load(f)
    st_lottie(powerBi,height=200)
    project_button("HR ANALYTICS DASHBOARD","https://github.com/VanshikanRana/HR-Analytics-Dashboard-Using-Power-BI")

st.write("")
st.write("")
st.write("")
st.markdown("----------------------------")
st.write("")
st.write("")
st.markdown("""<h2 style='text-align: center;'>More projects on Github</h2>""",unsafe_allow_html=True)
st.write("")
st.write("")
st.write("")
st.write("")
sp1,col,sp2=st.columns([3,1.5,3])
with col:
    custom_button("https://github.com/VanshikanRana","#333333","GitHub")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.markdown("---------------------------------------------------")
column1,spacer,column2=st.columns([1,3,1.5])
with column1:
    st.image("VanshikaCodeTrip_Logo.png",width=100)
with column2:
    st.write("")
    st.markdown("#####  VanshikaCodeTrip")
st.markdown("---------------------------------------------------")
def clickable_image(local_path, link_url, width=60):
    # Read the image and convert to base64
    with open(local_path, "rb") as f:
        img_bytes = f.read()
    b64 = base64.b64encode(img_bytes).decode()
    
    st.markdown(
        f"""
        <a href="{link_url}" target="_blank">
            <img src="data:image/png;base64,{b64}" width="{width}">
        </a>
        """,
        unsafe_allow_html=True
    )

email_icon = "email.png"
linkedin_icon = "linkedin.png"
github_icon = "github.png"

s1,col1, col2, col3 = st.columns([8,1,1,1])

with s1:
    st.markdown("**Thanks for traveling my world of code ✨ — Vanshika**")
with col1:
    clickable_image(email_icon, "mailto:ranavanshika191@gmail.com", 40)

with col2:
    clickable_image(linkedin_icon, "https://www.linkedin.com/in/ranavanshika2737", 40)

with col3:
    clickable_image(github_icon, "https://github.com/VanshikanRana", 40)


st.markdown("----------------------------------")
