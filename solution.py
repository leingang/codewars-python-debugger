#!/usr/bin/env python

import functools
import types

class Debugger(object):
    attribute_accesses = []
    method_calls = []
    
    
class Meta(type):
    
    def _getattribute_notify(obj,name):
        """Notify while getting `obj.name`."""
        # `object` here refers to the object *class*, not the instance `obj`!
        # Calling the parent class's method avoids an infinite recursion
        value = object.__getattribute__(obj,name)
        Debugger.attribute_accesses.append({
            'action': 'get',
            'class': object.__getattribute__(obj,'__class__'),
            'attribute': name,
            'value': value
        })
        return value

    def _setattr_notify(obj,name,value):
        """Notify while setting `obj.name` to `value`."""
        Debugger.attribute_accesses.append({
            'action': 'set',
            'class': object.__getattribute__(obj,'__class__'),
            'attribute': name,
            'value': value
        })
        return object.__setattr__(obj,name,value)

    def method_notify(f):
        """Notify while calling *f*."""
        @functools.wraps(f)
        def newf(*args,**kwargs):
            Debugger.method_calls.append({
                'class': (f.__self__.__class__ if type(f) is types.MethodType else f.__class__),
                'method': f.__name__,
                'args': args,
                'kwargs': kwargs
            })
            return f(*args,**kwargs)
        return newf    
 
    def __new__(cls, name, bases, attr):
        # Override generic methods to their notified versions
        for name, f in attr.items():
            if  (type(f) is types.FunctionType or type(f) is types.MethodType)\
                    and name != '__getattribute__'\
                    and name != '__setattr__':
                attr[name] = cls.method_notify(f)
        attr['__getattribute__'] = cls._getattribute_notify
        attr['__setattr__'] = cls._setattr_notify
        return super(Meta, cls).__new__(cls, name, bases, attr)
