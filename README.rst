ArchAddOn
=========

Straightforward toolbox of field types, widgets, and validators for
Archetypes.

Please feel free to add your own new fields, widgets, and validators
here, if you think they are general-purpose. I intend for this to be
not sample or learning archetypes add ons (ArchExample is for that),
but real-world usable toolbox pieces.

Features
--------

* New Fields for:

  - USAddress

  - USPhoneNumber

  - Email

  - Link

  - Instruction (only shows description on edit form, for adding
    sectional help or other HTML markup to an edit form)

  - DynamicField. This is a textual field that can contain TALES
    expressions which are evaluated. So you can add a "body" field to
    a schema that is of this type, and have it be a mix of HTML
    content and TALES expressions (just like in a ZPT).

  - SimpleDataGridField. A lines field with embedded vertical bars for
    fields. If the columns property is set, the isValidGrid validator
    will ensure that the entered text has exactly that number of
    columns for each row.  If strip_whitespace is True, the individual
    cells in the grid will be stripped of leading and trailing
    whitespace (that is, whitespace added around the delimiter).

    If column_names is set to a tuple or list of strings, it gives the names
    of columns in the grid. The getDataGridRow script and the getRow() method
    will return a dict using these column names as keys rather than using the
    column numbers (starting from zero).
    Fields are just strings, with no internal validation, etc.

* Matching widgets for these types

* Validators:

  - FormattedUSPhoneValidator: (999) 999-9999

  - USAddressValidator

  - isValidGrid


Requires
--------

Plone version 4.0 or higher.


Quickstart
----------

1) Use the quickinstaller_tool and install ArchAddOn

2) To create a sample object and test the new fields, widgets, etc.,
   go to the archetype_tool and install the "ArchAddOn Example" type,
   then add an object of that type.
