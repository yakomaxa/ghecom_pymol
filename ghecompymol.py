import subprocess
import tempfile
import os

# download ghecom here
# https://pdbj.org/ghecom/

def ghecom(target, option=""):

#make temporary dir and do everything there
    with tempfile.TemporaryDirectory() as dname:
        #turn off zooming when loading: set auto_zoom, off    
        old_auto_zoom=cmd.get("auto_zoom")
        cmd.set("auto_zoom","off")
        # print tmp dir name
        print("Temporary directory =" + dname)
        # make sure you have mican in PATH
        # directly giving 'execute' full path below is good alternative
        # For example : execute = "/usr/bin/mican"
        execute = "/Users/sakuma/mybin/ghecom"
        tmptarget = dname + "/target.pdb"
        tmpoutput = dname + "/output.pdb"
        pymol.cmd.save(tmptarget, target)

        mican = [execute, "-ipdb",tmptarget,"-opocpdb",tmpoutput]
        
        for op in option.split():
            if(op == "-O"):
                print("option -ipdb is reserved")
                raise CmdException
            if(op == "-opocpdb"):
                print("option -opocpdb is reserved")
                raise CmdException
            mican.append(op)
                
        proc=subprocess.run(mican,stdout = subprocess.PIPE)
        print(proc.stdout.decode("utf8")) # print result to pymol console
        
        pymol.cmd.load(tmpoutput,"pocket")
        pymol.cmd.hide("everything","pocket")
        pymol.cmd.show("sphere","pocket")
        # reset auto_zoom as you had set
        cmd.set("auto_zoom",old_auto_zoom)

pymol.cmd.extend("ghecom",ghecom)
cmd.auto_arg[0]['ghecom'] = cmd.auto_arg[0]['delete']
