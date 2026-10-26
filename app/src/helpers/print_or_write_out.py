import sys

from .write_out import WriteOut
from .pathname import get_pathname_direction

def create_write_out(s: str) -> WriteOut:
    pathname = get_pathname_direction(s)
    return WriteOut(pathname)

class PrintOrWriteOut:

    def __init__(self):
        self.write_out = False 
        self.out_file = None
        self.err_file = None

    def process_args(self, args: list[str]):
        index_out = -1
        index_err = -1

        if '1>' in args:
            index_out = args.index('1>')
            self.write_out = True
            
            self.out_file = create_write_out(args[index_out + 1])
        elif '1>>' in args:
            self.write_out = True
            index_out = args.index('1>>')
            self.out_file = create_write_out(args[index_out + 1])
            self.out_file.only_append()

        if '2>' in args:
            self.write_out = True
            index_err = args.index('2>')
            self.err_file = create_write_out(args[index_err + 1])
        elif '2>>' in args:
            self.write_out = True
            index_err = args.index('2>>')
            self.err_file = create_write_out(args[index_err + 1])
            self.err_file.only_append()

        if self.write_out:
            return

        if '>' in args:
            index_out = args.index('>')
            if len(args) <= index_out + 1:
                return
            self.out_file = create_write_out(args[index_out + 1])

        if '>>' in args:
            index_out = args.index('>>')
            if len(args) <= index_out + 1:
                return
            self.out_file = create_write_out(args[index_out + 1])
            self.out_file.only_append()

    def out(self, message):
        if not self.out_file:
            sys.stdout.write(message)
            return

        file_manager = self.out_file
        file_manager.write(message)

    def err(self, message):
        if not self.err_file:
            sys.stderr.write(message)
            return

        file_manager = self.err_file
        file_manager.write(message)

