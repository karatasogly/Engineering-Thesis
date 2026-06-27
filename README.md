#  Universal Decision AI
*Design and Implementation of a Web-Based Collaborative Decision Support Platform using Cloud Architecture*

An engineering thesis project aimed at solving "decision paralysis" for individuals and groups through an agile, gamified, and cloud-native "swipe" interface.

## Project Overview
Universal Decision AI is a collaborative decision-making platform that simplifies group choices (movies, food, games, activities). Instead of static polls or endless arguments, users swipe left (dislike) or right (like) on dynamically generated cards. 

# Key Features:
* Go Solo (Single Mode):** Quick individual filtering to optimize personal choices.
* Create/Join a Room (Group Mode):** Shared real-time sessions where multiple users swipe simultaneously, generating instant "Matches" when mutual preferences align.
* Cloud-Native Decoupled Architecture:** The system UI does not hold static data; it fetches options dynamically via REST API calls from a remote cloud repository.

---

##  Technical Stack
* Frontend/UI:** Python 3.x + [Streamlit](https://streamlit.io/) (Agile Web Delivery)
* Data Layer:** Remote JSON Cloud Repository (Simulating dynamic decoupled database management)
* Version Control:** Git & GitHub

---

# Repository Structure
* `app.py` - The core functional engine of the web application prototype.
* `Chapter_1_Introduction_Draft.docx` - Academic documentation detailing the background, problem statement, aims, and objectives of the thesis.
* `requirements.txt` - Python project dependencies for environment execution.

---

# Quick Start (Local Execution)

To run the current working prototype on your local machine:

1. Clone the repository:
   ```bash
   git clone [https://github.com/karatasogly/Engineering-Thesis.git](https://github.com/karatasogly/Engineering-Thesis.git)
   cd Engineering-Thesis
