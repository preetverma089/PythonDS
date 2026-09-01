chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
        print(chai_type)
    kitchen()
front_desk()
print(chai_type)