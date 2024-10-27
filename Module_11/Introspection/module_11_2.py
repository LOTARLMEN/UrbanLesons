from pprint import pprint


def introspection_info(obj):
    type_ = type(obj).__name__
    attributes = dir(obj)
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]
    module = getattr(obj, "__module__", None)
    return {
            "type": type_,
            "attributes": attributes,
            "methods": methods,
            "module": module,
            }

pprint(introspection_info(42))