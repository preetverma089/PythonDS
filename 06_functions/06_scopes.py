# chai_Type = "Masala Chai"
def serve_chai():
    chai_Type = "Masala Chai" # Local Scope
    def special_chai():
        chai_Type = "Ginger Special" # enclosing Scope
        print(chai_Type)
    special_chai()
    print(chai_Type)
   

serve_chai()

chai_Type = "Lemon Tea"
print(chai_Type)