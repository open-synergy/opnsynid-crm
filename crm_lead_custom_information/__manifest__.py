# Copyright 2022 OpenSynergy Indonesia
# Copyright 2022 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "CRM Custom Information",
    "version": "11.0.1.0.0",
    "license": "LGPL-3",
    "category": "Customer Relationship Management",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "depends": [
        "crm_lead_funnel_type",
        "ssi_custom_information_mixin",
    ],
    "data": [
        "views/crm_lead_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
