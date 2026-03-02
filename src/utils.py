# resume class 


class Resume:
    def __init__(self, name , email , skills):
        self.name = name
        self.email = email
        self.skills = skills
        
    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nSkills: {', '.join(self.skills)}"


class JobSeeker(Resume):
    def __init__(self , name , email , skills, experience):
        super().__init__(name , email , skills)
        self.experience = experience
        
    def display_profile(self):
        self.display_profile()
        print(f"Experience: {self.experience}") 


class User:
    def __init__(self, username ):
        self.username = username
        self.resumes = []

    def get_user_info(self):
        return f"Username: {self.username}"
        
    