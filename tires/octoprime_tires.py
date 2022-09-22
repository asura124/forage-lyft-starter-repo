from tires.tires import tires

class OctoprimeTires(tires):
    def __init__(self,tires_arr):
        self.tires_arr = tires_arr
    
    def needs_service(self):
        return sum(self.tires_arr) >= 3