import os

def run_workplace(work_dir):
    runtime_subpath = "/love/linux64/"
    runtime_binary = "love"
    runtime_path= "%s%s" % (work_dir, runtime_subpath)
    ld_library_path = "LD_LIBRARY_PATH=\"${LD_LIBRARY_PATH}:%s\"" % runtime_path
    executable = "\"%s%s\"" % (runtime_path, runtime_binary)
    argument = "\"%s/workplace\"" % work_dir
    run_command = "%s %s %s" % (ld_library_path, executable, argument)

    print("Running project...")
    os.system(run_command)
    
    print("Done.")