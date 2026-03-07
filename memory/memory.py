read_memory()
write_memory()
import os

MEMORY_FILE = "memory.txt"

def read_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r", encoding="utf-8") as file:
            return file.read()
    return ""

def write_memory(text):
    with open(MEMORY_FILE, "a", encoding="utf-8") as file:
        file.write(text + "\n")