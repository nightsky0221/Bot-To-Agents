This project implements typical chatbot logic, demonstrating how to use a chatbot and how to respond to user requests.
As you know, when a user makes a request, a specific process is required to understand and respond.

This project clearly demonstrates this process and teaches you how to manage a Learning Leadership Machine (LLM).

Typical chatbot logic is as follows:

    1. Receive user input as a string and analyze the request type.
    2. Send user input data and system prompts to LLM.
    3. LLM generates an appropriate response based on the user input and persona.
    4. LLM sends the response to the user.

1. Receiving and Analyzing User Input

When receiving user input, the first step is to determine the scope of the request. That is, what the request is about and what is required to process it.

Therefore, we define personas such as "Tutor," "Support," and "Other."

Requests related to NLP were classified as the "Tutor" persona, while product support requests were classified as the "Support" persona. Since this project focused on NLP technical support and product support requests, requests that weren't NLP- or product-related were politely declined using the "Other" persona.

We implemented a feature that automatically selects an appropriate persona by analyzing user input.

2. Sending User Data to the Local Learning Machine (LLM)

Once a persona matching the user input is identified, the user input is sent to the LLM along with the persona data. The LLM then provides the user with an appropriate response.
To prevent the chatbot from becoming confused after a long conversation, persona data must be sent with every user input. Over time, chatbots can easily encounter requests that naturally deviate from their scope or lose track of conversation history. To address this issue, persona data is always sent along with user input data, and only the most recent conversation data is used to reduce memory usage.

3. Generate Appropriate Responses

Based on the data sent by the chatbot, LLM identifies the correct answer. After identifying the persona, it generates a more specialized response to the user's request.

4. LLM returns the response and displays it to the user.

Once LLM sends the response to the chatbot, it is immediately displayed to the user.
The conversation history browser provides both general and selective modes, allowing users to view the entire conversation history by persona or partial conversation history for a specific persona.

That's all. Enjoy using our chatbot, and if you encounter any issues, no matter how minor, please let us know immediately. We will continuously update the chatbot to provide you with a more useful service.

Thank you.