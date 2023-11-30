from models.base_model import BaseModel

class Message(BaseModel):
    def __init__(self, sender_id, receiver_id, content, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content

    def __str__(self):
        return "[Message] ({}) {}".format(self.id, self.__dict__)


class Review(BaseModel):
    def __init__(self, job_seeker_id, employer_id, rating, feedback, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_seeker_id = job_seeker_id
        self.employer_id = employer_id
        self.rating = rating
        self.feedback = feedback

    def __str__(self):
        return "[Review] ({}) {}".format(self.id, self.__dict__)
