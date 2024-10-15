# Cold Email Generator using LLMs and Generative A
## Overview
This project is a prototype for generating cold emails tailored to job postings scraped from company websites. Using state-of-the-art Generative AI models (ChatGroq), the app extracts relevant job information (role, skills, experience, etc.) and crafts personalized emails, including links to your portfolio based on the job requirements.

The project is built with:
-  LangChain for chain building and prompt management.
-  Streamlit for the user interface.
-  ChromaDB for storing and querying portfolio links.
-  Generative AI for crafting the emails.

## Features
Features
-  Extract job details from any job posting webpage.
-  Automatically generate cold emails with personalized portfolio links.
-  Clean text data to ensure relevant information is processed.

## Installation
1. Clone the repository.
```bash
git clone https://github.com/your-username/mail-crafter.git
cd mail-crafter
```
2. Create Virtual Environment
```python
python -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate  # For Windows
```
3. Install Dependencies
```python
pip install -r requirements.txt
```
4. Run the app
```pyhton
streamlit run main.py
```
## Usage
- Enter your API Key.
- Paste the job url

## Licence
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
This application utilizes LangChain and Groq for handling language models.
Special thanks to the open-source community for providing powerful libraries and frameworks.