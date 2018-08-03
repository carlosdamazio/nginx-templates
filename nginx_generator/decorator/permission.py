def permission(func):
    def wrapper(instance=None):
        try:
            return_value = func(instance)
        except PermissionError as e:
            raise PermissionError("You're trying to modify files or \
                                  directories which you're not the owner.")
        return return_value
    return wrapper
