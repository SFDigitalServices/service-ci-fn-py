""" functions related to step implementation """
import importlib

# pylint: disable=too-few-public-methods
class Step():
    """ Step Class """

    @staticmethod
    def run(data: dict, content: dict):
        """ run step """
        uses_token = data['uses'].split('/')
        mod_name = uses_token[0]
        method_token = uses_token[1].split('@v')
        method = method_token[0]
        version = int(method_token[1])
        print(f"Step.run {mod_name}")
        mod = importlib.import_module(f".{mod_name}", "mods")
        print("--- step:data ---")
        print(data)
        print("--- step:content ---")
        print(content)
        out = mod.process(data, content, method, version)
        print ("--- step:out ---")
        print (out)
        return out
