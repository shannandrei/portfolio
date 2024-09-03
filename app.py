import streamlit as st
from streamlit_option_menu import option_menu
import base64
import plotly.graph_objects as go
from PIL import Image

st.set_page_config(page_title="Xianna Portfolia", page_icon=":shark:", layout="wide")

project1 = Image.open("assets/classconnect_project.png")
project2 = Image.open("assets/campuseats_project.png")
project3 = Image.open("assets/codetech_project.png")
project4 = Image.open("assets/attendance_project.png")
with open("assets/main.css") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
st.write("##")
st.subheader("Hey there! Welcome :wave:")
st.title("My Portfolio Website")
st.write("Explore my projects and contact me if you want to collaborate!")
st.write("##")


with st.container():
    selected = option_menu(
        menu_title=None,
        options=["About", "Projects", "Contact"],
        icons=["📄", "📂", "📞"],
        default_index=0,
        orientation="horizontal",
    )

if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2, vertical_alignment="center")
        with col2:
            with open("assets/resume.pdf", "rb") as pdf_file:
                pdf_bytes = pdf_file.read()
            st.write("##")
            st.markdown("<h6 style='margin-bottom:0;'>Hello,</h6>", unsafe_allow_html=True)  # Smaller "Hello"
            st.title("I'm Xianna Andrei!")
            st.markdown("<h5>4TH YEAR BSIT STUDENT</h5>", unsafe_allow_html=True)  # Subheader below the name
            st.write("""
            I am a motivated and dedicated college student from Cebu Institute of Technology - University  with a strong passion for web development and machine learning (ML).
            My interests include Artificial Intelligence, Machine Learning, Computer Vision, and Natural Language Processing.
            """)
            st.download_button(
                label="Download Resume",
                data=pdf_bytes,
                file_name="Xianna Andrei Cabaña Resume.pdf",
                mime="application/pdf",
                key="resume-pdf"
            )
        with col1:
            

            with open("assets/img.png", "rb") as img_file:
                img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()

            st.write(f"""
                <div class="container">
                     <div class="box">
                        <div class="spin-container">
                            <div class="shape">
                                <div class="bd">
                                    <img src="{img}" alt="Xianna Andrei">
                                </div>
                            </div>
                        </div>
                     </div>
                </div>
                     """, unsafe_allow_html=True)

            social_icons = {
                "GitHub": ["https://github.com/shannandrei", "https://icon-library.com/images/github-icon-white/github-icon-white-6.jpg"],
                "LinkedIn": ["https://www.linkedin.com/in/xianna-andrei-caba%C3%B1a-8068ab259/", "https://cdn-icons-png.flaticon.com/512/174/174857.png"],
                "Facebook": ["https://www.facebook.com/xiannandrei", "https://cdn-icons-png.flaticon.com/512/733/733547.png"],
                "Instagram": ["https://www.instagram.com/xiannandrei/", "https://cdn-icons-png.flaticon.com/512/2111/2111463.png"],
            }

            social_icons_html = [
                f"<a href='{social_icons[platform][0]}' target='_blank' style='margin-right: 10px;'>"
                f"<img class='social-icon' src='{social_icons[platform][1]}' alt='{platform}'></a>"
                for platform in social_icons
            ]

            st.write(f"""
                <div style="display: flex; justify-content: center; margin-bottom: 20px;">
                    {"".join(social_icons_html)}
                </div>""", unsafe_allow_html=True)

