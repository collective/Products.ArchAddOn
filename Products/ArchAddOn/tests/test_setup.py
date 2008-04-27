from base import ArchAddOnTestCase
from Products.Archetypes.Extensions.utils import installTypes
from Products.Archetypes.public import listTypes
from Products.ArchAddOn.config import PROJECTNAME
from StringIO import StringIO

class TestProductInstall(ArchAddOnTestCase):

    def afterSetUp(self):
        out=StringIO()
        installTypes(self.portal, out,
                     listTypes(PROJECTNAME),
                     PROJECTNAME)
        self.types = ('ArchAddOnExample',)

    def testTypesInstalled(self):
        for t in self.types:
            self.failUnless(t in self.portal.portal_types.objectIds(),
                            '%s content type not installed' % t)

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    return suite
