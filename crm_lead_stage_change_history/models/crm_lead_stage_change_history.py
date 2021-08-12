# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import fields, models


class CRMLeadStageChangeHistory(models.Model):
    _name = "crm.lead_stage_change_history"
    _description = "CRM Lead Stage Change History"

    lead_id = fields.Many2one(
        string="# Lead",
        comodel_name="crm.lead",
        ondelete="cascade",
        required=True,
    )
    user_id = fields.Many2one(
        string="User",
        comodel_name="res.users",
        required=True,
    )
    stage_from_id = fields.Many2one(
        string="Stage From",
        comodel_name="crm.stage",
        required=True,
    )
    stage_to_id = fields.Many2one(
        string="Stage To",
        comodel_name="crm.stage",
        required=True,
    )
    date_change = fields.Datetime(
        string="Date Change",
        required=True,
    )
