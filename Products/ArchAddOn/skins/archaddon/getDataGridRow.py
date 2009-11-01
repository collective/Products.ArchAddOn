## Script (Python) "getDataGridRow"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=fieldName, key, keyColumn=0
##title=Get the entire data-grid row of a given field

# Looks for the given data grid field in the current context and its
# acquisition parents. Once found, look up the given key in the given column
# (defaults to 0 - the first column) and return the row.

# Returns a dict. If the field has the column_names property set, use these
# as the dict keys. Else use the column index as keys, starting from 0.

obj = context

while obj is not None:
    if hasattr(obj, 'Schema') and obj.Schema().has_key(fieldName):
        # Found it
        break
    else:
        if hasattr(obj, 'aq_parent'):
            obj = obj.aq_parent
        else:
            obj = None
            break

if obj is None:
    raise AttributeError, "Field %s not found" % (fieldName,)

return obj.getWrappedField(fieldName).getRow(obj, key, keyColumn)
