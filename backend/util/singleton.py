import threading
from typing import Type, Any


def singleton(cls: Type[Any]) -> Type[Any]:
    """Decorator that enforces the singleton pattern.
    
    Classes decorated with @singleton must be initialized via get_instance().
    Direct instantiation via __init__ is blocked.
    """
    instances = {}
    lock = threading.Lock()
    original_init = cls.__init__

    def get_instance(*args, **kwargs):
        with lock:
            if cls not in instances:
                instance = object.__new__(cls)
                original_init(instance, *args, **kwargs)
                instances[cls] = instance
            return instances[cls]

    def reset_instance():
        with lock:
            instances.pop(cls, None)

    def guarded_init(self, *args, **kwargs):
        if cls in instances and instances[cls] is self:
            return
        raise RuntimeError(
            f"{cls.__name__} is a singleton. Use {cls.__name__}.get_instance() instead."
        )

    cls.__init__ = guarded_init
    cls.get_instance = staticmethod(get_instance)
    cls.reset_instance = staticmethod(reset_instance)

    return cls
