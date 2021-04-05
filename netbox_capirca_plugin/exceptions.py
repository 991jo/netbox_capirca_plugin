class UnsupportedTarget(Exception):
    """The target is not supported."""
    pass


class BasePathEscapeError(Exception):
    """The path is not a subpath of the base path."""
    pass
