# === Castle-Anthrax-Programming-Challenges ===
# Python Error on assignment:
#    make assertion fail, you my not clobber or re-define builtins

# Author, Date:
#   Jonah Yolles-Murphy, 08Dec2021, discord: TG-Techie#5402

# --- solution ---


class MyClass:
    def __new__(cls):
        return None


# --- test code, (no modification below this line) ---

x = MyClass()

assert isinstance(
    x, MyClass
), "make this assert fail... so if you're seering this it works!"
