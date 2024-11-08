# Article Generator Chatbot

This project is a simple Streamlit-based chatbot designed to generate articles and respond to user queries. It leverages the Google Gemini API to generate high-quality text content using advanced language models.

## Features

- User-friendly interface built with Streamlit for content generation.
- Generates text content based on user-provided queries.
- Utilizes Google GenAI Models for powerful and coherent text generation.
- Quick and reliable text output tailored to user queries.

## Prerequisites

### Ensure you have the following installed:
- Python 3.7 or higher
<!--Code start-->
### Install the required dependencies using pip:
    pip install -r requirements.txt
<!--Code end-->

## How to Run
- Open a terminal and navigate to the project directory.
<!--Code start-->
- Run the Streamlit application:
    streamlit run app.py
<!--Code end-->
- Enter your query into the text input box and click GENERATE to get the generated article content.

## How it Works

The chatbot uses the Google Gemini Model to generate content based on user queries. Here’s a brief breakdown of the core functionality:

- Configuration: Sets up the environment and API key.
- Model: Loads the Google Generative AI model.
- Functionality:
    - get_response(question): Sends the user's query to the model and returns the generated response.
- User Interface: Built with Streamlit to provide an interactive input box and display the generated content.

## Example Usage

### Input:
"What is Artificial Intelligence?"
<!--Code start-->
### Output:
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to
<!--Code end-->

