How to get ``recordId`` in record triggered flow
================================================

For record triggered flows the record that triggered the flow is automatically stored in the global variable ``{!$Record}``. 
You do not need to create a variable to store it as you can directly access it and any of the fields on the record:

* Record Id = ``{!$Record.Id}``.
* Record Type Name = ``{!$Record.RecordType.DeveloperName}``.
* Record Name = ``{!$Record.Name}``.
* Any other field = ``{!$Record.FIELD_NAME}``.

There is also a global variable ``{!$Flow.CurrentRecord}`` that contains the Record Id, but you can get all you need with ``{!$Record}``.

.. tab:: {!$Record.Id}

    .. figure:: /images/salesforce-core-record-id.png

.. tab:: {!$Flow.CurrentRecord}

    .. figure:: /images/salesforce-core-flow-current-record.png

.. tab:: {!$Record.FIELD_NAME}

    .. figure:: /images/salesforce-core-record-field-name.png


