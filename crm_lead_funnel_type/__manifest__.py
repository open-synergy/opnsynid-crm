# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# pylint: disable=locally-disabled, manifest-required-author
{
    "name": "CRM Funnel Type",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "category": "Customer Relationship Management",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "depends": [
        "crm",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/res_groups_data.xml",
        "security/ir_rule_data.xml",
        "views/crm_lead_views.xml",
        "views/crm_funnel_type_views.xml"
    ],
    "installable": True,
    "auto_install": False,
}
