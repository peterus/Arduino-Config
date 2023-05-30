from typing import List

from .field import Field


def create_header_fields(f: str, fields: List[Field], level: int = 1) -> str:
    for field in fields:
        if field.type == "object":
            f = f + "    " * level + f"class {field.name} {{\n"
            f = f + "    " * level + "public:\n"
            f = create_header_fields(f, field.fields, level + 1)
            f = f + "    " * level + "};\n"
        # elif field.type == "list":
        #    j[field.name] = [create_header_fields(field.fields)]
        elif field.type == "string":
            f = f + "    " * level + f"String {field.name};\n"
        elif field.type == "bool":
            f = f + "    " * level + f"bool {field.name};\n"
        elif field.type == "ip":
            f = f + "    " * level + f"IPAddress {field.name};\n"
        elif field.type == "int":
            f = f + "    " * level + f"int {field.name};\n"
        elif field.type == "double":
            f = f + "    " * level + f"double {field.name};\n"
        else:
            assert True, "missing type"
    return f


def create_header(fields: List[Field]) -> str:
    f = """#ifndef PROJECT_CONFIGURATION_H_
#define PROJECT_CONFIGURATION_H_

class Configuration {
public:
"""

    f = create_header_fields(f, fields)

    f = f + """};

#endif
"""
    return f
