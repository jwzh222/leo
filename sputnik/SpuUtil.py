#-*- coding: utf-8 -*-
import os
from functools import wraps
from inspect import getcallargs


def type_check(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg, value in getcallargs(func, *args, **kwargs).items():
            if arg in func.__annotations__:
                arg_type = func.__annotations__[arg]
                assert isinstance(value, arg_type)

        ret_val = func(*args, **kwargs)

        if 'return' in func.__annotations__:
            assert isinstance(ret_val, func.__annotations__['return']) 

        return ret_val
    return wrapper


@type_check
def get_suffix_by_filename(filename: str) -> str:
    if filename.endswith(('.jpg', '.jpeg', '.png', '.pjpeg', '.amr')):
        _, suffix = os.path.splitext(filename)
        suffix = '.jpg' if suffix == '.jpeg' else suffix
        return suffix 
    return ''
