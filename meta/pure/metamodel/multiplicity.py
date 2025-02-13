from meta import Package
from meta.pure.metamodel import PackageableElement, ReferenceUsage, Stereotype, TaggedValue


class Multiplicity:

    def __init__(self, lower_bound: "MultiplicityValue" = None,
                 multiplicity_parameter: str = None,
                 upper_bound: "MultiplicityValue" = None):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.multiplicity_parameter = multiplicity_parameter


class MultiplicityValue:

    def __init__(self, value: int = None):
        self.value = value


class PackageableMultiplicity(Multiplicity, PackageableElement):

    def __init__(self, lower_bound: "MultiplicityValue" = None,
                 multiplicity_parameter: str = None,
                 name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None,
                 upper_bound: "MultiplicityValue" = None):
        Multiplicity.__init__(self, lower_bound, multiplicity_parameter, upper_bound)
        PackageableElement.__init__(self, name, package, reference_usages, stereotypes, tagged_values)
