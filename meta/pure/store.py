from meta import Package
from meta.pure.metamodel import PackageableElement, ReferenceUsage, Stereotype, TaggedValue


class Store(PackageableElement):

    def __init__(self, includes: list["Store"] = None,
                 name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, package, reference_usages, stereotypes, tagged_values)
        self.includes = [] if includes is None else includes
