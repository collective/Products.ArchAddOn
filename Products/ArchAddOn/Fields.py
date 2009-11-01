from Products.Archetypes import atapi
from Products.Archetypes.public import DisplayList
from Widgets import LinkWidget, USPhoneWidget, EmailWidget, AddressWidget, \
    InstructionWidget, SimpleDataGridWidget


class USAddressField(atapi.TextField):
    """A field that stores strings"""
    _properties = atapi.TextField._properties.copy()
    _properties.update(
        {'widget': AddressWidget,
         'validators': ('isUSAddress',),
         })


class LinkField(atapi.StringField):
    """A field that stores strings"""
    _properties = atapi.StringField._properties.copy()
    _properties.update(
        {'widget': LinkWidget,
         'validators': ('isURL',),
         })


class USPhoneField(atapi.StringField):
    """A field that stores strings"""
    _properties = atapi.StringField._properties.copy()
    _properties.update(
        {'widget': USPhoneWidget,
         'validators': ('isFormattedUSPhone',),
         })


class EmailField(atapi.StringField):
    """A field that stores strings"""
    _properties = atapi.StringField._properties.copy()
    _properties.update(
        {'widget': EmailWidget,
         'validators': ('isEmail',),
         })


class InstructionField(atapi.ObjectField):
    """Just help"""
    _properties = atapi.ObjectField._properties.copy()
    _properties.update({'widget': InstructionWidget})


class SimpleDataGridField(atapi.LinesField):
    """A lines field with embedded vertical bars for fields. If the
    columns property is set, the isValidGrid validator will ensure that
    the entered text has exactly that number of columns for each row.
    If strip_whitespace is True, the individual cells in the grid will
    be stripped of leading and trailing whitespace (that is, whitespace
    added around the delimiter).

    If column_names is set to a tuple or list of strings, it gives the names
    of columns in the grid. The getDataGridRow script and the getRow() method
    will return a dict using these column names as keys rather than using the
    column numbers (starting from zero).

    Fields are just strings, with no internal validation, etc.
    """
    _properties = atapi.LinesField._properties.copy()
    _properties.update(
        {'widget': SimpleDataGridWidget,
         'columns': None,
         'column_names': None,
         'validators': ('isValidGrid',),
         'strip_whitespace': True,
         'delimiter': '|',
         })

    def get(self, instance, **kwargs):
        data = atapi.LinesField.get(self, instance, **kwargs)
        return data

    def getAsGrid(self, instance, **kwargs):
        """Return a tuple of tuples - the outer tuple has one element
        per row in the grid, the inner tuple has one element per column
        in that row.
        """
        data = self.get(instance, **kwargs)
        rows = []
        for d in data:
            cols = self._split(d)
            rows.append(tuple(cols))
        return tuple(rows)

    def getRow(self, instance, key, keyCol=0, **kwargs):
        """Get a row matching the given key, looked up in the given column.

        Returns a dict. If the column_names property is not set, the
        keys of the dict are the integral column indexes. If it is
        set, the relevant column names are used as keys instead.
        """
        data = self.get(instance, **kwargs)
        for d in data:
            rowData = self._split(d)
            if rowData[keyCol] == self._strip(key):
                row = {}
                for i in range(0, len(rowData)):
                    key = self._getColName(i)
                    row[key] = rowData[i]
                return row

    def getColumn(self, instance, column, **kwargs):
        """Get a tuple of all values in the given column, indexed from 0.
        """
        data = self.get(instance, **kwargs)
        col = []
        for d in data:
            col.append(self._split(d)[column])
        return tuple(col)

    def lookup(self, instance, key, column, keyCol=0, **kwargs):
        """Look for the given key in the column with index given by keyCol,
        and return the value stored in the given column. Returns None if the
        value could not be found. Raises IndexError if the matching row
        does not have the requested column. Returns None if the value could
        not be found.
        """
        data = self.get(instance, **kwargs)
        for d in data:
            cols = self._split(d)
            if cols[keyCol] == self._strip(key):
                return cols[column]
        return None

    def getAsDisplayList(self, instance, keyCol=0, valueCol=1, **kwargs):
        """Get two columns of each row as a DisplayList - the key columns is
        keyCol, and the value column is valueCol.
        """
        data = self.get(instance, **kwargs)
        lst = DisplayList()
        for d in data:
            cols = self._split(d)
            lst.add(cols[keyCol], cols[valueCol])
        return lst

    def _strip(self, value):
        """Strip whitespace from a value if applicable"""
        if self.strip_whitespace:
            return value.strip()
        else:
            return value

    def _split(self, row):
        """Return a row split on the delimiter, optionally stripped
        """
        return [self._strip(r) for r in row.split(self.delimiter)]

    def _getColName(self, column):
        """Get the name of the given column. If column_names is set, use
        that if it contains a value. Else, use the integral column name.
        """
        if self.column_names and len(self.column_names) > column:
            return self.column_names[column]
        else:
            return column

