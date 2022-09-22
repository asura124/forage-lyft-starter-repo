from tires.tires import tires

class CarriganTires(tires):
    def __init__(self,tires_arr):
        self.tires_arr = tires_arr
    
    def needs_service(self):
        for tire in self.tires_arr:
            if(tire >=0.9):
                return True
        return False