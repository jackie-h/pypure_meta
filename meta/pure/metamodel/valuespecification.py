
#from meta.pure.metamodel.function import FunctionDefinition, Function
from meta.pure.metamodel.multiplicity import Multiplicity
#from meta.pure.metamodel.type import FunctionType, Type
from meta.pure.metamodel.type.generics import GenericType
from meta.pure.store import Store
from meta.pure.metamodel.import_ import ImportGroup


class ValueSpecification:

    def __init__(self, generic_type: "GenericType",
                 multiplicity: "Multiplicity",
                 usage_context: "ValueSpecificationContext" = None):
        self.generic_type = generic_type
        self.multiplicity = multiplicity
        self.usage_context = usage_context


class Expression(ValueSpecification):

    def __init__(self, generic_type: "GenericType",
                 multiplicity: "Multiplicity",
                 usage_context: "ValueSpecificationContext" = None):
        super().__init__(generic_type, multiplicity, usage_context)


class VariableExpression(Expression):

    def __init__(self, generic_type: "GenericType",
                 multiplicity: "Multiplicity",
                 name: str,
                 function_type_owner: "FunctionType" = None,
                 usage_context: "ValueSpecificationContext" = None):
        super().__init__(generic_type, multiplicity, usage_context)
        self.name = name
        self.function_type_owner = function_type_owner


class InstanceValue(ValueSpecification):

    def __init__(self, generic_type: "GenericType",
                 multiplicity: "Multiplicity",
                 usage_context: "ValueSpecificationContext" = None,
                 values: list["Any"] = None):
        super().__init__(generic_type, multiplicity, usage_context)
        self.values = [] if values is None else values


class ValueSpecificationContext:

    def __init__(self, offset: int):
        self.offset = offset


class NonExecutableValueSpecification(ValueSpecification):

    def __init__(self, generic_type: "GenericType",
                 multiplicity: "Multiplicity",
                 usage_context: "ValueSpecificationContext" = None,
                 values: list["Any"] = None):
        super().__init__(generic_type, multiplicity, usage_context)
        self.values = [] if values is None else values


class ExpressionSequenceValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, function_definition: "FunctionDefinition",
                 offset: int):
        super().__init__(offset)
        self.function_definition = function_definition


class InstanceValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, instance_value: "InstanceValue",
                 offset: int):
        super().__init__(offset)
        self.instance_value = instance_value


class ClassConstraintValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset: int,
                 type_: "Type"):
        super().__init__(offset)
        self.type_ = type_


class ParameterValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, function_expression: "FunctionExpression",
                 offset: int):
        super().__init__(offset)
        self.function_expression = function_expression


class FunctionExpression(Expression):

    def __init__(self, func: "Function",
                 generic_type: "GenericType",
                 import_group: "ImportGroup",
                 multiplicity: "Multiplicity",
                 function_name: str = None,
                 original_milestoned_property: "Function" = None,
                 original_milestoned_property_parameters_values: list["ValueSpecification"] = None,
                 parameters_values: list["ValueSpecification"] = None,
                 property_name: "InstanceValue" = None,
                 qualified_property_name: "InstanceValue" = None,
                 resolved_multiplicity_parameters: list["Multiplicity"] = None,
                 resolved_type_parameters: list["GenericType"] = None,
                 usage_context: "ValueSpecificationContext" = None):
        super().__init__(generic_type, multiplicity, usage_context)
        self.func = func
        self.import_group = import_group
        self.parameters_values = [] if parameters_values is None else parameters_values
        self.function_name = function_name
        self.property_name = property_name
        self.qualified_property_name = qualified_property_name
        self.original_milestoned_property = original_milestoned_property
        self.original_milestoned_property_parameters_values = [] if original_milestoned_property_parameters_values is None else original_milestoned_property_parameters_values
        self.resolved_type_parameters = [] if resolved_type_parameters is None else resolved_type_parameters
        self.resolved_multiplicity_parameters = [] if resolved_multiplicity_parameters is None else resolved_multiplicity_parameters


class KeyValueValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, function_expression: "FunctionExpression",
                 offset: int):
        super().__init__(offset)
        self.function_expression = function_expression


class SimpleFunctionExpression(FunctionExpression):

    def __init__(self, func: "Function",
                 generic_type: "GenericType",
                 import_group: "ImportGroup",
                 multiplicity: "Multiplicity",
                 function_name: str = None,
                 original_milestoned_property: "Function" = None,
                 original_milestoned_property_parameters_values: list["ValueSpecification"] = None,
                 parameters_values: list["ValueSpecification"] = None,
                 property_name: "InstanceValue" = None,
                 qualified_property_name: "InstanceValue" = None,
                 resolved_multiplicity_parameters: list["Multiplicity"] = None,
                 resolved_type_parameters: list["GenericType"] = None,
                 usage_context: "ValueSpecificationContext" = None):
        super().__init__(func, generic_type, import_group, multiplicity, function_name, original_milestoned_property,
                         original_milestoned_property_parameters_values, parameters_values, property_name,
                         qualified_property_name, resolved_multiplicity_parameters, resolved_type_parameters,
                         usage_context)


class StoreValueSpecificationContext(ValueSpecificationContext):

    def __init__(self, offset: int,
                 store: "Store"):
        super().__init__(offset)
        self.store = store
