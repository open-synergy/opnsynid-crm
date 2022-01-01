# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CRMLead(models.Model):
    _name = "crm.lead"
    _inherit = [
        "crm.lead",
    ]

    date_won_manual = fields.Date(
        string="Manual Date Won",
    )
