import json
import re

def parse_text(text):
    data = {}
    
    # Example regex patterns for structured data extraction
    name_match = re.search(r'Name:\s*([A-Za-z ]+)', text)
    age_match = re.search(r'Age:\s*(\d+)', text)

    data["Name"] = name_match.group(1) if name_match else "Unknown"
    data["Age"] = age_match.group(1) if age_match else "Unknown"
    
    return json.dumps(data, indent=4)

# Example usage
# text = extract_text_from_image("sample.jpg")
# print(parse_text(text))
