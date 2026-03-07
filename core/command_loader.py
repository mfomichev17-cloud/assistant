import os
import importlib

def load_commands():

    commands = {}

    commands_folder = "commands"

    for file in os.listdir(commands_folder):

        if file.endswith(".py") and file != "__init__.py":

            module_name = file[:-3]

            module = importlib.import_module(f"commands.{module_name}")

            if hasattr(module, "COMMANDS"):

                commands.update(module.COMMANDS)

    return commands