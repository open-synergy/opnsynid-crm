# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "CRM Lead Status Check",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "category": "Customer Relationship Management",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "depends": [
        "crm_lead_funnel_type",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/res_groups_data.xml",
        "views/crm_lead_views.xml",
        "views/crm_status_check_menu.xml",
        "views/crm_status_check_item.xml",
        "views/crm_status_check_template.xml",
        "views/crm_lead_status_check.xml",
    ],
    "installable": True,
    "auto_install": False,
}
