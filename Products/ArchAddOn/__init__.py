from Globals import package_home
from Products.Archetypes.public import process_types, listTypes
from Products.CMFCore import utils
from Products.CMFCore.DirectoryView import registerDirectory
import os, os.path

from Products.validation import validation
from Validators import *

from config import ADD_CONTENT_PERMISSION, PROJECTNAME, SKINS_DIR, GLOBALS

registerDirectory(SKINS_DIR, GLOBALS)

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    validation.register(FormattedUSPhoneValidator('isFormattedUSPhone'))
    validation.register(USAddressValidator('isUSAddress'))
    validation.register(LinesAllFloatValidator('areLinesFloat'))
    validation.register(LinesAllIntValidator('areLinesInt'))
    validation.register(SimpleDataGridValidator('isValidGrid'))
    
    ##Import Types here to register them
    # import SomeType

    import Example

    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)
    
    utils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)
    

