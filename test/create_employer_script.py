import requests
import json

# Define the base URL for your local development server
base_url = "http://127.0.0.1:5000"

# Endpoint for creating an employer
create_employer_endpoint = f"{base_url}/employer"

# Data for creating an employer
employer_data = {
    "company_name": "ALX",
    "industry": "TECH INDUSTRY",
    "email": "alxafrica@gmail.com",
    "age": 30,
    "password": "password"
}

# Make a POST request to create the employer
response = requests.post(create_employer_endpoint, json=employer_data)

# Print the response
print(response.status_code)
employer_id = response.json().get('id')
print(f"Employer ID: {employer_id}")
