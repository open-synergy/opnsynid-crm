# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "CRM Lead Workflow Policy",
    "version": "11.0.1.1.0",
    "license": "AGPL-3",
    "category": "Customer Relationship Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "depends": [
        "crm",
        "base_workflow_policy",
    ],
    "data": [
        "data/base_workflow_policy_data.xml",
        "views/crm_team_views.xml",
        "views/crm_lead_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
