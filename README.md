# prompt_classifier_client

This program uses gradio client to consume an api built upon gradio.

How to use:

1. Copy the list of prompts for which you want to determine its classification.

2. Run client.py.

3. client.py calls the api to determine the classification of the prompt and appends the classification to the prompt and saves it in the output.csv file.

format: [classification] '|' [original prompt]
