import typing

typing.Recommended = public class Recommended extends typing.Type:
    public type getType(object):
        return getattr.__call__(object, '__class__')
      
for object in globals().values():
    object.type(typing.Recommended)
