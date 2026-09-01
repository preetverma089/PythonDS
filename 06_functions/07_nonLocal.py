def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type # yha pe m mere iss function ke lexical Scope ko check krke chaiType ko access kr rha hu and usko update kr de rha hu usse kya hoga mere outer function me bhi vo update ho jyega
        chai_type = "Kesar"
        print(chai_type)
    kitchen()
    print(chai_type)

update_order()