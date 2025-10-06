from langchain_ollama import OllamaLLM
from langchain.schema import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
 
def analyze_sentiment(text, sentiment=None, num_words=100):
    # Initialize the Ollama LLMs
    sentiment_llm = OllamaLLM(model="gemma3:4b", temperature=0.1)
    text_generator_llm = OllamaLLM(model="gemma3:4b", temperature=0.7) # temperature adjusts creativity of the model's responses

    # Define the prompt templates to tell the LLMs what to do
    prompt_template_sentiment_analyzer = PromptTemplate(
        input_variables=["text"],
        template="Analyze the sentiment of the following text, and return the sentiment as Positive, Negative, or Neutral:{text}Sentiment:"
    )

    prompt_template_text_generator = PromptTemplate( 
        input_variables=["text", "sentiment", "num_words"],
        template="Based on the sentiment '{sentiment}', generate a paragraph of approximately {num_words} words about the following text:\n\n{text}\n\nGenerated Paragraph:"
    )

    # Create the LLM chains
    sentiment_chain = LLMChain(llm=sentiment_llm, prompt=prompt_template_sentiment_analyzer, output_parser=StrOutputParser()) # Using StrOutputParser to get plain text output
    generator_chain = LLMChain(llm=text_generator_llm, prompt=prompt_template_text_generator, output_parser=StrOutputParser()) 

    # First, get the sentiment
    if not sentiment:
        sentiment_response = sentiment_chain.invoke({"text": text})
        # print(sentiment_response)
        sentiment = sentiment_response["text"].strip("\n")

    # Then, generate the paragraph based on the sentiment
    response = generator_chain.invoke({
        "text": text,
        "sentiment": sentiment,
        "num_words": num_words
    })
    # response is a dict with 'text' key
    # Just keep the text part of the response json object
    final_response = response["text"].strip()

    return final_response, sentiment

