from google import genai

client = genai.Client(api_key="your api key")

chat = client.chats.create(
    model="gemini-2.5-flash"
)

print("Gemini Chatbot")
print("Type 'exit' to quit.\n")

while True:
    message = input("You: ")

    if message.lower() == "exit":
        break

    response = chat.send_message(message)

    print("Bot:", response.text)
    print()