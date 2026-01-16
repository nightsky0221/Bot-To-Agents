from openai import OpenAI

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

client = OpenAI(api_key="YOUR_API_KEY")

def llm_call(messages):
    response = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content

conversations = {"tutor": [], "supprot": []}

MAX_MEMORY = 6

def chat(user_input, persona="tutor"):
    global conversation

    conversation.append({
        "role": "user",
        "content": user_input
    })

    messages = [
        personas[persona],
        *conversation
    ]

    response = llm_call(messages)

    conversation.append({
        "role": "assistant",
        "content": response
    })

    conversation = conversation[-MAX_MEMORY:]

    return response

def reset_conversation():
    global conversation
    conversation = []

chat("Explain tokenization", persona="tutor")
chat("What is the capital of France", persona="tutor")

for m in conversation:
    print(m["role"], ": ", m["content"])

reset_conversation()
print("\n")
chat("My app crashes on login", persona="support")

for m in conversation:
    print(m["role"], ": ", m["content"])

print(personas["tutor"]["content"])