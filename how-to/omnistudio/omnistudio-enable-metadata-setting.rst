Enable Metadata setting in OmniStudio
=====================================

To be able to deploy and retrieve OmniStudio components using the Metadata API, enable the OmniStudio Metadata Setting.

1. Navigate to Setup
2. Select OmniStudio Settings
3. Enable OmniStudio Metadata

.. warning::

    Once you enable the OmniStudio Metadata setting, you can't turn it off.

The process of enabling the setting checks all the OmniStudio component unique names for violations.
If Salesforce finds any violations, it sends an email listing all the components that doesn't conform to the requirement.

.. 

    | Your data migration for organization ID ORD_ID failed. 
    
    | Fix your data and enable OmniStudioMetadata again. 
    | These records had errors:
    | RECORD_ID_1 - Field must be alphanumeric and contain no spaces or underscores.
    | RECORD_ID_2 - Field must be alphanumeric and contain no spaces or underscores.

In the event of a trail org, these violations can be safely deleted as they're sample components most of the times.

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