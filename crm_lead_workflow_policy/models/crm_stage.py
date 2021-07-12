# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class CRMStage(models.Model):
    _inherit = "crm.stage"

    allowed_stage_ids = fields.Many2many(
        string="Allowed Stages",
        comodel_name="crm.stage",
        relation="rel_stage_allowed_stage",
        column1="parent_stage_id",
        column2="stage_id",
    )
