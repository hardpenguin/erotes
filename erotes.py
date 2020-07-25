import os
import sys

import start
import run
import export
from utils import config, arguments, options, modes

erotes_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
current_dir = os.getcwd()

config_file_path = "%s/config.json" % erotes_dir
config = config.Config(config_file_path)

arguments = arguments.Arguments(sys.argv)

for option in options.Options:
    arguments.add_argument(
                            option[0],
                            option[1],
                            option[2]
                            )

mode = modes.select_mode(arguments)

if (mode == "start"):
    start.start_project(config, current_dir)

elif (mode == "run"):
    run.run_workplace(current_dir)

elif (mode == "export"):
    export.export_project(config, current_dir)

else:
    arguments.display_help()