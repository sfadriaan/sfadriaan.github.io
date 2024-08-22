Check OmniStudio package version
================================

Salesforce releases updates to the OmniStudio Managed Package during every release cycle i.e. Spring, Summer, and Winter.
Updates to the OmniStudio Managed Package should happen automatically in your production org.

In the event that you have a trail org that has an outdated version, or your production org hasn't updated automatically, you can manually update the managed package.

1. Check latest version by visiting the `OmniStudio Release page <https://help.salesforce.com/s/articleView?id=000394906&type=1>`_
2. Check which version is in your org:
    a. Navigate to Setup
    b. Search ``Installed Packages``
    c. Search for Package Name ``Omnistudio``
    d. Check version number

    .. figure:: /images/omnistudio-outdated-package-version.png

    e. For outdated versions, follow the instructions in the `OmniStudio Release page <https://help.salesforce.com/s/articleView?id=000394906&type=1>`_ to install the latest version.
    f. After the updates/installation has completed, verify that the Installed Package version is correct.

    .. figure:: /images/omnistudio-latest-package-version.png
