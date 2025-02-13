from meta.pure.metamodel import PropertyOwner, PackageableElement, Referenceable
from meta.pure.metamodel.constraint import Constraint
from meta.pure.metamodel.extension import ElementWithConstraints, AnnotatedElement
from meta.pure.metamodel.function import FunctionDefinition, Function
from meta.pure.metamodel.function.property import Property, QualifiedProperty
from meta.pure.metamodel.multiplicity import Multiplicity
from meta.pure.metamodel.relationship import Generalization
from meta.pure.metamodel.treepath import RootRouteNode
from meta.pure.metamodel.type.generics import TypeParameter, GenericType
from meta.pure.metamodel.valuespecification import InstanceValue, VariableExpression
from meta.pure.test import Testable, Test


class Type:

    def __init__(self, generalizations: list["Generalization"] = None,
                 name: str = None,
                 specializations: list["Generalization"] = None):
        self.name = name
        self.generalizations = [] if generalizations is None else generalizations
        self.specializations = [] if specializations is None else specializations


class Class(Type, PropertyOwner, ElementWithConstraints, PackageableElement, Testable):

    def __init__(self, constraints: list["Constraint"] = None,
                 generalizations: list["Generalization"] = None,
                 multiplicity_parameters: list["InstanceValue"] = None,
                 name: str = None,
                 original_milestoned_properties: list["Property"] = None,
                 package: "Package" = None,
                 properties: list["Property"] = None,
                 properties_from_associations: list["Property"] = None,
                 qualified_properties: list["QualifiedProperty"] = None,
                 qualified_properties_from_associations: list["QualifiedProperty"] = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 specializations: list["Generalization"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None,
                 tests: list["Test"] = None,
                 type_parameters: list["TypeParameter"] = None,
                 type_variables: list["VariableExpression"] = None):
        Type.__init__(self, generalizations, name, specializations)
        PropertyOwner.__init__(self, name, package, reference_usages, stereotypes, tagged_values)
        ElementWithConstraints.__init__(self, constraints)
        PackageableElement.__init__(self, name, package, reference_usages, stereotypes, tagged_values)
        Testable.__init__(self, tests)
        self.properties = [] if properties is None else properties
        self.original_milestoned_properties = [] if original_milestoned_properties is None else original_milestoned_properties
        self.properties_from_associations = [] if properties_from_associations is None else properties_from_associations
        self.qualified_properties = [] if qualified_properties is None else qualified_properties
        self.qualified_properties_from_associations = [] if qualified_properties_from_associations is None else qualified_properties_from_associations
        self.type_parameters = [] if type_parameters is None else type_parameters
        self.type_variables = [] if type_variables is None else type_variables
        self.multiplicity_parameters = [] if multiplicity_parameters is None else multiplicity_parameters


class Any:

    def __init__(self, classifier_generic_type: "GenericType" = None,
                 element_override: "ElementOverride" = None):
        self.classifier_generic_type = classifier_generic_type
        self.element_override = element_override


class Nil:

    def __init__(self):
        pass


class DataType(Type):

    def __init__(self, generalizations: list["Generalization"] = None,
                 name: str = None,
                 specializations: list["Generalization"] = None):
        super().__init__(generalizations, name, specializations)


class Measure(DataType, PackageableElement):

    def __init__(self, canonical_unit: "Unit" = None,
                 generalizations: list["Generalization"] = None,
                 name: str = None,
                 non_canonical_units: list["Unit"] = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 specializations: list["Generalization"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        DataType.__init__(self, generalizations, name, specializations)
        PackageableElement.__init__(self, name, package, reference_usages, stereotypes, tagged_values)
        self.canonical_unit = canonical_unit
        self.non_canonical_units = [] if non_canonical_units is None else non_canonical_units


class Unit(DataType, Referenceable):

    def __init__(self, measure: "Measure",
                 conversion_function: "FunctionDefinition" = None,
                 generalizations: list["Generalization"] = None,
                 name: str = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 specializations: list["Generalization"] = None):
        DataType.__init__(self, generalizations, name, specializations)
        Referenceable.__init__(self, reference_usages)
        self.measure = measure
        self.conversion_function = conversion_function


class PrimitiveType(DataType, PackageableElement, ElementWithConstraints):

    def __init__(self, constraints: list["Constraint"] = None,
                 extended: bool = None,
                 generalizations: list["Generalization"] = None,
                 name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 specializations: list["Generalization"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None,
                 type_variables: list["VariableExpression"] = None):
        DataType.__init__(self, generalizations, name, specializations)
        PackageableElement.__init__(self, name, package, reference_usages, stereotypes, tagged_values)
        ElementWithConstraints.__init__(self, constraints)
        self.extended = extended
        self.type_variables = [] if type_variables is None else type_variables


class Enumeration(DataType, PackageableElement):

    def __init__(self, values,
                 generalizations: list["Generalization"] = None,
                 name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 specializations: list["Generalization"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        DataType.__init__(self, generalizations, name, specializations)
        PackageableElement.__init__(self, name, package, reference_usages, stereotypes, tagged_values)
        self.values = values


class Enum(AnnotatedElement):

    def __init__(self, name: str,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(stereotypes, tagged_values)
        self.name = name


class ElementOverride:

    def __init__(self):
        pass


class GetterOverride(ElementOverride):

    def __init__(self, getter_override_to_many: "Function" = None,
                 getter_override_to_one: "Function" = None,
                 hidden_payload: "Any" = None):
        super().__init__()
        self.getter_override_to_one = getter_override_to_one
        self.getter_override_to_many = getter_override_to_many
        self.hidden_payload = hidden_payload


class FunctionType(Type, Referenceable):

    def __init__(self, return_multiplicity: "Multiplicity",
                 return_type: "GenericType",
                 function: list["Function"] = None,
                 generalizations: list["Generalization"] = None,
                 multiplicity_parameters: list["InstanceValue"] = None,
                 name: str = None,
                 parameters: list["VariableExpression"] = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 specializations: list["Generalization"] = None,
                 type_parameters: list["TypeParameter"] = None):
        Type.__init__(self, generalizations, name, specializations)
        Referenceable.__init__(self, reference_usages)
        self.return_type = return_type
        self.return_multiplicity = return_multiplicity
        self.function = [] if function is None else function
        self.parameters = [] if parameters is None else parameters
        self.type_parameters = [] if type_parameters is None else type_parameters
        self.multiplicity_parameters = [] if multiplicity_parameters is None else multiplicity_parameters


class ConstraintsOverride(ElementOverride):

    def __init__(self, constraints_manager: "Function" = None):
        super().__init__()
        self.constraints_manager = constraints_manager


class ConstraintsGetterOverride(GetterOverride, ConstraintsOverride):

    def __init__(self, constraints_manager: "Function" = None,
                 getter_override_to_many: "Function" = None,
                 getter_override_to_one: "Function" = None,
                 hidden_payload: "Any" = None):
        GetterOverride.__init__(self, getter_override_to_many, getter_override_to_one, hidden_payload)
        ConstraintsOverride.__init__(self, constraints_manager)


class ClassProjection(Class, PackageableElement):

    def __init__(self, projection_specification: "RootRouteNode",
                 constraints: list["Constraint"] = None,
                 generalizations: list["Generalization"] = None,
                 multiplicity_parameters: list["InstanceValue"] = None,
                 name: str = None,
                 original_milestoned_properties: list["Property"] = None,
                 package: "Package" = None,
                 properties: list["Property"] = None,
                 properties_from_associations: list["Property"] = None,
                 qualified_properties: list["QualifiedProperty"] = None,
                 qualified_properties_from_associations: list["QualifiedProperty"] = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 specializations: list["Generalization"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None,
                 tests: list["Test"] = None,
                 type_parameters: list["TypeParameter"] = None,
                 type_variables: list["VariableExpression"] = None):
        Class.__init__(self, constraints, generalizations, multiplicity_parameters, name,
                       original_milestoned_properties, package, properties, properties_from_associations,
                       qualified_properties, qualified_properties_from_associations, reference_usages, specializations,
                       stereotypes, tagged_values, tests, type_parameters, type_variables)
        PackageableElement.__init__(self, name, package, reference_usages, stereotypes, tagged_values)
        self.projection_specification = projection_specification
