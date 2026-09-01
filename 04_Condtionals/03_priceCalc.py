glass_size = input("Tell me your prefer size ").lower()

if glass_size=='small':
    print(f"Size for your small size glass is {'10'}")
elif glass_size == 'medium':
    print(f"Size for your medium size glass is {'15'}")
elif glass_size == 'large':
    print(f"Size for your large size glass is {'20'}")
else:
    print("Invalid glass size")