from typing import List
from .field import Field


def create_default_fields(fields: List[Field]):
    j = {}
    for field in fields:
        if field.type == "object":
            j[field.name] = create_default_fields(field.fields)
        elif field.type == "list":
            j[field.name] = [create_default_fields(field.fields)]
        else:
            j[field.name] = field.default

    return j
