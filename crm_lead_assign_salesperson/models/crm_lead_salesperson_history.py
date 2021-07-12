# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CRMLeadSalespersonHistory(models.Model):
    _name = "crm.lead.salesperson_history"
    _description = "Salesperson history"

    lead_id = fields.Many2one(
        string="Lead",
        comodel_name="crm.lead",
        required=True,
    )
    user_id = fields.Many2one(
        string="Salesperson",
        comodel_name="res.users",
        required=True,
    )
