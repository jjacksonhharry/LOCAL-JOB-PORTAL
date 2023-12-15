from flask import Flask, request, jsonify, render_template
from models.base_model import BaseModel
from models.job import Job
from models.job_seeker import JobSeeker
from models.employer import Employer
from models.job_application import JobApplication
from models.job_seeker_interactions import Message, Review

app = Flask(__name__)

# path to JSON file
BaseModel._FileStorage__file_path = "file.json"

# Set up FileStorage
storage = BaseModel.storage
storage.reload()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/job-applications', methods=['POST'])
def apply_for_job():
    data = request.json
    job_id = data["job_id"]
    job = next((job for job in jobs if job["id"] == job_id), None)

    if job:
        application = {
            "job_seeker_id": data["job_seeker_id"],
            "job_id": job_id,
            "status": "Pending"
        }
        job_applications.append(application)
        return jsonify(application), 201
    else:
        return jsonify({"error": "Job not found"}), 404

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        password = request.form['password']
        job_seeker = JobSeekerAuth.register(name, email, age, password)
        return redirect(url_for('success'))
    return render_template('register.html')

@app.route('/success')
def success():
    return render_template('success.html')

# Routes for jobs
@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = [job.to_dict() for job in storage.all().values()]
    return jsonify(jobs)

@app.route('/job/<job_id>', methods=['GET'])
def get_job(job_id):
    print(f"Attempting to retrieve job with ID: {job_id}")
    job = storage.get(Job, job_id)
    if job:
        print(f"Job found: {job.to_dict()}")
        return jsonify(job.to_dict())
    else:
        print(f"Job not found")
        return jsonify({'error': 'Job not found'}), 404

@app.route('/job', methods=['POST'])
def create_job():
    data = request.json
    employer_id = data.get('employer_id')
    title = data.get('title')
    salary = data.get('salary')
    job_type = data.get('job_type')
    description = data.get('description')
    location = data.get('location')

    if not all([employer_id, title, salary, job_type, description, location]):
        return jsonify({'error': 'Missing data'}), 400

    employer = storage.get(Employer, employer_id)
    if not employer:
        return jsonify({'error': 'Employer not found'}), 404

    job = employer.create_job(title, salary, job_type, description, location)
    return jsonify(job.to_dict()), 201

# Routes for job seekers
@app.route('/job_seekers', methods=['GET'])
def get_job_seekers():
    job_seekers = [job_seeker.to_dict() for job_seeker in storage.all(JobSeeker).values()]
    return jsonify(job_seekers)

@app.route('/job_seeker/<job_seeker_id>', methods=['GET'])
def get_job_seeker(job_seeker_id):
    job_seeker = storage.get(JobSeeker, job_seeker_id)
    if job_seeker:
        return jsonify(job_seeker.to_dict())
    return jsonify({'error': 'Job Seeker not found'}), 404

@app.route('/job_seeker', methods=['POST'])
def create_job_seeker():
    data = request.json
    sir_name = data.get('sir_name')
    middle_name = data.get('middle_name')
    last_name = data.get('last_name')
    email = data.get('email')
    age = data.get('age')
    password = data.get('password')
    skills = data.get('skills')
    experience = data.get('experience')

    if not all([sir_name, middle_name, last_name, email, age, password, skills, password]):
        return jsonify({'error': 'Missing data'}), 400

    job_seeker = JobSeeker(sir_name=sir_name, middle_name=middle_name, last_name=last_name, email=email, age=age, password=password, skills=skills, experience=experience)

    #Add jobseeker to storage
    storage.new(job_seeker)
    storage.save()

    return jsonify(job_seeker.to_dict()), 201

# Routes for employers
@app.route('/employers', methods=['GET'])
def get_employers():
    employers = [employer.to_dict() for employer in storage.all(Employer).values()]
    return jsonify(employers)

@app.route('/employer/<employer_id>', methods=['GET'])
def get_employer(employer_id):
    print(f"Attempting to retrieve employer with ID: {employer_id}")
    employers = storage.all(Employer)
    print(f"All employers in storage: {employers}")

    employer = storage.get(Employer, employer_id)
    if employer:
        return jsonify(employer.to_dict())

    print("Employer not found")
    return jsonify({'error': 'Employer not found'}), 404

