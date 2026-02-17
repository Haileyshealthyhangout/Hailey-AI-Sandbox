#!/usr/bin/env python3
"""
Sample workflow demonstrating memory persistence and self-reflection.
Run this script in a local environment to see how memory is updated over time.
"""

import json
import os

MEMORY_FILE = "memory.json"

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return {"history": []}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def reflect(memory):
    history = memory.get("history", [])
    if not history:
        return "No prior entries. Start a new conversation."
    last = history[-1]
    return f"Reflecting on {len(history)} entries. Last entry: '{last}'."

def main():
    memory = load_memory()
    print("Welcome to the self-reflection sample. Type 'quit' to exit.")
    while True:
        user_input = input("Say something: ")
        if user_input.lower().strip() == "quit":
            break
        memory["history"].append(user_input)
        save_memory(memory)
        print(reflect(memory))

if __name__ == "__main__":
    main()
