import requests
import json

# Define the base URL for your local development server
base_url = "http://127.0.0.1:5000"

# Endpoint for creating a job seeker
create_jobseeker_endpoint = f"{base_url}/job_seeker"

# Data for creating an employer
jobseeker_data = {
    "sir_name": "Harry",
    "middle_name": "Jack",
    "last_name": "Macharia",
    "email": "hharryjjack@gmail.com",
    "password": "password",
    "age": 21,
    "skills": "Software Engineering",
    "Experience": "Beginner"
}

# Make a POST request to create the job seeker
response = requests.post(create_jobseeker_endpoint, json=jobseeker_data)

# Print the response
print(response.status_code)
jobseeker_id = response.json().get('id')
print(f"JobSeeker ID: {jobseeker_id}")