@app.route('/employer', methods=['POST'])
def create_employer():
    data = request.json
    company_name = data.get('company_name')
    industry = data.get('industry')
    email = data.get('email')
    age = data.get('age')
    password = data.get('password')

    if not all([company_name, industry, email, age, password]):
        return jsonify({'error': 'Missing data'}), 400

    employer = Employer(company_name=company_name, industry=industry, email=email, age=age, password=password)
    # Add employer to storage
    storage.new(employer)
    storage.save()

    return jsonify(employer.to_dict()), 201

# Routes for job applications
@app.route('/job_applications', methods=['GET'])
def get_job_applications():
    job_applications = [job_app.to_dict() for job_app in storage.all(JobApplication).values()]
    return jsonify(job_applications)

@app.route('/job_application/<job_application_id>', methods=['GET'])
def get_job_application(job_application_id):
    job_application = storage.get(JobApplication, job_application_id)
    if job_application:
        return jsonify(job_application.to_dict())
    return jsonify({'error': 'Job Application not found'}), 404

@app.route('/job_application', methods=['POST'])
def create_job_application():
    data = request.json
    job_seeker_id = data.get('job_seeker_id')
    job_id = data.get('job_id')
    status = data.get('status', JobApplication.STATUS_PENDING)

    if not all([job_seeker_id, job_id]):
        return jsonify({'error': 'Missing data'}), 400

    job_seeker = storage.get(JobSeeker, job_seeker_id)
    job = storage.get(Job, job_id)

    if not job_seeker or not job:
        return jsonify({'error': 'Job Seeker or Job not found'}), 404

    job_application = JobApplication(job_seeker_id=job_seeker_id, job_id=job_id, status=status)
    storage.new(job_application)
    storage.save()

    return jsonify(job_application.to_dict()), 201

@app.route('/messages', methods=['GET'])
def get_messages():
    messages = [message.to_dict() for message in storage.all(Message).values()]
    return jsonify(messages)

@app.route('/message/<message_id>', methods=['GET'])
def get_message(message_id):
    message = storage.get(Message, message_id)
    if message:
        return jsonify(message.to_dict())
    return jsonify({'error': 'Message not found'}), 404

@app.route('/message', methods=['POST'])
def create_message():
    data = request.json
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    content = data.get('content')

    if not all([sender_id, receiver_id, content]):
        return jsonify({'error': 'Missing data'}), 400

    sender = storage.get(JobSeeker, sender_id) or storage.get(Employer, sender_id)
    receiver = storage.get(JobSeeker, receiver_id) or storage.get(Employer, receiver_id)

    if not sender or not receiver:
        return jsonify({'error': 'Sender or Receiver not found'}), 404

    message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    storage.new(message)
    storage.save()

    return jsonify(message.to_dict()), 201

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = [review.to_dict() for review in storage.all(Review).values()]
    return jsonify(reviews)

@app.route('/review/<review_id>', methods=['GET'])
def get_review(review_id):
    review = storage.get(Review, review_id)
    if review:
        return jsonify(review.to_dict())
    return jsonify({'error': 'Review not found'}), 404

@app.route('/review', methods=['POST'])
def create_review():
    data = request.json
    job_seeker_id = data.get('job_seeker_id')
    employer_id = data.get('employer_id')
    rating = data.get('rating')
    feedback = data.get('feedback')

    if not all([job_seeker_id, employer_id, rating, feedback]):
        return jsonify({'error': 'Missing data'}), 400

    job_seeker = storage.get(JobSeeker, job_seeker_id)
    employer = storage.get(Employer, employer_id)

    if not job_seeker or not employer:
        return jsonify({'error': 'Job Seeker or Employer not found'}), 404

    review = Review(job_seeker_id=job_seeker_id, employer_id=employer_id, rating=rating, feedback=feedback)
    storage.new(review)
    storage.save()

    return jsonify(review.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True)

