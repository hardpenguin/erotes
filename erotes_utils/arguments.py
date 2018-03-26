import os

class Arguments(object): # command line arguments given
    
    def __init__(self,Args):
        self.Args=Args
        self.SupportedArgs=[]

    def AddArgument(self,Short,Long,Description):
        NewArg={ \
                "short":Short, \
                "long":Long, \
                "description":Description \
               }
        self.SupportedArgs.append(NewArg)

    def ChooseFirstArgument(self):
        return(self.Args[1])

    def DisplayHelp(self):
        ScriptName=os.path.basename(self.Args[0])
        print "Syntax:"
        print " "+ScriptName+" [options]"
        print ""
        print "Available options:"
        for Arg in self.SupportedArgs:
            print("  {:5}  {:20}  {:40}".format(Arg["short"]+",",Arg["long"],Arg["description"]))