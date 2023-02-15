# ChatBot-python
This an ai-based python chatbot. This an example of an basic ai program.

# Practical Understanding -
## Modules used- 
 - [Random](https://docs.python.org/3/library/random.html)
 - [Wikipedia](https://pypi.org/project/wikipedia/)
 - [Time](https://docs.python.org/3/library/time.html)
 
 ## Working 
 The '''generate_response''' function takes the user's input, checks it against the keywords defined in the various functions, and returns an appropriate response based on the highest-priority keyword matched.
 
 ## Pros-
- The code is written in Python, a widely used and popular programming language.
* The chatbot responds to different types of inputs, such as greetings, inquiries about the user's well-being, and questions asked by the user.
+ The chatbot uses the Wikipedia API to answer user questions.
- The chatbot provides a default response when it doesn't understand the user's input.
* The code is easy to understand and modify if needed, with each function focusing on a specific keyword or phrase and returning a corresponding response.
## Cons-
- The chatbot's responses are limited to specific keywords or phrases, which may not cover all possible user inputs.
* The chatbot's use of the Wikipedia API may not always return the most accurate or up-to-date information.
+ The chatbot is limited to text-based communication and cannot respond to voice or visual inputs.

# Theoretical Understanding- 
+ Introduction to the chatbot:

  The chatbot is a program written in Python that can communicate with users by interpreting and responding to text-based inputs. The chatbot is designed to respond to certain keywords or phrases, such as greetings, inquiries about the user's well-being, and questions asked by the user. The chatbot is also capable of using the Wikipedia API to provide information and answer user questions.

  The purpose of the chatbot is to provide a user-friendly and interactive experience for those who interact with it. By responding to user inputs in a conversational manner, the chatbot can create a more engaging and personalized experience for the user. The chatbot can also be used in a variety of settings, such as customer service, education, and entertainment, among others.

  The chatbot's functionality and capabilities can be further developed and improved with additional programming and integration with other tools and technologies. Ultimately, the chatbot has the potential to be a powerful and versatile tool for interacting with users in a variety of contexts.

* Features of the chatbot include:

  - Greeting: The chatbot can greet the user with various responses such as "hi", "hello", and "hey".

  - Responding to inquiries: The chatbot can respond to inquiries about the user's well-being with responses like "I'm good, thanks for asking!" and "I'm doing well, thanks!".

  - Responding to other phrases: The chatbot can respond to certain phrases like "nice", "good", and "great" with responses like "yes" and "yeah".

  - Answering user questions: The chatbot can respond to the user's request to ask a question by using the Wikipedia API to provide information and answer the user's question.

  - Exiting the chat: The user can exit the chat by typing "exit".
+ Design and Development - 
  A simple chatbot that can respond to certain user inputs using pre-defined responses. The chatbot is designed to work in a loop, continuously accepting input from the user and generating responses until the user chooses to exit the program.

  The chatbot uses several functions to determine the appropriate response based on the user's input. For example, the `greetings` function uses a for loop to iterate through the words in the user's input and check if any of them match pre-defined greetings. If a match is found, the function returns a random greeting from a list of possible responses.

  Similarly, the `inquiry` function checks if the user's input contains any pre-defined inquiry phrases, and if a match is found, returns a random response from a list of possible answers.

  The chatbot also includes functions to respond to certain other phrases and to answer user questions using the Wikipedia API. The `generate_response` function calls these functions based on the user's input to determine the appropriate response.

  Finally, the chatbot includes a `while` loop that continuously accepts input from the user and generates responses until the user types "exit" to terminate the program.

  Overall, the code is a simple demonstration of how a chatbot can be built using Python, but there is certainly room for further development and improvement, such as adding more features, improving the natural language processing, and enhancing the user experience.
