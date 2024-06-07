from functools import wraps
from typing import Callable

from res.info_text import PERMISSION_ERROR_TEXT
from viewModel import vm
from config import bot


def isAuth(func: Callable) -> Callable:
    @wraps(func)
    def _wrapper(*args, **kwargs) -> Callable | PermissionError:
        if hasattr(vm, 'auth') and hasattr(vm.auth, 'authDataChecker') and vm.auth.authDataChecker.isAuth:
            return func(*args, **kwargs, error=None)

        func(*args, **kwargs, error=PermissionError(PERMISSION_ERROR_TEXT))

    return _wrapper
