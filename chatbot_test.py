conversation = []

system_prompt = {
    "role": "system",
    "content": "You are a helpful AI assistant. Keep answers concise."
}

def chat(user_input):
    conversation.append({"roel": "user", "content": user_input})

    messages = [system_prompt] + conversation

    response = "This is a placeholder response, replace later with real LLM"

    conversation.append({"role": "assistant", "content": response})

    return response

print(chat("Hi"))
print(chat("What is AI?"))
print(chat("Can you explain it simply?"))

print("\nConversation history : ", "\n")
for m in conversation[-8:]:
    print(m["content"])