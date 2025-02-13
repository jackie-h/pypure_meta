#from meta import Package
#import meta.pure.metamodel.extension as ext
#from meta.pure.metamodel.type import Any
from meta.pure.metamodel.extension import AnnotatedElement


class Referenceable:

    def __init__(self, reference_usages: list["ReferenceUsage"] = None):
        self.reference_usages = [] if reference_usages is None else reference_usages


class ModelElement(AnnotatedElement):

    def __init__(self, name: str = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(stereotypes, tagged_values)
        self.name = name


class PackageableElement(ModelElement, Referenceable):

    def __init__(self, name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        ModelElement.__init__(self, name, stereotypes, tagged_values)
        Referenceable.__init__(self, reference_usages)
        self.package = package

class Package(PackageableElement):

    def __init__(self, children: list["PackageableElement"] = None,
                 name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, package, reference_usages, stereotypes, tagged_values)
        self.children = [] if children is None else children

class PropertyOwner(PackageableElement):

    def __init__(self, name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, package, reference_usages, stereotypes, tagged_values)


class ReferenceUsage:

    def __init__(self, offset: int,
                 owner: "Any",
                 property_name: str):
        self.owner = owner
        self.property_name = property_name
        self.offset = offset
