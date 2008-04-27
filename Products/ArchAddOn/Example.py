from Products.Archetypes.public import *
from Fields import *
from Widgets import *

Schema = BaseSchema.copy() + Schema((
    USAddressField( 'usaddress' ),
    LinkField( 'link' ),
    USPhoneField( 'usphone' ),
    EmailField( 'email' ),
    InstructionField( 'instruction', widget=InstructionWidget( description='This is an instruction' )),

    #XXX: This breaks the example so better to fix or not include. 
    #DynamicField( 'dynamic' ), 

    SimpleDataGridField( 'datagrid',
        column_names=('col1', 'col2', 'col3'),
        columns=3,
        default=[
            'row1|Row 1|Row 1 Description',
            'row2|Row 2|Row 2 Description',
        ],
        widget=SimpleDataGridWidget(
            label='Datagrid',
            description='Datagrid',
            rows=2,
        )),
    ))

class ArchAddOnExample(BaseContent):
    """Example of all of our field types."""

    schema = Schema
    content_icon = 'document_icon.gif'
    archetypes_name = 'ArchAddOn Example'

registerType(ArchAddOnExample)
