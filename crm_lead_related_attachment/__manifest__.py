# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "CRM Lead Related Attachment",
    "version": "11.0.1.1.0",
    "license": "AGPL-3",
    "category": "Customer Relationship Management",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "depends": [
        "crm_lead_funnel_type",
        "ssi_related_attachment_mixin",
    ],
    "data": [
        "views/crm_lead_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
