1. ChatBot - Clothe's Store

A Gradio-powered AI assistant for a clothing store, encouraging customers to explore sales and discounts.
The chat is generated and displayed live in the Gradio interface.
![image](https://github.com/user-attachments/assets/7630c6a4-be52-47c0-bae6-85db6134be21)


2. Company Brochure Bot
   
This bot starts by scraping the company’s homepage and extracting the text content.
It collects all links from the homepage and using the LLM it decides which of them are meanigful for the brochure creation (e.g., "About Us", "Careers") and return them as a JSON file.
Again it fetches the content from all the relevant links that it decided to keep and combines all extracted text into a structured document.
Having all the information from all the relevant links it can now generate the selected company brochure.

The user can choose either a professional tone or a creative one.
The response is generated and displayed live in the Gradio interface.

![image](https://github.com/user-attachments/assets/21d03450-3f3e-46ae-86bf-b9ff45d26ffe)
![image](https://github.com/user-attachments/assets/b97362db-1e04-4b8b-b1ac-022c0acab11b)
