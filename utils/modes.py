import sys

def SelectMode(ArgumentsList): # which routine should be ran?
    
    if len(ArgumentsList.Args)<2:
        ArgumentsList.DisplayHelp()
        sys.exit()

    Mode=ArgumentsList.ChooseFirstArgument()

    if (Mode==ArgumentsList.SupportedArgs[0]["short"]) or \
       (Mode==ArgumentsList.SupportedArgs[0]["long"]):
        return("start")

    elif (Mode==ArgumentsList.SupportedArgs[1]["short"]) or \
         (Mode==ArgumentsList.SupportedArgs[1]["long"]):
        return("run")

    elif (Mode==ArgumentsList.SupportedArgs[2]["short"]) or \
         (Mode==ArgumentsList.SupportedArgs[2]["long"]):
        return("export")

    else:
        return("help")