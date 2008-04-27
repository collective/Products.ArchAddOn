
from base import ArchAddOnTestCase
from Products.Archetypes.Extensions.utils import installTypes
from Products.Archetypes.public import listTypes
from Products.ArchAddOn.config import PROJECTNAME
from StringIO import StringIO

class TestFields(ArchAddOnTestCase):

    def afterSetUp(self):
        out=StringIO()
        installTypes(self.portal, out,
                     listTypes(PROJECTNAME),
                     PROJECTNAME)
        self.types = ('ArchAddOnExample',)
        self.setRoles(('Manager',))
        self.portal.invokeFactory('ArchAddOnExample', 'aao')
        self.aao = self.portal.aao

    # Test these fields
    #    USAddressField( 'usaddress' ),
    #    LinkField( 'link' ),
    #    USPhoneField( 'usphone' ),
    #    EmailField( 'email' ),
    #    InstructionField( 'instruction', widget=InstructionWidget( description='This is an instruction' )),
    #    DynamicField( 'dynamic' ),
    #    SimpleDataGridField('datagrid'),

    def testSimpleDataGridField(self):
        self.aao.setDatagrid('row1|Row 1|Description of Row 1')
        self.assertEqual(self.aao.getField('datagrid').lookup(self.aao, 'row1', 1), 'Row 1')

    # XXX: Add tests for the rest of the fields.

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestFields))
    return suite
