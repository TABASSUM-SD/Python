class Mobile:
    @classmethod
    def show_model(cls):
        print("result me x")
realme = Mobile()
Mobile.show_model()

print("---------------------------")
class Mobile:
    fp='yes'
    @classmethod
    def show_model(cls):
        print("fingerprint scanner:",cls.fp)
realme = Mobile()
Mobile.show_model()




