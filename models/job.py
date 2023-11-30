from models.base_model import BaseModel

class Job(BaseModel):
    def __init__(self, employer_id, title, salary, job_type, description, location, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.employer_id = employer_id
        self.title = title
        self.salary = salary
        self.job_type = job_type
        self.description = description
        self.location = location
