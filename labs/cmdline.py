import argh

class Namespace(argh.EntryPoint):
    def add_subcommands(self, parser):
        argh.add_commands(
            parser,
            self.commands,
            namespace=self.name,
            namespace_kwargs=self.parser_kwargs
        )
