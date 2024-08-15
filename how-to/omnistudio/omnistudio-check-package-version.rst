Check OmniStudio Package Version
================================

Updates to the OmniStudio Managed Package are released with the Salesforce release cycle i.e. Spring, Summer, and Winter.
If OmniStudio is installed in your production environment, updates should happen automatically.

In the event that you have a trail org that has an outdated version (or your production org has not updated automatically), you can manually update the managed package.

1. Check latest version by visiting the `OmniStudio Release page <https://help.salesforce.com/s/articleView?id=000394906&type=1>`_
2. Check which version is installed in your org (production org or trail org)
    a. Navigate to Setup
    b. Search ``Installed Packages``
    c. Search for Package Name ``Omnistudio``
    d. Check version number

    .. figure:: /images/omnistudio-outdated-package-version.png

    e. If the version is outdated, follow the instructions in the `OmniStudio Release page <https://help.salesforce.com/s/articleView?id=000394906&type=1>`_ to install the latest version.
    f. After the updates/installation has completed, verify that the Installed Package version is correct.

    .. figure:: /images/omnistudio-latest-package-version.png
