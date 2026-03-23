#!/usr/bin/env python
import sys
print("=" * 60)
print("TEST: Import and call Flask app directly")
print("=" * 60)

print("\nStep 1: Importing app module...")
import app
print("✓ app module imported successfully")

print("\nStep 2: Getting test client...")
test_app = app.app
test_app.config['TESTING'] = True

print("\nStep 3: Calling /ask endpoint...")
with test_app.test_client() as client:
    resp = client.post('/ask', json={'prompt': 'How do I become an engineer?'})
    print(f"Response status: {resp.status_code}")
    print(f"Response data: {resp.json}")

print("\nDone!")
