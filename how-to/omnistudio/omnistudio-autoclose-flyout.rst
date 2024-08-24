Auto-close flyout
=================

See Salesforce `help file <https://help.salesforce.com/s/articleView?id=sf.os_fire_an_event_to_automatically_close_a_flyout_modal_27434.htm&type=5>`_ with regards to this topic.

The default way to close a flyout launched from a Flexcard, is to press the close button on the right top of the flyout once done.

The Flexcard can automatically close the flyout with a Pub/Sub event sent from the flyout when it needs to close.
When configuring the flyout, take note of the ``Channel Name``:

.. figure:: /images/omnistudio-flyout-channel-name.png

You can keep the default name of ``close_modal``.

You can close the flyout when the user clicks the last time on the ``Next`` button on a Step element in an OmniScript flyout.
The last ``Next`` button label can change to something more descriptive such as ``Save``/``Close``/``Finish`` etc.

To ensure there is a ``Next`` button on the last Step element in the Omniscript, some other element needs to follow the last Step element.
A DataRaptor or Integration Procedure usually follows the last Step that processes the data, but if in your scenario there is none, you can add a Set Values element.

.. tab:: Step element last

    .. figure:: /images/omnistudio-step-element-last.png

.. tab:: Step element not last

    .. figure:: /images/omnistudio-step-element-not-last.png

On the last element in the Omniscript flyout, enable ``Pub/Sub`` inside the Messaging Framework section.
Leave the Message Key/Value pair empty.

.. figure:: /images/omnistudio-enable-pubsub-on-element.png

Next, add an event listener to the Flexcard that launched the flyout:

Set the following:

* **Event Type**: ``Pubsub``
* **Channel Name**: ``omniscript_action``
* **Event Name**: ``data``

This ensures the event listener picks up the Pub/Sub triggered by the last element in the Omniscript flyout
Configure the action that closes the flyout:

* **Action Type**: ``Event``
* **Event Type**: ``PubSub``
* **Channel Name**: ``close_modal``
* **Event Name**: ``close``

.. figure:: /images/omnistudio-close-flyout-event-listener.png

