personas = {
    "tutor": {
        "role": "system",
        "content": (
            "You are an AI tutor specialized in NLP and LLMs. "
            "Explain concepts step-by-step using simple language. "
            "Use short paragraphs and examples. "
            "If a request is outside NLP, politely refuse. "
            "Ask one follow-up question after each answer. "
        )
    },
    "support": {
        "role": "system",
        "content": (
            "You are a customer support agent. "
            "Be polite, concise, and solution-focused. "
            "Only answer questions related to product. "
            "If you don't know the answer, escalate politely. "
        )
    }
}

personas["tutor"]["content"] += (
    "Format answers using bullet points. "
    "Limit reponses to 5 bullet max. "
)

conversation = []

MAX_MEMORY = 6

def chat(user_input, persona="tutor"):

    global conversation
  
    user_msg = {
        "role": "user",
        "content": user_input
    }

    conversation.append(user_msg)

    messages = [
        personas[persona],
        *conversation
    ]

    print("\n--- PROMPT SENT TO LLM ---\n")
    for m in messages:
        print(f"{m['role'].upper()}: {m['content']}")

    print("--- END PROMPT ---\n")

#     response = "Placeholder response from LLM"

#     assis_msg = {
#         "role": "assistant",
#         "content": response
#     }

#     conversation.append(assis_msg)

#     conversation = conversation[-MAX_MEMORY:]

#     return response

# def reset_conversation():
#     global conversation
#     conversation = []

chat("Explain tokenization", persona="tutor")
chat("What is the capital of France", persona="tutor")