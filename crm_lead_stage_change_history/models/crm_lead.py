# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class CRMLead(models.Model):
    _inherit = "crm.lead"

    stage_history_ids = fields.One2many(
        string="Stage Change History",
        comodel_name="crm.lead_stage_change_history",
        inverse_name="lead_id",
    )
    stage_history_summary_ids = fields.One2many(
        string="Stage Change Summary",
        comodel_name="crm.lead_stage_change_history_summary",
        inverse_name="lead_id",
    )

    @api.multi
    def _track_subtype(self, init_values):
        _super = super(CRMLead, self)
        self.ensure_one()
        if "stage_id" in init_values:
            init_stage_id = init_values["stage_id"]
            if init_stage_id and self.stage_id:
                self.create_stage_change_history(init_values["stage_id"].id)
        return _super._track_subtype(init_values)

    @api.multi
    def _prepare_stage_change_history(self, stage_from_id):
        self.ensure_one()
        values = {
            "lead_id": self.id,
            "user_id": self.env.user.id,
            "stage_from_id": stage_from_id,
            "stage_to_id": self.stage_id.id,
            "date_change": fields.Datetime.now(),
        }
        return values

    @api.multi
    def create_stage_change_history(self, stage_from_id):
        self.ensure_one()
        obj_stage_change_history = self.env["crm.lead_stage_change_history"]
        obj_stage_change_history.create(
            self._prepare_stage_change_history(stage_from_id)
        )
        return True
