from typing import List
from string import Template
from .field import Field


def read_template(filename):
    with open("Arduino_Config/templates/" + filename) as temp_file:
        return Template(temp_file.read())


header_file = read_template("header.h")
obj = read_template("header_obj.h")


def create_header_fields(fields: List[Field]):
    obj_text = ""
    for field in fields:
        sub_obj = ""
        field_list = ""
        if field.type == "object":
            sub_obj = create_header_fields(field.fields)
        # elif field.type == "list":
        #    j[field.name] = [create_header_fields(field.fields)]
        else:
            field_list = field_list + f"{field.name};\n"
        obj_text = obj_text + obj.substitute(OBJECTNAME=field.name, OBJECT=sub_obj,
                                             CONSTRUCTOR=f"{field.name}() {{}}", FIELDS=field_list)
    return obj_text


def create_header_file(fields: List[Field]):
    text = create_header_fields(fields)
    return header_file.substitute(OBJECT=text)
