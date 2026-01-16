personas = {
    "tutor": {
        "role": "system",
        "content": (
            "You are an AI tutor specialized in NLP and LLMs. "
            "Explain concepts step-by-step using simple language. "
            "Use short paragraphs and examples. "
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
    },
    "other": {
        "role": "system",
        "content": (
            "This is out of the personas. "
            "Please ask a more detailed question. "
        )

    }
}

personas["tutor"]["content"] += (
    "Format answers using bullet points. "
    "Limit responses to 5 bullet max. "
)

def route_persona(user_input):

    text = user_input.lower()

    support_keywords = [
        "crash", "error", "bug", "login", "issue", "problem", "doesn't work", "failed", "help", "support"
    ]

    tutor_keywords = [
        "explain", "what is", "how does", "token", "embedding", "llm", "nlp", "transformer", "attention", "model"
    ]

    if any(k in text for k in support_keywords):
        return "support"
    elif any(k in text for k in tutor_keywords):
        return "tutor"
    else:
        return "other"

def fake_llm(messages, persona):

    user_input = messages[-1]["content"]

    if persona == "tutor":
        # nlp_keywords = [
        #     "nlp", "llm", "token", "tokenization", "embedding", "transformer", "attention", "language model"
        # ]
        bullets = [
                "- Tokenization splits text into smaller units called tokens.",
                "- Tokens can be words, subwords, or characters.",
                "- Models process tokens instead of raw text.",
                "- Tokenization affects model vocabulary and performance.",
                "- Different models use different tokenizers."
        ]
        # if not any(k in user_input for k in nlp_keywords):
        return(
                # "- I can help with NLP and LLM topics only.\n"
                # "- This question is outside my scope.\n"
                # "- Please ask another NLP-related question.\n"
            "\n".join(bullets[:5]) +
            "\nWhat part of tokenization would you like to explore next?"
        )
        
        # return "Tutor-style response(step-by-step)."
    
    elif persona == "support":
        
        # issue_keywords = [
        #     "crash", "error", "bug", "login", "issue", "problem"
        # ]
        # if not any(k in user_input for k in issue_keywords):
            # return(
            #     "Thanks for reaching out. "
            #     "Could you please provide more details about the issue "
            #     "so I can assist you further?"
            # )
        
        return(
            "Sorry you are experiencing this issue. "
            "Please try clearing your app cache and restarting the app. "
            "If the problem persists, I will escalate this to our technical team."
        )
    
    elif persona == "other":
        return(
            "Thanks for your question. "
            "This request doesn't fall under NLP tutoring or product support. "
            "Could you please clarify or provide more details so I can help you."
        )

conversations = {"tutor": [], "support": [], "other": []}

global_conversation = []

MAX_MEMORY = 6

def chat(user_input, persona=None):

    if persona is None:
        persona = route_persona(user_input)    

    if persona not in conversations:
        raise ValueError(f"Unknown persona: {persona}")
    
    user_msg = {
        "role": "user",
        "persona": persona,
        "content": user_input
    }

    conversations[persona].append(user_msg)
    global_conversation.append(user_msg)

    messages = [
        personas[persona],
        *conversations[persona]
    ]

    response = fake_llm(messages, persona)

    assistant_msg = {
        "role": "assistant",
        "persona": persona,
        "content": response
    }

    conversations[persona].append(assistant_msg)
    global_conversation.append(assistant_msg)

    conversations[persona] = conversations[persona][-MAX_MEMORY:]

    return response

def reset_conversation():
    for persona in conversations:
        conversations[persona].clear()

chat("Tell me about token and how we realize the tokenization.")
chat("Where is the capital of France?")

# for m in conversations["tutor"]:
#     print(m["role"], ": ", m["content"])

# print("\n---\n")

# for m in conversations["other"]:
#     print(m["role"], ": ", m["content"])

# print("\n---\n")

# reset_conversation()

chat("My app crashes on login")

# for m in conversations["support"]:
#     print(m["role"], ": ", m["content"])

# print("\nTutor persona instructions:\n")
# print(personas["tutor"]["content"])

for m in global_conversation:
    print(f"[{m['persona']}] {m['role']}: {m['content']}")