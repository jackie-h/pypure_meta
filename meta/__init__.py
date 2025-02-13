import meta.pure.metamodel as m





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