# 🧩 User Configuration Manager (Python)

A lightweight Python project for managing user configuration settings such as **theme**, **notifications**, and **volume**.  
Built as part of a certification project with a focus on **clean code**, **test-driven development**, and **Pythonic design**.

---

## 🚀 Features

- Add new settings with validation  
- Update existing settings  
- Delete settings safely  
- View all settings in a formatted, user-friendly output  
- Case-insensitive key handling  
- Fully test-compliant implementation  

---

## 🛠️ Technologies & Concepts

- Python 3
- Dictionaries (CRUD operations)
- Tuple unpacking
- String normalization (`lower`, `capitalize`)
- Control flow & validation
- Test-oriented development
- Clean and reusable function design

---

## 📦 Example Usage

```python
from config_manager import (
    add_setting,
    update_setting,
    delete_setting,
    view_settings
)

settings = {}

print(add_setting(settings, ("Theme", "Dark")))
# Setting 'theme' added with value 'dark' successfully!

print(update_setting(settings, ("Theme", "Light")))
# Setting 'theme' updated to 'light' successfully!

print(add_setting(settings, ("Volume", "High")))
# Setting 'volume' added with value 'high' successfully!

print(view_settings(settings))
```
Output

Current User Settings:
Theme: light
Volume: high
---

## ✅ Implemented Functions

- `add_setting(settings_dict, (key, value))`
- `update_setting(settings_dict, (key, value))`
- `delete_setting(settings_dict, key)`
- `view_settings(settings_dict)`

Each function follows a consistent pattern:

**normalize → validate → process → return message**

---

## 🧠 What This Project Demonstrates

- Translating user requirements into working Python code  
- Strong understanding of Python data structures  
- Writing predictable, test-friendly functions  
- Attention to edge cases and exact output formatting  
- Clean separation between logic and data  

---

## 🧪 Testing

The implementation passes strict automated tests, including:

- Exact string matching  
- Edge case handling  
- Dictionary mutation checks  
- Newline-sensitive output formatting  

---

## 📁 Project Structure

user-configuration-manager/
├── config_manager.py
├── README.md
└── examples.py # optional demo script

---

## 📌 Why This Project Matters

This project reflects real-world backend logic commonly found in:

- Configuration managers  
- CLI tools  
- Settings handlers  
- Small backend services  

It focuses on correctness, clarity, and maintainability rather than unnecessary complexity.

---

## 👤 Author

**Muhammed Ebrar Arslan**  
Python Learner | AI / ML Engineering Path
