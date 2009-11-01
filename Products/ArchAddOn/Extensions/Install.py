from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, install_subskin
from Products.ArchAddOn.config import PROJECTNAME, GLOBALS
from Products.ArchAddOn.config import INSTALL_SAMPLE_TYPES

from StringIO import StringIO


def install(self):
    out = StringIO()

    if INSTALL_SAMPLE_TYPES:
        installTypes(self, out,
                     listTypes(PROJECTNAME),
                     PROJECTNAME)

    install_subskin(self, out, GLOBALS)

    print >> out, "Successfully installed %s." % PROJECTNAME
    return out.getvalue()
