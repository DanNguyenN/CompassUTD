
# Refining and Training the Model

- [ ] Try out different agents Types
- [X] Go through documentation for tools
- [X] Go through the tool kits
- [ ] Combine agents and vector stores
- [X] Tool Retreiver
- [X] Custom LLM agents
- [X] Use a Chat LLM model

# Functionality of the App

- [X] Rate My Professor
- [X] Tell me the difference of the class
- [X] Contact People at my University
- [X] List of all the professor who teach a specific class
- [X] List of all the classes that a professor teaches (Pulled from RMP)
- [ ] List of all the professors that teach a specific class

# Current issues with the app

- [x] The app are not able to filter out answer to it's greetings, and it will get confuse
- [ ] The app sometimes does not know what to do with the answer
- [ ] The results chain does not taken into account of student questions
- [x] You can do prompt injection
- [X] Doesnt know any alumni or Temoc (Pretty disapointing)
- [ ] Currently, it won't be able to answer about course section or who teaching that course
- [ ] It can't answer anything about current event, or about date of thing start (Currently working on it)
- [ ] It sometime do get confuse about the current question, prolly due to chat history not in it
- [ ] It sometime talk about agent max iterations error or time limit error (Need to fix that)
- [X] Add Chat VertTex AI 
- [X] Make sure description are being used in calling for tools

# Notes Prompts

1. Rename the tool Keyword and description for UTD to UTD Course API. This make the model return fewers steps to the example below for Zero Shot React Description  while the description of the function stay the same.

2. Making block and allow list to filter out the prompt before having it go through the model

3. Make a better prompt for the filter template

4. Make a better prompt for the result template
