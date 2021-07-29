import os
import sys

from nuitka import Options
from nuitka.plugins.PluginBase import NuitkaPluginBase

class NuitkaPluginWebAssemblyWorkarounds(NuitkaPluginBase):
    plugin_name = "wasm-compat"

    # def __init__(self, trace_my_plugin):
    #     # demo only: extract and display my options list
    #     # check whether some specific option is set

    #     self.check = trace_my_plugin
    #     self.info(" 'trace' is set to '%s'" % self.check)

    #     # do more init work here ...

    # @classmethod
    # def addPluginCommandLineOptions(cls, group):
    #     group.add_option(
    #         "--trace-my-plugin",
    #         action="store_true",
    #         dest="trace_my_plugin",
    #         default=False,
    #         help="This is show in help output."
    #     )

    # def onModuleSourceCode(self, module_name, source_code):
    #     # if this is the main script and tracing should be done ...
    #     if module_name == "__main__" and self.check:
    #         self.info("")
    #         self.info(" Calls to 'math' module:")
    #         for i, l in enumerate(source_code.splitlines()):
    #             if "math." in l:
    #                 self.info(" %i: %s" % (i+1, l))
    #         self.info("")
    #     return source_code


    def __init__(self):
        cc_flags = os.environ.get("CCFLAGS", "")
        cc_flags += " -I/usr/include/"
        cc_flags += " -I/usr/include/x86_64-linux-gnu/"
        # cc_flags += " --target=wasm64"
        os.environ["CCFLAGS"] = cc_flags

    @staticmethod
    def getPreprocessorSymbols():
        return {
            "__linux__": "",
            "__x86_64__": "",
            # "__LP64__": "",
            # "SIZEOF_LONG": "8",
            # "LONG_BIT": "64",
        }
        return {}
 
