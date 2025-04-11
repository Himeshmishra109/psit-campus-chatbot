from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# 🔐 Your OpenAI API Key here
openai.api_key = "your-api-key-here"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # या gpt-4 अगर plan है
        messages=[
            {"role": "system", "content": "You are a helpful assistant for PSIT college. Answer only PSIT-related questions."},
            {"role": "user", "content": user_input}
        ]
    )

    answer = response.choices[0].message.content
    return jsonify({"response": answer})

if __name__ == '__main__':
    app.run(debug=True)

