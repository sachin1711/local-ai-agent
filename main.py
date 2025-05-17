from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

def initialize_chain():
    # Initialize the LLM
    model = OllamaLLM(model="gemma3:1b")
    
    # Define the prompt template with history
    template = '''
You are an expert in answering questions about a pizza restaurant.
Always use the chat history to understand the user's intent and provide context-aware answers.
Chat history:
{history}
Here are some relevant reviews of the restaurant: {reviews}
Here is the question to answer: {question}
'''

    
    prompt = ChatPromptTemplate.from_template(template)
    
    # Build the chain
    return prompt | model

# Initialize components for Gradio to import
chain = initialize_chain()
