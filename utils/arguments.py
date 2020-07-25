import os

class Arguments(object): # command line arguments given
    
    def __init__(self, args):
        self.args = args
        self.supported_args = []

    def add_argument(self, short_str, long_str, description):
        new_arg = {
                    "short": short_str,
                    "long": long_str,
                    "description": description
                   }
        self.supported_args.append(new_arg)

    def choose_first_argument(self):
        return(self.args[1])

    def display_help(self):
        script_name = os.path.basename(self.args[0])
        print("Syntax:")
        print(" %s [options]" % script_name)
        print()
        print("Available options:")
        for arg in self.supported_args:
            help_line = "  {:5},  {:20}  {:40}".format(
                                                        arg["short"],
                                                        arg["long"],
                                                        arg["description"]
                                                    )
            print(help_line)