import datetime
import time
import streamlit as st

st.title("Welcome To Pythone")

st.image("Python.jpg",)


st.text("Python is a high-level, easy-to-read programming language used for building websites, apps, data analysis, AI, and more. It focuses on simplicity and readability, making it great for both beginners and experts.")
st.write("👈Select a demo from the dropdown on the left to see some examples of what Python can do!")
st.markdown("""
### Want to Learn More
-  Pythone - [Pythone.io](https://www.mcdonalds.com/)  
-  Jump into Over - [Documentation]()  
""")




demo = st.title("Professional Features:") 
with demo:
   st.markdown("""
### Unit Converter
- 📚 Comprehensive Python Curriculum
- ✍️ Industry-Standard Examples
- 📝 Professional Certification Preparation
- 🎯 Real-world Projects
- 🎮 Interactive Learning Tools
- 📱 Enterprise-level Projects
- 💻 Advanced Code Challenges
- 🏆 Industry Recognition
- 👥 Professional Network
- 📺 Expert Video Tutorials
""")
   
#    Image
st.image("Capture.GIF", width=700)
   
    # Premium Features

st.title("�� Premium Features:")

st.markdown("""
### 🎓 Enterprise Learning:
- Industry-standard tutorials
- Expert-led sessions
- Professional exercises

""")

st.markdown("""
### 🏆Professional Development:
- Industry challenges
- Enterprise projects
- Certification prep

""")

st.markdown("""
### 👥Network:
- Professional community
- Expert consultation
- Industry connections

""")

 # Career Path
st.subheader("🚀 Career Roadmap")
st.info("Choose your specialized career path in Python development")
    
    # Industry Updates
st.subheader("📢 Industry Updates")
st.success("New Enterprise Python courses available!")
st.success("Industry-recognized certification tracks open!")
    
    # Professional Tips
st.subheader("💡 Professional Best Practices")
tips = [
        "Implement design patterns effectively",
        "Follow PEP 8 style guidelines",
        "Use proper error handling",
        "Practice test-driven development",
        "Optimize code performance",
        "Implement security best practices"
    ]
st.info(tips[int(time.time()) % len(tips)])
   
    


# information
info = st.sidebar.title("Contect Information")
navigation = st.sidebar.title("📌 Pythone Project")
feedback = st.sidebar.expander("💬 Feedback")
# Navigation
genre = st.sidebar.radio(
    "What's your favorite movie genre",
    [":rainbow[Home]",
              "Learning Path",
              "Practice Lab",
              "Assessments",
              "Enterprise Projects",
              "Interactive Tools",
              "Professional Network",
              "About Us"],
    index=None,
)

st.sidebar.write("You selected:", genre)




# feed
with feedback:
    user_feedback = st.text_area("Leave your feedback:")
    if st.button("Submit Feedback"):
        st.sidebar.success("Thank you for your feedback!")
        
         
with info:
    st.sidebar.markdown("""
                        ****
                   
                        Join our professional network  
                        Follow us on LinkedIn  
                        Email: areejzaheer96@gmail.com
                        
""")        