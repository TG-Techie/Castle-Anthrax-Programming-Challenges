# === Castle-Anthrax-Programming-Challenges ===
# Python Error on assignment:
#   Make the the assignment of x raise an error

# Challenge Author(s): Jonah Yolles-Murphy
# Solution Author(s):
#   Full Name, 01Jan1970, optional twitter, discord, or github

# --- solution ---

# <your code here>
# class Base:
#     ...

# --- test code, (no modification below this line) ---

obj = object()


class MyClass(Base):
    x = obj  # raise some error on the assignmnet of x
    assert False, "inside: this line should not be reached"
