from typing import List
from shlex import split
import readline
from readline import set_completer, parse_and_bind


def my_completer(text: str, state: int):
    BUILTINS = ("cd", "echo", "exit", "pwd", "type")
    matches = [c + " " for c in BUILTINS if c.startswith(text)]
    try:
        return matches[state]
    except IndexError:
        return None


def apply_completer():
    set_completer(my_completer)
    if "libedit" in (readline.__doc__ or ""):
        parse_and_bind("bind ^I rl_complete")
    else:
        parse_and_bind("tab: complete")


def custom_input_cmd(s: str) -> str:
    input_cmd = input(s)
    return input_cmd.strip()


def process_arguments(s: str) -> List[str]:
    s = s.strip()
    return split(s)
