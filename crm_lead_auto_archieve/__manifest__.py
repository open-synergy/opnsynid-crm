# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "CRM Lead Day Auto Archieve",
    "version": "11.0.1.0.1",
    "license": "AGPL-3",
    "category": "Customer Relationship Management",
    "website": "https://simetri-sinergi.id",
    "author": "PT. Simetri Sinergi Indonesia, OpenSynergy Indonesia",
    "depends": [
        "crm_lead_day_on_stage",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/crm_team_views.xml",
    ],
    "installable": True,
    "auto_install": False,
}
