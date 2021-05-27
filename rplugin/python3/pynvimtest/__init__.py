import pynvim
from pynvim.api.nvim import Nvim

@pynvim.plugin
class PynvimTest(object):
    def __init__(self, nvim: Nvim):
        self.nvim = nvim
    
    def vimecho(self, msg):
        self.nvim.command("echo \"" + msg + "\"")

    @pynvim.command('TestCommandWithoutArgs')
    def testcommand(self):
        self.nvim.out_write("Command Call : 'TestCommandWithoutArgs'\n")
    
    @pynvim.command('TestCommandWithArgs',nargs='*')
    def testcommand_with_args(self,*args):
        self.nvim.out_write("Command Call : 'TestCommandWithArgs' and \nargs : " + str(args) + "\n")

    @pynvim.command('TestCommandOutWrite')
    def testcommand_outwrite(self):
        self.nvim.out_write("Message as normal message\n")

    @pynvim.command('TestCommandWithRange', nargs='*' ,range="")
    def testcommand_with_range(self,*args):
        firstline = args[1][0]
        lastline = args[1][1]
        self.nvim.out_write("firstline: {0} lastline: {1}\n".format(firstline,lastline))
    
    @pynvim.command('TestCommandInput')
    def testcommand_input(self,*args):
        insert = 'i'
        normal = '<ESC>'
        ret = '<CR>'
        self.nvim.input(insert + "Written Message ..." + normal + ":echo 'Echo Message ...'" + ret)

    @pynvim.command('TestCommandCommandOutput')
    def testcommand_command_output(self):
        msg = self.nvim.command_output("echo \"Hello PyNvim\"")
        self.nvim.out_write("\"" + msg +"\" Output\n")
        

    @pynvim.command('TestListRuntimePaths')
    def testcommand_list_runtimepaths(self,*args):
        self.nvim.out_write(str(self.nvim.list_runtime_paths())+'\n')
    
    @pynvim.command('TestCommandEval')
    def testcommand_eval(self):
        variable = self.nvim.eval('g:test#test_GlobalVariable')
        self.nvim.out_write(variable + "\n")
    
    @pynvim.command('TestCommandVars')
    def testcommand_vars(self):
        # Many types of variables
        self.nvim.vars['new_global_var'] = [1, 2, 3]
        self.nvim.out_write(str(self.nvim.eval('g:new_global_var'))+'\n')
    
    @pynvim.command('DummyCommand')
    def dummy(self):
        pass


