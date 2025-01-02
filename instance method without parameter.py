class Mobile:
    def __init__(self):
        self.model = "result me x"
    def show_model(self):
        print(self.model)
realme = Mobile()
realme.show_model()
r=realme.show_model
print("outside class:",r)            