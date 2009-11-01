from Products.Archetypes.Widget import StringWidget, TextAreaWidget
from Products.Archetypes.Widget import LinesWidget


class LinkWidget(StringWidget):
    _properties = StringWidget._properties.copy()
    _properties.update(
        {'size': '60',
         'maxlength': '255',
         'description': ("Enter the web address (URL). You can copy & paste "
                         "this from a browser window."),
         'macro': 'archaddon_widgets/link',
         })


class USPhoneWidget(StringWidget):
    _properties = StringWidget._properties.copy()
    _properties.update(
        {'size': '20',
         'maxlength': '20',
         'description': ("Enter phone number in the form '(800) 555-1212'. "
                         "Don't forget the area code."),
         })


class EmailWidget(StringWidget):
    _properties = StringWidget._properties.copy()
    _properties.update(
        {'size': '40',
         'maxlength': '60',
         'macro': 'archaddon_widgets/email',
         })


class AddressWidget(TextAreaWidget):
    _properties = TextAreaWidget._properties.copy()
    _properties.update(
        {'rows': 3,
         'cols': 40,
         'description': ("Enter the address, putting each address line on a "
                         "separate line."),
         #'macro':'archaddon_widgets/address'
         })


class InstructionWidget(StringWidget):
    _properties = StringWidget._properties.copy()
    _properties.update(
        {'macro': 'archaddon_widgets/instruction',
         'modes': ('edit',),
         'visible': {'view': 0, 'edit': 'visible'},
         })


class SimpleDataGridWidget(LinesWidget):
    _properties = LinesWidget._properties.copy()
    #_properties.update(
    #    {#'macro':'archaddon_widgets/instruction',
    #        })


__all__ = ('LinkWidget', 'USPhoneWidget', 'EmailWidget', 'AddressWidget',
           'InstructionWidget', 'SimpleDataGridWidget')
