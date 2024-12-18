How to create an integration user in Salesforce
===============================================

Salesforce introduced the Salesforce Integration User License with the `Spring '23 release <https://help.salesforce.com/s/articleView?id=release-notes.rn_api_integration_license.htm&release=242&type=5>`_.
Depending on your Salesforce Instance, you get one or more licenses for free.

Set up procedure
----------------

Select the following options when creating a new Integration User:

* **User License**: Salesforce Integration
* **Profile**: Minimum Access - API Only Integrations

Next, assign the relevant permission sets to the user:

* Under “Permission Set License Assignments” assign the “Salesforce API Integration” Permission Set License.
* Create a custom Permission Set for the integration user giving it the necessary permissions as per your use case.

Add all permissions required by the external system to the newly created custom Permission Set. 

Other considerations
--------------------

Follow the below steps to enable the following permissions:

Record types
''''''''''''

The user's default record types are on the Profile level. 
Assign additional record types via the custom Permission Set.

Take the following steps to assign/change a default record type for a given object:

* Disable “Enhanced Profile User Interface” setting by going to Setup -> User Management Settings.
* Select the “Minimum Access - API Only Integrations” profile and change/add the default record type for the relevant object.

Classic email templates
'''''''''''''''''''''''

The `Salesforce documentation <https://help.salesforce.com/s/articleView?id=sf.email_templates_perms.htm&type=5>`_ specifies how to grant access to email templates and email template folders via the Permission Set user interface. 

Even with the necessary permissions provided, the API user doesn't have access to the relevant email templates. 
It's necessary to add additional permissions programmatically by updating the metadata of the custom Permission Set. 

Take the following steps:

1. Retrieve the metadata of the relevant custom Permission Set
    a. Do this either via `Workbench <https://workbench.developerforce.com/login.php>`_ or the `SF command-line tool <https://developer.salesforce.com/docs/atlas.en-us.sfdx_cli_reference.meta/sfdx_cli_reference/cli_reference_top.htm>`_.
    b. Example SF command-line tool command for retrieving Permission Set metadata:

.. code:: bash

    sf project retrieve start --metadata PermissionSet:NAME_OF_PERMISSION_SET -o ORG_ALIAS

2. Add the following system permission:

.. code:: xml

    <userPermissions>
      <enabled>true</enabled>
      <name>EmailTemplateManagement</name>
    </userPermissions>

2. Deploy the updated metadata to the relevant Salesforce org.



.. raw:: html

    <embed>
        <script src="https://giscus.app/client.js"
            data-repo="sfadriaan/sfadriaan.github.io"
            data-repo-id="R_kgDOMjpG6Q"
            data-category="General"
            data-category-id="DIC_kwDOMjpG6c4Chwzv"
            data-mapping="pathname"
            data-strict="0"
            data-reactions-enabled="1"
            data-emit-metadata="0"
            data-input-position="bottom"
            data-theme="preferred_color_scheme"
            data-lang="en"
            crossorigin="anonymous"
            async>
        </script>
    </embed>
