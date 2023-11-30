from models.base_model import BaseModel

class JobApplication(BaseModel):
    STATUS_PENDING = "Pending"
    STATUS_ACCEPTED = "Accepted"
    STATUS_DECLINED = "Declined"

    def __init__(self, job_seeker_id, job_id, status=STATUS_PENDING, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_seeker_id = job_seeker_id
        self.job_id = job_id
        self.status = status
