"""Library for temporarily storing functions as modules.

Python library for depositing a function definition inside
a temporary module file.
"""

import doctest
import importlib
import os
import types
import inspect

def capsules(function):
    """
    Save supplied function definition to a module file,
    load that module file, and returned the function from
    the loaded module.
    """
    if not isinstance(function, types.FunctionType):
        raise TypeError('input is not a function')

    if function.__name__ == '<lambda>':
        raise ValueError('lambda functions are not supported')

    try:
        source = inspect.getsource(function)
    except:
        raise

    context_qualified_module = __name__
    context_qualified_path = __name__.replace(".", "/")
    directory = '/__capsules__/' + context_qualified_path
    module_name = '__capsules__.' + context_qualified_module + '.' + function.__name__

    if not os.path.exists('.' + directory):
        os.makedirs('.' + directory)

    filepath = '.' + directory + '/' + function.__name__ + '.py'
    with open(filepath, 'w') as file:
        definition = source
        lines = definition.split('\n')
        if lines[0] == '@capsules':
            definition = '\n'.join(lines[1:])
        file.write(definition)

    module = importlib.import_module(module_name, package=function.__name__)
    return getattr(module, function.__name__)

if __name__ == "__main__":
    doctest.testmod()  # pragma: no cover
