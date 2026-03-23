import sys
import os
sys.path.insert(0, '.')

print("=" * 60)
print("DIRECT TEST: Importing and calling ask_ai()")
print("=" * 60)

from ai_test import ask_ai

prompt = "How do I become an engineer?"
print(f"\nPrompt: {prompt}")
print("\nCalling ask_ai()...")
result = ask_ai(prompt)
print(f"Result type: {type(result)}")
print(f"Result: {result}")

print("\n" + "=" * 60)
print("Now testing via Flask")
print("=" * 60)

from flask import Flask, make_response
from werkzeug.test import EnvironBuilder
from werkzeug.wrappers import Request

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask_handler():
    data = request.json if request.is_json else {}
    prompt = data.get("prompt")
    print(f"[Flask Handler] Prompt: {prompt}")
    print(f"[Flask Handler] Calling ask_ai()...")
    response_text = ask_ai(prompt)
    print(f"[Flask Handler] Response: {response_text[:100]}...")
    return {"response": response_text}

# Test the handler
from flask import request
with app.test_request_context(
    "/ask",
    method="POST",
    json={"prompt": "How do I become a doctor?"}
):
    print(f"\n[Test] Request method: {request.method}")
    print(f"[Test] Request data: {request.json}")
    result = ask_handler()
    print(f"[Test] Handler returned: {result}")
