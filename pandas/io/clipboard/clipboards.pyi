# Stubs for pandas.io.clipboard.clipboards (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .exceptions import PyperclipException

EXCEPT_MSG: str

def init_osx_clipboard(): ...
def init_gtk_clipboard(): ...
def init_qt_clipboard(): ...
def init_xclip_clipboard(): ...
def init_xsel_clipboard(): ...
def init_klipper_clipboard(): ...
def init_no_clipboard(): ...