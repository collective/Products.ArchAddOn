try:
    from Products.CMFCore.permissions import AddPortalContent
except ImportError:  # TODO do we really still need to support CMF < 1.5? 
    from Products.CMFCore.CMFCorePermissions import AddPortalContent

ADD_CONTENT_PERMISSION = AddPortalContent
PROJECTNAME = "ArchAddOn"
SKINS_DIR = 'skins'

GLOBALS = globals()
