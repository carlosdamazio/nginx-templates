def permission(func):
    def wrapper(*args, **kwargs):
        try:
            func()
        except PermissionError as e:
            raise PermissionError("You're trying to modify files or \
                                  directories which you're not the owner.")
    return wrapper
