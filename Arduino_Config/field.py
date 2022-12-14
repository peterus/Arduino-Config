
class Field(object):
    def __init__(self, name, type, default=None, fields=None) -> None:
        self.name = name
        self.type = type
        self.default = default
        if fields:
            self.fields = [Field(**f) for f in fields]
        else:
            self.fields = None

    def __str__(self) -> str:
        return f"name: {self.name}, type: {self.type}, default: {self.default}, fields: {[f.__str__() for f in  self.fields] if self.fields else None}"
