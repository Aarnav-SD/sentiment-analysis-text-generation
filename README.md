# Internship assessment task
#### NOTE: Deployment may not be possible due to the usage of a local llm that cannot be pushed onto github
## Methodology
1. Used streamlit for frontend UI
2. Used the ollama LLM `gemma3:4b`
3. With the help of LangChain, created a multi-llm workflow
4. `gemma3:4b` takes user input as prompt and returns the sentiment of the prompt (positive, negative or neutral)
5. the same prompt + sentiment from `gemma3:4b` + text legnth constraint is passed to `gemma3:4b` again
6. `gemma3:4b`'s output is 'streamed' to the frontend to simulate a chatbot using `time.sleep()`

## Setup
#### 1. Setup Ollama for local LLM
i. install ollama from <https://ollama.com> and run the setup  
ii. verify installation in command prompt/terminal with `ollama`  
#### 2. Install the llm locally
do the following to install the required llm locally:  
`ollama pull gemma3:4b` (takes about 3.3GB of space)  
verify the installation of the model by `ollama list`, gemma3:4b should show up  
#### 3. Setup dependencies
i. `cd <project location>`  
ii. create a virtual environment (optional but recommended)  
create like this: `python -m venv .venv`  
activate like this: `.venv\Scripts\activate` (for windows)  
iii. install dependencies using `pip install -r requirements.txt`  
iv. before running the app, make sure the model is running, run the model via `ollama run gemma3:4b`  
v. run the frontend app using `streamlit run app.py`  

## App Guide
1. The app consists of one input field where the user should input the text of which the sentiment is to be analyzed (make sure to press enter upon entering the text to make sure the input text field has received the input)
2. By default, the number of words is set to 100, this can, however, be changed with the help of the slider
3. Optionally, the user may manually provide the sentiment using the "Manually select sentiment" checkbox, clicking on the checkbox will reveal a selectbox where the user can select the sentiment of choice
4. Click the analyze sentiment button to then begin generating text
5. Depending on the computational power of the user's device, the time taken may vary
6. The output consists of sentiment and the corresponding generated paragraph
