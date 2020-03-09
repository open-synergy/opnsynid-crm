# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "CRM Lead Day On Stage",
    "version": "11.0.1.0.0",
    "license": "AGPL-3",
    "category": "Customer Relationship Management",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "depends": [
        "crm",
    ],
    "data": [
        "data/ir_cron.xml",
        "views/crm_lead_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
