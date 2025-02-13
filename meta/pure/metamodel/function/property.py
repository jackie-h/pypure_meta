from enum import auto, Enum

from meta.pure.metamodel import ModelElement, ReferenceUsage, PropertyOwner
from meta.pure.metamodel.function import Function, FunctionDefinition
from meta.pure.metamodel.multiplicity import Multiplicity
from meta.pure.metamodel.type.generics import GenericType
from meta.pure.metamodel.valuespecification import FunctionExpression, ValueSpecification


class AggregationKind(Enum):
    None_ = auto()
    Shared = auto()
    Composite = auto()


class AbstractProperty(Function, ModelElement):

    def __init__(self, generic_type: "GenericType",
                 multiplicity: "Multiplicity",
                 owner: "PropertyOwner",
                 applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        Function.__init__(self, applications, function_name, name, reference_usages)
        ModelElement.__init__(self, name, stereotypes, tagged_values)
        self.generic_type = generic_type
        self.multiplicity = multiplicity
        self.owner = owner


class Property(AbstractProperty):

    def __init__(self, aggregation: "AggregationKind",
                 generic_type: "GenericType",
                 multiplicity: "Multiplicity",
                 owner: "PropertyOwner",
                 applications: list["FunctionExpression"] = None,
                 default_value: "DefaultValue" = None,
                 function_name: str = None,
                 name: str = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(generic_type, multiplicity, owner, applications, function_name, name, reference_usages,
                         stereotypes, tagged_values)
        self.aggregation = aggregation
        self.default_value = default_value


class QualifiedProperty(AbstractProperty, FunctionDefinition):

    def __init__(self, expression_sequence: list["ValueSpecification"],
                 generic_type: "GenericType",
                 id: str,
                 multiplicity: "Multiplicity",
                 owner: "PropertyOwner",
                 applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        AbstractProperty.__init__(self, generic_type, multiplicity, owner, applications, function_name, name,
                                  reference_usages, stereotypes, tagged_values)
        FunctionDefinition.__init__(self, expression_sequence, applications, function_name, name, reference_usages)
        self.id = id


class DefaultValue(ModelElement):

    def __init__(self, function_definition: "FunctionDefinition" = None,
                 name: str = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, stereotypes, tagged_values)
        self.function_definition = function_definition