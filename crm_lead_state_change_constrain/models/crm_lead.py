# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class CRMLead(models.Model):
    _inherit = "crm.lead"

    stage_change_constrain_template_id = fields.Many2one(
        string="Stage Change Constrain Template",
        comodel_name="crm.stage_change_constrain_template",
    )

    @api.onchange(
        "partner_id",
        "user_id",
        "team_id",
        "funnel_type_id",
    )
    def onchange_stage_change_constrain_template_id(self):
        obj_stage_change_cons_tmpl = self.env["crm.stage_change_constrain_template"]
        self.stage_change_constrain_template_id = False

        template_ids = obj_stage_change_cons_tmpl.search(
            [],
            order="sequence desc",
        )
        if template_ids:
            for template in template_ids:
                if self._evaluate_python_code(template):
                    self.stage_change_constrain_template_id = template.id
                    break

    @api.constrains(
        "stage_id",
    )
    def _check_stage_constrain(self):
        for document in self:
            if document.stage_change_constrain_template_id:
                detail_ids = document.stage_change_constrain_template_id.detail_ids
                check_detail_ids = detail_ids.filtered(
                    lambda r: r.stage_id == document.stage_id
                )
                if check_detail_ids:
                    status_check_item_ids = check_detail_ids.status_check_item_ids
                    status_check_ids = document.status_check_ids
                    for detail in status_check_item_ids:
                        status_check = status_check_ids.filtered(
                            lambda r: r.status_check_item_id.id == detail.id
                        )
                        if not status_check.status_ok:
                            item = status_check.status_check_item_id.name
                            msg_error = _("Check Status item: %s") % (item)
                            raise UserError(msg_error)
