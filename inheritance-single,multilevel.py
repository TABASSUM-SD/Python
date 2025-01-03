class vehicle:
    def __init__(self):
        print("hey...! iam the vehicle class constructor....!")
class bike(vehicle):
    def __init__(self):
        super().__init__()
        print("hey...! iam the bike class constructor....!")
class superbike(bike):
    def __init__(self):
        super().__init__()
        print("hey...! iam the super bike class constructor....!")
s1=superbike()        
