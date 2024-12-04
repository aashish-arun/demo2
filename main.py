print("heloooo")

# Class 1 - Doctor Class done by Chris Hanlon
class doctor:
# Initializes the doctor object
    def __init__(self, doctor_id, name, specialization, working_time, qualification, room_number):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number
# Makes all the getters    
    def get_doctor_id(self):
        return self.doctor_id
    def get_name(self):
        return self.name
    def get_specialization(self):
        return self.specialization
    def get_working_time(self):
        return self.working_time
    def get_qualification(self):
        return self.qualification
    def get_room_number(self):
        return self.room_number
# Makes the setters    
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id
    def set_name(self, new_name):
        self.name = new_name
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
    def set_working_time(self, new_working_time):
        self.working_time = new_working_time
    def set_qualification(self, new_qualification):
        self.qualification = new_qualification
    def set_room_number(self, new_room_number):
        self.room_number = new_room_number
# Makes the string output     
    def __str__(self):
        return f"{self.doctor_id}_{self.name}_{self.specialization}_{self.working_time}_{self.qualification}_{self.room_number}"

