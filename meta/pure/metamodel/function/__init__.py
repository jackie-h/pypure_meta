from meta import Package
from meta.pure.metamodel import Referenceable, PackageableElement, Stereotype, TaggedValue, ReferenceUsage
from meta.pure.metamodel.constraint import Constraint
from meta.pure.metamodel.valuespecification import FunctionExpression, ValueSpecification
from meta.pure.test import Testable, Test


class Function(Referenceable):

    def __init__(self, applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 reference_usages: list["ReferenceUsage"] = None):
        super().__init__(reference_usages)
        self.name = name
        self.function_name = function_name
        self.applications = [] if applications is None else applications


class FunctionDefinition(Function):

    def __init__(self, expression_sequence: list["ValueSpecification"],
                 applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 reference_usages: list["ReferenceUsage"] = None):
        super().__init__(applications, function_name, name, reference_usages)
        self.expression_sequence = expression_sequence


class PackageableFunction(PackageableElement, Function):

    def __init__(self, applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 package: "Package" = None,
                 post_constraints: list["Constraint"] = None,
                 pre_constraints: list["Constraint"] = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        PackageableElement.__init__(self, name, package, reference_usages, stereotypes, tagged_values)
        Function.__init__(self, applications, function_name, name, reference_usages)
        self.pre_constraints = [] if pre_constraints is None else pre_constraints
        self.post_constraints = [] if post_constraints is None else post_constraints


class NativeFunction(PackageableFunction):

    def __init__(self, applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 package: "Package" = None,
                 post_constraints: list["Constraint"] = None,
                 pre_constraints: list["Constraint"] = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(applications, function_name, name, package, post_constraints, pre_constraints,
                         reference_usages, stereotypes, tagged_values)


class ConcreteFunctionDefinition(FunctionDefinition, PackageableFunction, Testable):

    def __init__(self, expression_sequence: list["ValueSpecification"],
                 applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 package: "Package" = None,
                 post_constraints: list["Constraint"] = None,
                 pre_constraints: list["Constraint"] = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None,
                 tests: list["Test"] = None):
        FunctionDefinition.__init__(self, expression_sequence, applications, function_name, name, reference_usages)
        PackageableFunction.__init__(self, applications, function_name, name, package, post_constraints,
                                     pre_constraints, reference_usages, stereotypes, tagged_values)
        Testable.__init__(self, tests)


class LambdaFunction(FunctionDefinition):

    def __init__(self, expression_sequence: list["ValueSpecification"],
                 applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 open_variables: list[str] = None,
                 reference_usages: list["ReferenceUsage"] = None):
        super().__init__(expression_sequence, applications, function_name, name, reference_usages)
        self.open_variables = [] if open_variables is None else open_variables
