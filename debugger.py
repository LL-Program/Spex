from colorama import Fore, Back, Style
from sys import exit

class SpexDebugger:
    def __init__(self,Interpreter):
        self.status = ""
        self.interpreter = Interpreter
        self.mainfile = None
    def ThrowError(self, FormatText,Line,Type):
        print(f"""ErrorCall (SpexDebugger):
    {self.mainfile}, {Fore.GREEN}line::{Line}{Fore.WHITE}, in {Fore.CYAN}__MAIN__{Fore.RESET}
        "{FormatText}" - this means you are fucked
{Fore.LIGHTRED_EX}{Back.WHITE}Spe*{Back.RESET}{Fore.RESET} |{Fore.RED}{Type}Error{Fore.RESET}""")
        exit(1)
    def ThrowNote(self, NoteText, FormatValue = "INFO"):
        print(f"""{FormatValue} | (SpexDebugger):
    {self.mainfile}, {Fore.GREEN}line:: -Unknown- {Fore.WHITE}, in {Fore.CYAN}__MAIN__{Fore.RESET}
        "{NoteText}"
{Fore.LIGHTRED_EX}{Back.WHITE}Spe*{Back.RESET}{Fore.RESET}""")
