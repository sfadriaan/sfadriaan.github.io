Datable events
==============

Short description
-----------------

What platform events are available when using the datatable component in a flexcard.

`Salesforce help files <https://help.salesforce.com/s/articleView?id=sf.os_flexcards_datatable_properties_29884.htm&type=5>`_ mentions datatable events:

* ``update``
* ``selectrow``
* ``rowclick``
* ``delete``

as available when a user interacts with the datatable component in a flexcard.

.. figure:: /images/omnistudio-datatable-event-examples.gif

Long description
----------------

``update`` event
''''''''''''''''

The ``update`` event fires when table data changes.

A few things that it **doesn't** do:

* the updated values aren't exposed by the event, 
* it doesn't update the JSON node ``{records}`` with the newest data

``selectrow`` event
'''''''''''''''''''

When selecting a row on the datatable, the ``selectrow`` event fires. 
Enable the "User Selectable Row" on the datatable component properties for a user to select a row that fires the ``selectrow`` event.

.. figure:: /images/omnistudio-datatable-selectrow-event.gif

Some considerations that you need to take into account when using this event:

* The ``{action.result.FIELD_NAME}`` only contains the latest selected or de-selected row's information.
* The Salesforce documentation says that the event fires when a row is "updated," but that's not the case; it only fires when selecting or de-selecting a row.
* When selecting the option to select all the rows, the datable event doesn't return any data.

``rowclick`` event
''''''''''''''''''

When clicking on a datatable row, the ``rowclick`` event fires.
The ``rowclick`` event contains the information of the record of the row on which the user clicked.

.. figure:: /images/omnistudio-datatable-rowclick-event.gif

Some observations:

* The ``{action.result.FIELD_NAME`` contains the latest clicked on row's information.
* You don't need to click a cell's information, it can be anywhere on the row.
* When you do cell level edits or row level edits, the click to edit fires the event.

``delete`` event
''''''''''''''''

When deleting a row, the ``delete`` event fires.
Make sure to enable the ``Row Delete`` attribute of the datatable component to ensure the user has the option to delete a row in the datatable.

.. figure:: /images/omnistudio-datatable-delete-event.gif