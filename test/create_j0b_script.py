import requests
import json

# Define the base URL for your local development server
base_url = "http://127.0.0.1:5000"

# Endpoint for creating a job
create_job_endpoint = f"{base_url}/job"

# Employer data obtained from the previous script or any other means
employer_data = {
    "id": "bc1e7f82-26e8-4901-a8b8-9e1352666f8f",
    "company_name": "ALX",
    "industry": "TECH INDUSTRY",
    "email": "alxafrica@gmail.com",
    "age": 30,
    "password": "password"
}

# Job data for creating a job
job_data = {
    "employer_id": employer_data["id"],
    "title": "Waiter",
    "salary": 9000,
    "job_type": "Full-time",
    "description": "Exciting opportunity for a intrested waiter",
    "location": "Nanyuki"
}

# Make a POST request to create the job
response = requests.post(create_job_endpoint, json=job_data)

# Print the response
if response.status_code == 201:
    created_job = response.json()
    print("Job Created:")
    print(f"Job ID: {created_job.get('employer_id')}-{created_job.get('id')}")
    print(f"Title: {created_job.get('title')}")
    print(f"Salary: {created_job.get('salary')}")
    print(f"Job Type: {created_job.get('job_type')}")
    print(f"Description: {created_job.get('description')}")
    print(f"Location: {created_job.get('location')}")
else:
    print(f"Error: {response.status_code}, {response.text}")
