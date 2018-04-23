# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Sale Team Average Win Cycle",
    "version": "8.0.1.1.0",
    "website": "https://opensynergy-indonesia.com",
    "author": "OpenSynergy Indonesia",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "crm",
    ],
    "data": [
        "data/ir_cron_data.xml",
        "views/crm_case_section_views.xml",
        "views/crm_lead_views.xml",
    ],
}
