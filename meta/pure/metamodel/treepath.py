from meta.pure.metamodel import AnnotatedElement, ReferenceUsage, Stereotype, TaggedValue, Any
from meta.pure.metamodel.function import FunctionDefinition
from meta.pure.metamodel.function.property import AbstractProperty
from meta.pure.metamodel.functions.collection import TreeNode
from meta.pure.metamodel.type import GenericType
from meta.pure.metamodel.valuespecification import ValueSpecification, FunctionExpression, InstanceValue


class RouteNode(AnnotatedElement):

    def __init__(self, include_all: str,
                 name: str,
                 type_: "GenericType",
                 children: list["PropertyRouteNode"] = None,
                 excluded: list["RouteNodePropertyStub"] = None,
                 included: list["RouteNodePropertyStub"] = None,
                 resolved_properties: list["AbstractProperty"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(stereotypes, tagged_values)
        self.name = name
        self.include_all = include_all
        self.type_ = type_
        self.children = [] if children is None else children
        self.resolved_properties = [] if resolved_properties is None else resolved_properties
        self.included = [] if included is None else included
        self.excluded = [] if excluded is None else excluded


class RootRouteNode(RouteNode):

    def __init__(self, include_all: str,
                 name: str,
                 type_: "GenericType",
                 children: list["PropertyRouteNode"] = None,
                 excluded: list["RouteNodePropertyStub"] = None,
                 included: list["RouteNodePropertyStub"] = None,
                 owner: "Any" = None,
                 resolved_properties: list["AbstractProperty"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(include_all, name, type_, children, excluded, included, resolved_properties, stereotypes,
                         tagged_values)
        self.owner = owner


class PropertyRouteNode(RouteNode):

    def __init__(self, include_all: str,
                 name: str,
                 property_name: str,
                 root: "RootRouteNode",
                 type_: "GenericType",
                 children: list["PropertyRouteNode"] = None,
                 excluded: list["RouteNodePropertyStub"] = None,
                 included: list["RouteNodePropertyStub"] = None,
                 resolved_properties: list["AbstractProperty"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(include_all, name, type_, children, excluded, included, resolved_properties, stereotypes,
                         tagged_values)
        self.property_name = property_name
        self.root = root


class RouteNodePropertyStub(AnnotatedElement):

    def __init__(self, owner: "RouteNode",
                 parameters: list["InstanceValue"] = None,
                 property_: list["AbstractProperty"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(stereotypes, tagged_values)
        self.owner = owner
        self.property = [] if property_ is None else property
        self.parameters = [] if parameters is None else parameters


class ExistingPropertyRouteNode(PropertyRouteNode):

    def __init__(self, include_all: str,
                 name: str,
                 property_: "RouteNodePropertyStub",
                 property_name: str,
                 root: "RootRouteNode",
                 type_: "GenericType",
                 children: list["PropertyRouteNode"] = None,
                 excluded: list["RouteNodePropertyStub"] = None,
                 included: list["RouteNodePropertyStub"] = None,
                 resolved_properties: list["AbstractProperty"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(include_all, name, property_name, root, type_, children, excluded, included,
                         resolved_properties, stereotypes, tagged_values)
        self.property_ = property_


class NewPropertyRouteNode(PropertyRouteNode):

    def __init__(self, function_definition: "NewPropertyRouteNodeFunctionDefinition",
                 include_all: str,
                 name: str,
                 property_name: str,
                 root: "RootRouteNode",
                 specifications: list["ValueSpecification"],
                 type_: "GenericType",
                 children: list["PropertyRouteNode"] = None,
                 excluded: list["RouteNodePropertyStub"] = None,
                 included: list["RouteNodePropertyStub"] = None,
                 resolved_properties: list["AbstractProperty"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(include_all, name, property_name, root, type_, children, excluded, included,
                         resolved_properties, stereotypes, tagged_values)
        self.specifications = specifications
        self.function_definition = function_definition


class NewPropertyRouteNodeFunctionDefinition(FunctionDefinition):

    def __init__(self, expression_sequence: list["ValueSpecification"],
                 owner: "NewPropertyRouteNode",
                 applications: list["FunctionExpression"] = None,
                 function_name: str = None,
                 name: str = None,
                 reference_usages: list["ReferenceUsage"] = None):
        super().__init__(expression_sequence, applications, function_name, name, reference_usages)
        self.owner = owner


class PropertyPathTreeNode(TreeNode):

    def __init__(self, children_data: list["TreeNode"] = None,
                 property_: "AbstractProperty" = None):
        super().__init__(children_data)
        self.property_ = property_
