# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class CRMStageAutoArchieve(models.Model):
    _name = "crm.stage_auto_archieve"

    team_id = fields.Many2one(
        string="#Team",
        comodel_name="crm.team",
        required=True,
    )
    stage_id = fields.Many2one(
        string="Stage",
        comodel_name="crm.stage",
        required=True,
    )
    day_limit = fields.Float(
        string="Day Limit",
    )

    @api.multi
    @api.constrains(
        "team_id",
        "stage_id",
    )
    def _check_duplicate_stage(self):
        if self.stage_id:
            strWarning = _("No duplicate stage")
            check_stage = self.search(
                [("team_id", "=", self.team_id.id), ("stage_id", "=", self.stage_id.id)]
            )
            if len(check_stage) > 1:
                raise UserError(strWarning)
