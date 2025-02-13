from meta.pure.metamodel import PackageableElement, ReferenceUsage


class ElementWithConstraints():

    def __init__(self, constraints: list["Constraint"] = None):
        self.constraints = [] if constraints is None else constraints


class ElementWithStereotypes():

    def __init__(self, stereotypes: list["Stereotype"] = None):
        self.stereotypes = [] if stereotypes is None else stereotypes


class ElementWithTaggedValues():

    def __init__(self, tagged_values: list["TaggedValue"] = None):
        self.tagged_values = [] if tagged_values is None else tagged_values


class TaggedValue():

    def __init__(self, tag: "Tag",
                 value: str):
        self.tag = tag
        self.value = value


class AnnotatedElement(ElementWithStereotypes, ElementWithTaggedValues):

    def __init__(self, stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        ElementWithStereotypes.__init__(self, stereotypes)
        ElementWithTaggedValues.__init__(self, tagged_values)


class Profile(PackageableElement):

    def __init__(self, name: str = None,
                 p___stereotypes: list["Stereotype"] = None,
                 p___tags: list["Tag"] = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, package, reference_usages, stereotypes, tagged_values)
        self.p___stereotypes = [] if p___stereotypes is None else p___stereotypes
        self.p___tags = [] if p___tags is None else p___tags


class Annotation():

    def __init__(self, profile: "Profile",
                 value: str,
                 model_elements: list["AnnotatedElement"] = None):
        self.profile = profile
        self.value = value
        self.model_elements = [] if model_elements is None else model_elements


class Tag(Annotation):

    def __init__(self, profile: "Profile",
                 value: str,
                 model_elements: list["AnnotatedElement"] = None):
        super().__init__(profile, value, model_elements)


class Stereotype(Annotation):

    def __init__(self, profile: "Profile",
                 value: str,
                 model_elements: list["AnnotatedElement"] = None):
        super().__init__(profile, value, model_elements)