#  Set and FrozenSet in python
# set:
# ✅ Unique values rakhta hai
# ✅ Mutable hai
# ❌ Duplicate values nahi rakhta
# ❌ Indexing nahi hoti
# ❌ Slicing nahi hoti
# Order ko rely karke code nahi likhna chahiye
# set ek unordered collection of unique elements hai.
#  in sets data are unique, not giving me duplicate value
# a and b me dono same hote h unko bolte h intersection it means some portion of a and some portion of b called intersection
# duplicates isliye remove hote h ku ki sets internally hashing ka use krta h 
# set me indexing ni hoti Because set ka concept position/index based collection nahi hai.
# agar list me merko 30 in nums check kru to complete list ko traverse krke result dega 
# but sets me Hashing ki wajah se membership lookup average O(1) hota hai.
# set create krne k lie syntax ye h : s = {1, 2, 3}, s = set([1, 2, 3])
# s = {} ye empty set nhi h ye empty dict h 
# s = set() ye h empty set
# methods for sets: add, update(multiple element add krna), remove krna, pop(first element remove krta h ), clear(set ko mempty krna)
# set Operation: A = {1, 2, 3, 4}  B = {3, 4, 5, 6} Union: dono sets ke unique element A | B or A.union(B), Intersecrtion: dono set k same element A & B or A.intersection(B) 
# Diffrence: A - B , A me hain but B me nahi
# Symmetric Difference:  Jo A ya B me hai, but dono me common nahi hai.  A ^ B 
# A = {1,2,3,4}
# B = {3,4,5,6}

# Common = {3,4}

# Symmetric Difference = {1,2,5,6}

# Subset aur Superset 
# A = {1, 2, 3, 4, 5}
# B = {2, 3}
# B, A ka subset hai: B.issubset(A) means A ke andar B ke srre elements h  shortcut: B <= A 
# A, B ka superset hai:  A.issuperset(B) shortcut: A >= B
# Disjoint: ye check krta h ki dono sets me common element nahi hai: isDisjoint()
# A = {1, 2}
# B = {3, 4}

# A.isdisjoint(B)
# Important properties

# Frozen Set: 
# frozenset = immutable set
# fs = frozenset([1, 2, 3]) isme hm add ni kr skte add krne k lie new bnana hoga

# Feature	                       set	             frozenset
# Unique elements	               ✅	               ✅
# Mutable	                       ✅	               ❌
# Add	                           ✅ 	               ❌  
# Remove 	                       ✅	               ❌
# Indexing	                       ❌	               ❌
# Hashable	                       ❌                   ✅
# Dictionary key ban sakta?        ❌	               ✅
# Set ke andar element ban sakta?  ❌	               ✅


# Frozenset hashable kyun hai?

# Python me generally mutable object ko hashable nahi rakh sakte because uska content change ho sakta hai.

# Normal set:

# s = {1, 2, 3}

# change ho sakta hai:

# s.add(4)

# Isliye set hashable nahi hai.

# But:

# fs = frozenset([1, 2, 3])

# change nahi ho sakta.

# Isliye Python usko hash kar sakta hai.

# Final mental model 🧠
# LIST
# ↓
# Ordered
# Duplicates allowed
# Mutable
# Indexing available


# SET
# ↓
# Unique elements
# Mutable
# No indexing
# Fast membership lookup
# Hash-based


# FROZENSET
# ↓
# Unique elements
# Immutable
# No indexing
# Hashable
# Can be dictionary key / set element

# Sabse important distinction:

# set = unique + mutable
# frozenset = unique + immutable


essential_spices = {"cardamom","ginger","cinnamon"}
optional_spcies = {"cloves","ginger","black pepper"}

# union between two objects
all_spices = essential_spices | optional_spcies
print(f"union spices means unique from both{all_spices}")

# intersection
common_spices = essential_spices & optional_spcies
print(f"common_Spices{common_spices}")

# if we want only in essential

only_essential = essential_spices - optional_spcies
print(f"only in essential{only_essential}")