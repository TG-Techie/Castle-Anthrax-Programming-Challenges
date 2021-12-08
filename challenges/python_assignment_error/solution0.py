# === Castle-Anthrax-Programming-Challenges ===
# Python Error on assignment:
#   Make the the assignment of x raise an error

# Challenge Author(s): Jonah Yolles-Murphy
# Solution Author(s):
#   Jonah Yolles-Murphy, 08Dec2021, discord: TG-Techie#5402

# --- solution ---


class RestrictedDict(dict):
    def __setitem__(self, name, value):
        if name == "x":
            raise AttributeError(f"cannot set x, tis a no no")
        else:
            super().__setitem__(name, value)


class BaseMeta(type):
    @classmethod
    def __prepare__(metacls, cls, bases, **kwds):
        return RestrictedDict()


class Base(metaclass=BaseMeta):
    pass


# --- test code, (no modification below this line) ---

obj = object()


class MyClass(Base):
    x = obj  # raise some error on the assignmnet of x
    assert False, "inside: this line should not be reached"
