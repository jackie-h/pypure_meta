from meta.pure.metamodel import PackageableElement, Stereotype, TaggedValue, ReferenceUsage


class Package(PackageableElement):

    def __init__(self, children: list["PackageableElement"] = None,
                 name: str = None,
                 package: "Package" = None,
                 reference_usages: list["ReferenceUsage"] = None,
                 stereotypes: list["Stereotype"] = None,
                 tagged_values: list["TaggedValue"] = None):
        super().__init__(name, package, reference_usages, stereotypes, tagged_values)
        self.children = [] if children is None else children


class SourceInformation():

    def __init__(self, column: int,
                 end_column: int,
                 end_line: int,
                 line: int,
                 source: str,
                 start_column: int,
                 start_line: int):
        self.source = source
        self.start_line = start_line
        self.start_column = start_column
        self.line = line
        self.column = column
        self.end_line = end_line
        self.end_column = end_column