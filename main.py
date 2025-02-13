import json

from meta.pure.metamodel.type import Class


class PureContent:

    def __init__(self, classifierPath: str,
                 content: str):
        self.classifierPath = classifierPath
        self.content = content


def object_decoder(obj):
    if 'classifierPath' in obj and obj['classifierPath'] == 'meta::pure::metamodel::type::Class':
        content = obj["content"]

        return Class(**obj["content"])
    return obj

def main():

    with open('../cdm/entities/model/external/cdm/Account.json') as f:
        d = json.load(f, object_hook=object_decoder)
        print(d)

    print("Hello, World!")



if __name__ == '__main__':
    main()
