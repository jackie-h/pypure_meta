#from meta import Package
from meta.pure.metamodel import PackageableElement, ReferenceUsage
#from meta.pure.metamodel.function.property import AbstractProperty
#from meta.pure.metamodel.type import Class, Enumeration, Enum


class ImportGroup(PackageableElement):

    def __init__(self, imports: list["Import"] = None,
                 name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, package, reference_usages, stereotypes, tagged_values)
        self.imports = [] if imports is None else imports


class Import:

    def __init__(self, path: str):
        self.path = path


class ImportStub:

    def __init__(self, id_or_path: str,
                 import_group: "ImportGroup",
                 resolved_node: "Any" = None):
        self.import_group = import_group
        self.id_or_path = id_or_path
        self.resolved_node = resolved_node


class PropertyStub:

    def __init__(self, owner: "Class",
                 property_name: str,
                 resolved_property: "AbstractProperty" = None):
        self.owner = owner
        self.property_name = property_name
        self.resolved_property = resolved_property


class EnumStub:

    def __init__(self, enum_name: str,
                 enumeration: "Enumeration",
                 resolved_enum: "Enum" = None):
        self.enumeration = enumeration
        self.enum_name = enum_name
        self.resolved_enum = resolved_enum
