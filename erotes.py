import os
import sys

import start
import run
import export
import utils

erotes_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
current_dir = os.getcwd()

config_file_path = "%s/config.json" % erotes_dir
config = utils.config.Config(config_file_path)

arguments = utils.arguments.Arguments(sys.argv)

for option in utils.options.Options:
    arguments.add_argument(
                            option[0],
                            option[1],
                            option[2]
                            )

mode = utils.modes.select_mode(arguments)

if (mode == "start"):
    start.start_project(config, current_dir)

elif (mode == "run"):
    run.run_workplace(current_dir)

elif (mode == "export"):
    export.export_project(config, current_dir)

else:
    arguments.display_help()