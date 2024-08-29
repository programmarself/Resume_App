import streamlit as st
from PIL import Image

# Load custom CSS
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# IRFAN ULLAH KHAN
##### *Data Scientist | Machine Learning Engineer | Data Engineer | Generative AI Engineer | Google Cloud Professional Certified*
''')

# Display profile image
image = Image.open('dp.png')
st.image(image, width=150)

# Summary section
st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Working on and busy with Data Science, Machine Learning, AI, Cloud Computing.
''')

#####################
# Navigation
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/irfanullahkhanmarwat" target="_blank">IRFAN ULLAH KHAN</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#experience">Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#certifications">Certifications</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)

def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)

def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)
  
def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)

#####################
# Contact Information
st.markdown('''
## Contact
- **Location:** Peshawar, Pakistan
- **Mobile:** +92-3021906646
- **Email:** programmarself@gmail.com
- **LinkedIn:** [irfanullahkhanmarwat](https://www.linkedin.com/in/irfanullahkhanmarwat)
- **Portfolio:** [flowcv.me/ikm](https://flowcv.me/ikm)
- **GitHub:** [programmarself](https://github.com/programmarself)
''')

#####################
# Experience
st.markdown('''
## Experience
''')

txt('**YoungDev Intern**, Python Developer', 'July 2024 - Present')
txt('**TechWithWarriors (Pvt.) Ltd**, Python Developer', 'August 2024 - August 2024')
txt('**CodeClause**, Python Development Intern', 'April 2024 - June 2024')
txt('**Prodigy InfoTech**, Machine Learning Trainee', 'March 2024 - April 2024')
txt('**MeriSKILL**, Data Analyst', 'March 2024 - April 2024')
txt('**Bharat Intern**, Data Science', 'March 2024 - April 2024')
txt('**Mentorness**, Machine Learning Intern', 'March 2024 - March 2024')
txt('**CodSoft**, Machine Learning Engineer', 'February 2024 - March 2024')
txt('**Accenture**, Data Scientist', 'January 2024 - February 2024')
txt('**UTH**, Database Administrator', 'December 2021 - December 2023')
txt('**MB Traders**, Computer Operator', 'August 2020 - December 2021')
txt('**UTH**, Computer System Operator', 'January 2015 - August 2020')

#####################
# Education
st.markdown('''
## Education
''')

txt('**Bachelor of Science - BS**, Computer Science, Virtual University of Pakistan', 'January 2019 - June 2024')
txt('**ICS**, Mathematics and Computer Science, Government Degree College', '')

#####################
# Skills
st.markdown('''
## Skills
''')

txt3('Programming', '`Python`, `R`, `Linux`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `plotly`, `altair`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Deep Learning', '`TensorFlow`')
txt3('Web development', '`Flask`, `HTML`, `CSS`')
txt3('Model deployment', '`streamlit`, `gradio`, `R Shiny`, `Heroku`, `AWS`, `Digital Ocean`')

#####################
# Certifications
st.markdown('''
## Certifications
''')

txt3('Data Analytics Essentials', '')
txt3('IBM Full Stack Software Developer', '')
txt3('Google Cloud Digital Leader Training', '')
txt3('Data Science Foundations', '')
txt3('Generative AI Essentials', '')

#####################
# Honors & Awards and Publications
st.markdown('''
## Honors & Awards
''')

st.markdown('''
- 4x Cisco Certified
''')

st.markdown('''
## Publications
''')

txt3('A Gate Way to Quantum Machine Learning (QML)', '')
txt3('New Era of Actuarial Science', '')

#####################
# Social Media
st.markdown('''
## Social Media
''')

txt2('LinkedIn', 'https://www.linkedin.com/in/irfanullahkhanmarwat')
txt2('GitHub', 'https://github.com/programmarself')
txt2('Portfolio', 'https://flowcv.me/ikm')
