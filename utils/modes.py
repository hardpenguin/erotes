import sys

def select_mode(arg_list): # which routine should be ran?
    
    if len(arg_list.args) < 2:
        arg_list.display_help()
        sys.exit(0)

    mode = arg_list.choose_first_argument()

    if mode in [
                    arg_list.supported_args[0]["short"],
                    arg_list.supported_args[0]["long"]
                ]:
        return("start")

    elif mode in [
                    arg_list.supported_args[1]["short"], 
                    arg_list.supported_args[1]["long"]
                ]:
        return("run")

    elif mode in [
                    arg_list.supported_args[2]["short"],
                    arg_list.supported_args[2]["long"]
                ]:
        return("export")

    else:
        return("help")