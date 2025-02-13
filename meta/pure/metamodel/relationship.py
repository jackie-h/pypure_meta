from meta import Package
from meta.pure.metamodel import PropertyOwner, ReferenceUsage, Stereotype, TaggedValue
from meta.pure.metamodel.function.property import Property, QualifiedProperty
from meta.pure.metamodel.type import Type, ClassProjection, GenericType


class Generalization:

    def __init__(self, general: "GenericType",
                 specific: "Type"):
        self.specific = specific
        self.general = general


class Association(PropertyOwner):

    def __init__(self, name: str = None,
                 original_milestoned_properties: list["Property"] = None,
                 package: "Package" = None,
                 properties: list["Property"] = None,
                 qualified_properties: list["QualifiedProperty"] = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, package, reference_usages, stereotypes, tagged_values)
        self.properties = [] if properties is None else properties
        self.original_milestoned_properties = [] if original_milestoned_properties is None else original_milestoned_properties
        self.qualified_properties = [] if qualified_properties is None else qualified_properties


class AssociationProjection(Association):

    def __init__(self, projections: list["ClassProjection"],
                 projected_association: "Association",
                 name: str = None,
                 original_milestoned_properties: list["Property"] = None,
                 package: "Package" = None,
                 properties: list["Property"] = None,
                 qualified_properties: list["QualifiedProperty"] = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, original_milestoned_properties, package, properties, qualified_properties,
                         reference_usages, stereotypes, tagged_values)
        self.projections = projections
        self.projected_association = projected_association
