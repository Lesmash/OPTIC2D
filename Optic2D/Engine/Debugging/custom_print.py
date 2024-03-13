class CPrint:
    def __init__(self, msg: str, code: int, show_error: bool):
        self.msg = msg
        self.code = code
        self.show_error = show_error

    def cprint(self):
        if self.code == 0:
            print(f'{str(self.code)}: EXIT')
        else:
            print(f'{str(self.code)}: {self.msg}')