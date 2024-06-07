from functools import wraps
from typing import Callable
from viewModel import vm
from config import bot


def isAuth(func: Callable) -> Callable:
    @wraps(func)
    def _wrapper(*args, **kwargs) -> Callable | None:
        if hasattr(vm, 'auth') and vm.auth.authDataChecker.isAuth:
            return func(*args, **kwargs)

    return _wrapper
