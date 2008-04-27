from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.ArchAddOn.config import *

from StringIO import StringIO

def install(self):
    out = StringIO()

    # make this true to install sample types
    if 0:
        installTypes(self, out,
                     listTypes(PROJECTNAME),
                     PROJECTNAME)

    install_subskin(self, out, GLOBALS)

    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()
