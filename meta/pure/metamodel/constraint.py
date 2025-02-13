from enum import auto, Enum

from meta.pure.metamodel import ModelElement, Stereotype, TaggedValue, Any
from meta.pure.metamodel.function import FunctionDefinition
from meta.pure.metamodel.type import Class


class EnforcementLevel(Enum):
    Error = auto()
    Warn = auto()


class Constraint(ModelElement):

    def __init__(self, function_definition: "FunctionDefinition",
                 enforcement_level: str = None,
                 external_id: str = None,
                 message_function: "FunctionDefinition" = None,
                 name: str = None,
                 owner: str = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, stereotypes, tagged_values)
        self.function_definition = function_definition
        self.owner = owner
        self.external_id = external_id
        self.enforcement_level = enforcement_level
        self.message_function = message_function


class ValidatedInstance:

    def __init__(self, instance: "Any",
                 results: list["ValidationResult"] = None):
        self.instance = instance
        self.results = [] if results is None else results


class ValidationResult:

    def __init__(self, constraint: "Constraint",
                 enforcement_level: "EnforcementLevel",
                 ins: "ValidatedInstance",
                 success: bool,
                 message: str = None):
        self.success = success
        self.constraint = constraint
        self.enforcement_level = enforcement_level
        self.ins = ins
        self.message = message


class ConstraintContextInformation:

    def __init__(self, class_: "Class",
                 constraint: "Constraint",
                 enforcement_level: "EnforcementLevel",
                 message: str = None,
                 message_function: "FunctionDefinition" = None):
        self.class_ = class_
        self.constraint = constraint
        self.enforcement_level = enforcement_level
        self.message = message
        self.message_function = message_function
