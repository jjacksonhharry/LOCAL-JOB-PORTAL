from models.base_model import BaseModel
from models.job_application import JobApplication

class Employer(BaseModel):
    def __init__(self, company_name, industry, email, password, age, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company_name = company_name
        self.industry = industry
        self.email = email
        self.password = password
        self.age = age

    def __str__(self):
        return "[Employer] ({}) {}".format(self.id, self.__dict__)

    def create_job(self, title, salary, job_type, description, location):
        job = Job(employer_id=self.id, title=title, salary=salary, job_type=job_type, description=description, location=location)
        self.jobs.append(job)
        self.save()
        return job

    def list_jobs(self):
        return self.jobs

    def update_company_info(self, new_name, new_industry):
        # Placeholder method for updating company information
        self.company_name = new_name
        self.industry = new_industry
        self.save()

    def list_applications(self, job):
        return JobApplication.list_all(filter_condition=lambda app: app.job_id == job.id)

class EmployerAuth:
    employers = []

    @classmethod
    def register(cls, company_name, industry, email, age, password):
        employer = Employer(company_name=company_name, industry=industry, email=email, age=age, password=password)
        cls.employers.append(employer)
        return employer

    @classmethod
    def login(cls, email, password):
        for employer in cls.employers:
            if employer.email == email and employer.password == password:
                return employer
        return None
