import json

def check_for_test(json_input):
    # Convert JSON string to dictionary if necessary
    if isinstance(json_input, str):
        try:
            json_data = json.loads(json_input)
        except json.JSONDecodeError:
            return "FAIL"
    else:
        json_data = json_input

    # Recursive function to search for the string "Test"
    def search_value(data):
        if isinstance(data, dict):
            return any(search_value(v) for v in data.values())
        elif isinstance(data, list):
            return any(search_value(item) for item in data)
        elif isinstance(data, str):
            return "Test" in data
        return False

    return "PASS" if search_value(json_data) else "FAIL"

# Example usage
json_response = {
    "status": "OK",
    "message": "Test passed successfully",
    "data": {"id": 1, "name": "Sample"}
}

print(check_for_test(json_response))  # Output: PASS
