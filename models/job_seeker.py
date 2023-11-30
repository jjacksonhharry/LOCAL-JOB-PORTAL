from models.base_model import BaseModel
from models.job_application import JobApplication

class JobSeeker(BaseModel):
    def __init__(self, sir_name, middle_name, last_name, email, password, age, skills=None, experience=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sir_name = sir_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.age = age
        self.skills = skills or []
        self.experience = experience or 0

    def __str__(self):
        return "[JobSeeker] ({}) {}".format(self.id, self.__dict__)

    def update_skills(self, new_skills):
        self.skills.extend(new_skills)
        self.save()

    def update_experience(self, new_experience):
        self.experience += new_experience
        self.save()

    def look_for_jobs(self, keyword=None, job_type=None, location=None):
        matching_jobs = []
        for job in Job.list_all():
            if (not keyword or keyword.lower() in job.title.lower()) and \
               (not job_type or job_type.lower() == job.job_type.lower()) and \
               (not location or location.lower() == job.location.lower()):
                matching_jobs.append(job)
        return matching_jobs

    def apply_for_job(self, job):
        application = JobApplication(job_seeker_id=self.id, job_id=job.id)
        application.save()
        return application

    def list_applications(self):
        return JobApplication.list_all(filter_condition=lambda app: app.job_seeker_id == self.id)

class JobSeekerAuth:
    job_seekers = []

    @classmethod
    def register(cls, name, email, age, password):
        job_seeker = JobSeeker(name=name, email=email, age=age, password=password)
        cls.job_seekers.append(job_seeker)
        return job_seeker

    @classmethod
    def login(cls, email, password):
        for job_seeker in cls.job_seekers:
            if job_seeker.email == email and job_seeker.password == password:
                return job_seeker
        return None