#-------- dyndoc helper classes

from AccessControl import getSecurityManager
from zope.tal.taldefs import TALExpressionError as TALESError

from Products.PageTemplates import PageTemplate
from Products.PageTemplates.ZopePageTemplate import SecureModuleImporter
from Acquisition import Implicit, aq_parent, aq_inner
from Persistence import Persistent


class ddPageTemplate(PageTemplate.PageTemplate, Implicit, Persistent):

    def pt_getContext(self):
        root = self.getPhysicalRoot()
        template = aq_parent(self)
        here = aq_parent(template)
        c = {'template': template,
             'options': {},
             'nothing': None,
             'request': None,
             'root': root,
             'request': getattr(root, 'REQUEST', None),
             'modules': SecureModuleImporter,
             'here': here,
             'context': here,
             'container': aq_inner(here),
             }
        return c

    def __setstate__(self, state):
        ddPageTemplate.inheritedAttribute('__setstate__')(self, state)
        self._cook()

#class Macros(Base):
#
# taken from CMFDynamicDocument
#
# should be easy to allow dyndocs to be used as a macro (uncomment
# this and stuff below), but not tested/not interested in this.

#    """
#    Evaluate to the macros collection of the contained page template.
#    """
#    def __of__( self, doc):
#        return doc.get_pt().macros


class DynamicField(atapi.TextField):
    """Just help"""
    _properties = atapi.ObjectField._properties.copy()
    _properties.update(
        {'widget': atapi.TextAreaWidget,
         'default_output_type': 'text/html',
         })

    #macros = Macros()
    #security.declareProtected(CMFCorePermissions.View, 'macros')

    def get_unwrapped(self, instance):
        """
        return unwrapped PageTemplate object
        """

        #import pdb
        #pdb.set_trace()
        #raise "foo",dir(fldname)
        try:
            return getattr(instance, self.getName()).__of__(instance)
        except:
            setattr(instance, self.getName(), ddPageTemplate())
            return getattr(instance, self.getName()).__of__(instance)

    def getRaw(self, instance, **kwargs):
        """Get raw"""

        # not sure if there's a better way to do this:
        # if this is our first access (ie, we haven't used property
        # before, then init to page template)
        # probably better handled in object's __init__ or addXXXX function,
        # both not sure how to handle __init__ properly, and
        # addXXXX function would make user of this fieldtype have to
        # create one for every class that used this field type.

        if not hasattr(instance, self.getName()):
            setattr(instance, self.getName(), ddPageTemplate())
        else:
            return self.get_unwrapped(instance).read()

    def set(self, instance, value, **kwargs):
        """
          Edit the document
        """
        pt = self.get_unwrapped(instance)
        pt.write(value)

    def get(self, instance, mimetype=None, raw=0, **kwargs):
        """Return"""
        pt = self.get_unwrapped(instance)

        if raw:
            # when would this happen? not sure, copying from TextField
            return pt.read()

        security = getSecurityManager()
        security.addContext(self)
        try:
            try:
                result = self.get_unwrapped(instance).pt_render(
                    extra_context={'user': security.getUser()})
            except TALESError, err:
                if err.type == 'Unauthorized':
                    raise err.type, err.value, err.traceback
                raise
            return result
        finally:
            security.removeContext(self)


__all__ = ('USAddressField', 'LinkField', 'USPhoneField', 'EmailField',
           'InstructionField', 'DynamicField', 'SimpleDataGridField')
