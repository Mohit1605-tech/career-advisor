import requests
import json

try:
    print("Testing /test endpoint...")
    resp = requests.get("http://localhost:5000/test")
    print(f"Status: {resp.status_code}, Response: {resp.json()}")
    
    print("\nTesting /ask endpoint...")
    resp = requests.post("http://localhost:5000/ask", 
        json={"prompt": "I want to become a doctor"})
    print(f"Status: {resp.status_code}, Response: {resp.json()}")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
