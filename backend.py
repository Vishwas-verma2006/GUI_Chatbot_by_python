from google import genai # type: ignore
# Liabrary to use the gemini api

# Initialize the Gemini client
client = genai.Client(api_key = "YOUR API KEY") # MAKE SURE YOU USE YOUR OWN GEMINI API KEY BEFORE RUN THIS CODE 

# Start the chatbot loop
print("Chatbot is ready! Type 'bye' to exit.\n")

# loop for continuos conversation
def get_response(you):

    while True:
        if you.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        # Send user message to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-pro",
            contents=you
        )

        return response.text
