from zope.interface import implements
from Products.validation.interfaces.IValidator import IValidator
import re

phone_pattern = re.compile('\(\d\d\d\) \d\d\d-\d\d\d\d')


class FormattedUSPhoneValidator:
    implements(IValidator)

    def __init__(self, name):
        self.name = name
        return None

    def __call__(self, value, *args, **kwargs):
        if not phone_pattern.match(value):
            return """Not in form: (999) 555-1212"""
        return 1


class USAddressValidator:
    implements(IValidator)

    def __init__(self, name):
        self.name = name
        return None

    def __call__(self, value, *args, **kwargs):
        if not ("\n" in value or "\r" in value):
            return """Not a valid US addresss."""
        return 1


class LinesAllFloatValidator:
    implements(IValidator)

    def __init__(self, name):
        self.name = name
        return None

    def __call__(self, value, *args, **kwargs):
        for i in value:
            try:
                float(i)
            except:
                return """Not a valid floating-point number: %s""" % i
        return 1


class LinesAllIntValidator:
    implements(IValidator)

    def __init__(self, name):
        self.name = name
        return None

    def __call__(self, value, *args, **kwargs):
        for i in value:
            try:
                int(i)
            except:
                return """Not a valid integer: %s""" % i
        return 1


class SimpleDataGridValidator:
    """Ensure a data grid field has the correct number of columns, if a value
    is set as a field property.
    """
    implements(IValidator)

    def __init__(self, name):
        self.name = name
        return None

    def __call__(self, value, *args, **kwargs):
        field = kwargs['field']
        cols = field.columns
        if cols:
            for v in value:
                if len(v.split(field.delimiter)) != cols:
                    return "Each row must have exactly %d fields" % cols
        return 1


__all__ = ('FormattedUSPhoneValidator', 'USAddressValidator',
           'LinesAllFloatValidator', 'LinesAllIntValidator',
           'SimpleDataGridValidator')
