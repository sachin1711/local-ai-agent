import gradio as gr
from main import chain, retriever  # Import your chain and retriever

def chat_fn(message, history):
    # Format chat history as a dialogue
    history_text = ""
    for msg in history:
        if msg['role'] == 'user':
            history_text += f"User: {msg['content']}\n"
        elif msg['role'] == 'assistant':
            history_text += f"Assistant: {msg['content']}\n"
    # Add the current user question
    history_text += f"User: {message}\n"

    reviews = retriever.invoke(message)
    review_texts = "\n".join([doc.page_content for doc in reviews])
    response = chain.invoke({
        "history": history_text.strip(),
        "reviews": review_texts,
        "question": message
    })
    return response


# Gradio interface
demo = gr.ChatInterface(
    fn=chat_fn,
    title="Pizza Restaurant Chatbot 🍕",
    type="messages"
)

demo.launch()