# Skills and "More About Me" section
    with st.container():
        st.write("---")
        st.markdown("<h2 style='text-align: center; font-weight: bold'>Skills</h2>", unsafe_allow_html=True)

        
        col1, col2, col3 = st.columns([1, 1,1])  # Sub-columns inside col1

        with col1:
            # Skills data
            labels = ['Python', 'Java', 'JavaScript', 'HTML', 'CSS', 'C', 'C++']
            values = [4, 6, 7, 8, 8, 5, 5]

            # Creating Radar Chart
            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=labels,
                fill='toself',
                name='Programming Skills',
                line_color='rgb(255, 75, 75)',  # Set the line color to the extracted red color
                fillcolor='rgba(255, 75, 75, 0.3)'
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 9]
                    )),
                showlegend=False
            )

            st.plotly_chart(fig)
            st.markdown("<h5 style='text-align: center'>Languages</h5>", unsafe_allow_html=True)
            

        with col3:
            labels = ['Writing', 'Public Speaking', 'Time Management', 'Problem Solving', 'Communications', 'Multi-tasking']
            values = [4, 6, 7, 8, 8, 7]

            # Creating Radar Chart
            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=labels,
                fill='toself',
                name='Soft Skills',
                line_color='rgb(255, 75, 75)',  # Set the line color to the extracted red color
                fillcolor='rgba(255, 75, 75, 0.3)'
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 9]
                    )),
                showlegend=False
            )

            st.plotly_chart(fig)
            st.markdown("<h5 style='text-align: center'>Soft Skills</h5>", unsafe_allow_html=True)
        
        with col2:
            labels = ['Django', 'React JS', 'Spring', 'Bootstrap', 'React Native', 'Node JS']
            values = [3, 7, 7, 5, 4, 8]

            # Creating Radar Chart
            fig = go.Figure()

            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=labels,
                fill='toself',
                name='Soft Skills',
                line_color='rgb(255, 75, 75)',  # Set the line color to the extracted red color
                fillcolor='rgba(255, 75, 75, 0.3)'
            ))

            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 9]
                    )),
                showlegend=False
            )

            st.plotly_chart(fig)
            st.markdown("<h5 style='text-align: center'>Frameworks</h5>", unsafe_allow_html=True)

if selected == 'Projects':
    with st.container():
        st.header("My Projects")
        st.write("##")

        # Define a smaller width for the project images
        image_width = 300  # Set the desired width (you can adjust this value)

        col4, col5 = st.columns((1, 2))
        with col4:
            st.image(project1, use_column_width=False, width=image_width)  # Set width
        with col5:
            st.subheader("ClassConnect")
            st.write("""
                ClassConnect is a web-based tool that simplifies student life at CIT-U by merging the AIMS portal schedule and event calendar. This integration allows students to easily visualize their class schedules alongside upcoming university events, making planning and staying informed effortless.
            """)
            st.markdown("[View Project](https://github.com/shannandrei/ClassConnect)")

        st.write("---")

        col6, col7 = st.columns((1, 2))
        with col6:
            st.image(project2, use_column_width=False, width=image_width)  # Set width
        with col7:
            st.subheader("CampusEats")
            st.write("""
                CampusEats is a web application that aims to provide a convenient and efficient way for students to order food from the university's vicinity stores. This project was developed using Springboot and ReactJS.
            """)
            st.markdown("[View Project](https://github.com/shannandrei/campus_eats)")

        st.write("---")

        col8, col9 = st.columns((1, 2))
        with col8:
            st.image(project3, use_column_width=False, width=image_width)  # Set width
        with col9:
            st.subheader("CodeTech")
            st.write("""
                CodeTech is a web application that aims to provide a platform for students to learn and practice programming. This project was developed using Springboot and ReactJS.
            """)
            st.markdown("[View Project](https://github.com/gilberx/CodeTech)")

        st.write("---")

        col10, col11 = st.columns((1, 2))
        with col10:
            st.image(project4, use_column_width=False, width=image_width)  # Set width
        with col11:
            st.subheader("FaceTrack Attendance Monitoring System")
            st.write("""
                Facetrack is a convenient web application that streamlines attendance tracking for students. By utilizing facial recognition technology, students can simply log in and have their attendance automatically recorded, eliminating the need for manual sign-in processes.
            """)
            st.markdown("[View Project](https://github.com/Hazelyn123/Applied-AI)")


if selected == 'Contact':
    st.header("Get in Touch")
    st.write("Feel free to reach out to me if you have any questions or if you want to collaborate!")

    contact_form = """
            <form action="https://formsubmit.co/shannnandreibanana@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" required placeholder="Your message"></textarea>
            <button type="submit">Send</button>
            </form>
            """
    left, right = st.columns((2,1))
    with left:
        st.write(contact_form, unsafe_allow_html=True)
    with right:
        st.image("assets/contact.png", use_column_width=True)