---
layout: default
title: "Mail Crafter"
---

# Mail Crafter: A Cold Email Generator Using Generative AI
In this article, we'll explore the development of *Mail Crafter*, a Streamlit application that generates personalized cold emails for job applications. Leveraging advanced language models and document processing techniques, this application allows users to input job listing URLs, extract relevant job information, and automatically generate tailored emails. The app utilizes the LangChain framework and integrates the ChatGroq model for powerful language generation capabilities.

## Key Features of the App

- **User-Friendly Interface**: The app is designed with an intuitive UI that allows users to input job listing URLs easily.
- **Job Information Extraction**: By scraping the content from job postings, the app extracts relevant details such as the role, required skills, and job description.
- **Dynamic Email Generation**: The app generates a professional email tailored to the job description and the user's portfolio links, enhancing the chances of getting noticed.
- **API Key Integration**: Users can securely enter their GROQ API key for authentication to access the language model.

Let's dive into the details of how this works.

## Setting up the Environment

The core libraries and tools used in this app are:

- **Streamlit**: A Python framework for building interactive web applications.
- **LangChain**: A framework that connects language models to various data sources for enhanced applications.
- **ChatGroq API**: Provides access to the LLaMA-based ChatGroq language model for generating text.
- **Chromadb**: Used for storing portfolio information in a vector database.

Before starting, install the required dependencies:
```bash
pip install streamlit langchain langchain_groq langchain_community chromadb python-dotenv

Additionally, you should acquire a GROQ API key from https://console.groq.com.
```
## Application Structure

API Key Configuration

The application starts by asking the user to provide their GROQ API key. This key is crucial as it allows access to the language model. Here’s how the API key input is managed:
```python
# Input for API key (hidden with password field)
api_key = st.sidebar.text_input("Enter your GROQ API Key", type="password")

# If API key is not provided, show a warning message
if not api_key:
    st.sidebar.warning("Please enter your GROQ API Key to proceed.")
else:
    st.sidebar.success("API Key entered successfully!")
```
This block ensures users cannot proceed without entering their API key, promoting a secure setup for the application.

## URL Input and Job Data Processing

Users can input a URL from a job posting. The app uses WebBaseLoader from LangChain to fetch and load the content of the provided URL. The following code block handles the URL input:
```pyhton
url_input = st.text_input("Enter a URL:", value="Type or paste your job listing URL here")
```
The placeholder text serves as guidance for users without being persistent text.

Once the URL is provided and submitted, the application retrieves the job data:
```
if submit_button:
    loader = WebBaseLoader([url_input])
    data = clean_text(loader.load().pop().page_content)
```
The `clean_text` function processes the fetched data to ensure it is ready for extraction. It removes HTML tags, special characters, and unnecessary whitespace to improve the accuracy of the job extraction process.
Extracting Job Information

The extracted job data is then processed to identify key details such as role, experience, skills, and description using a prompt template:
```python
jobs = llm.extract_jobs(data)
```
This method invokes the language model to return structured job information in JSON format.

## Dynamic Email Generation
With the job details extracted, the application generates a cold email based on the retrieved information and user portfolio links:
```python
email = llm.write_mail(job, links)
```
This code block composes a professional email that includes a subject line, greeting, body text, and sender details, ensuring the final output resembles a well-structured email.

## Deploying the App
To deploy the app, you can use Streamlit Cloud. Here’s a quick guide on how to get the app running:
1. Create a GitHub Repository: Push the app's code to a GitHub repository.
2. Streamlit Cloud Deployment: Go to Streamlit Cloud and connect your GitHub repository. Streamlit Cloud will automatically detect the Streamlit app file and deploy it for you.
3. Environment Variables: If you want to avoid requiring users to enter the API key every time, set the `GROQ_API_KEY` as an environment variable in the Streamlit Cloud settings.
4. Accessing the App: Once deployed, users can access the app through the provided Streamlit Cloud URL.

## Real-World Practicality

The Mail Crafter application addresses a common challenge faced by job seekers—crafting personalized cold emails. In a competitive job market, standing out to potential employers is crucial. This tool enhances users' chances by providing tailored emails that reflect the specific requirements of job postings. By automating the email generation process, it saves time and ensures that users can focus on other aspects of their job search.

The application can be extended to integrate additional features such as:
- Multiple Email Templates: Allow users to choose from different email templates based on their preferences.
- Portfolio Upload: Enable users to upload their resumes or portfolios for automatic link inclusion.
- Analytics Dashboard: Provide users with insights on their email open rates or responses to track effectiveness.

Feel free to fork the project, customize it with additional features, and deploy it to fit your specific needs. Happy coding!
