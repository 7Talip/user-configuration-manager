def add_setting(settings_dict, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key in settings_dict:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings_dict[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"


def update_setting(settings_dict, setting):
    key, value = setting
    key = key.lower()
    value = value.lower()

    if key not in settings_dict:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

    settings_dict[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"


def delete_setting(settings_dict, key):
    key = key.lower()

    if key not in settings_dict:
        return "Setting not found!"

    settings_dict.pop(key)
    return f"Setting '{key}' deleted successfully!"


def view_settings(settings_dict):
    if not settings_dict:
        return "No settings available."

    lines = ["Current User Settings:"]

    for key, value in settings_dict.items():
        lines.append(f"{key.capitalize()}: {value}")

    return "\n".join(lines)
