import json
import re


from meta.pure.metamodel.type import Class

class PureContent:

    def __init__(self, classifierPath: str,
                 content: str):
        self.classifierPath = classifierPath
        self.content = content


def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def replace_keys_recursive(data):
    if isinstance(data, dict):
        new_data = {}
        for k, v in data.items():
            new_key = to_snake_case(k)
            new_data[new_key] = replace_keys_recursive(v)
        return new_data
    elif isinstance(data, list):
        return [replace_keys_recursive(item) for item in data]
    else:
        return data

def object_decoder(obj):
    if 'classifierPath' in obj and obj['classifierPath'] == 'meta::pure::metamodel::type::Class':
        content = obj["content"]
        content.pop("_type")
        content2 = replace_keys_recursive(content)
        return Class(**content2)
    return obj

def main():

    with open('../cdm/entities/model/external/cdm/Account.json') as f:
        d = json.load(f, object_hook=object_decoder)
        print(d)

    print("Hello, World!")



if __name__ == '__main__':
    main()
