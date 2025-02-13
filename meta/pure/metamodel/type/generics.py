from meta.pure.metamodel import Referenceable, ReferenceUsage
from meta.pure.metamodel.multiplicity import Multiplicity
from meta.pure.metamodel.type import Type
from meta.pure.metamodel.valuespecification import ValueSpecification


class GenericType(Referenceable):

    def __init__(self, multiplicity_arguments: list["Multiplicity"] = None,
                 raw_type: "Type" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 type_arguments: list["GenericType"] = None,
                 type_parameter: "TypeParameter" = None,
                 type_variable_values: list["ValueSpecification"] = None):
        super().__init__(reference_usages)
        self.raw_type = raw_type
        self.type_parameter = type_parameter
        self.type_variable_values = [] if type_variable_values is None else type_variable_values
        self.type_arguments = [] if type_arguments is None else type_arguments
        self.multiplicity_arguments = [] if multiplicity_arguments is None else multiplicity_arguments


class TypeParameter:

    def __init__(self, name: str,
                 contravariant: bool = None,
                 lower_bound: "GenericType" = None,
                 upper_bound: "GenericType" = None):
        self.name = name
        self.contravariant = contravariant
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound


class InferredGenericType(GenericType):

    def __init__(self, multiplicity_arguments: list["Multiplicity"] = None,
                 raw_type: "Type" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 type_arguments: list["GenericType"] = None,
                 type_parameter: "TypeParameter" = None,
                 type_variable_values: list["ValueSpecification"] = None):
        super().__init__(multiplicity_arguments, raw_type, reference_usages, type_arguments, type_parameter,
                         type_variable_values)
