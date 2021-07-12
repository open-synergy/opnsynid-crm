# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError
from odoo.tools.safe_eval import safe_eval as eval


class CRMLead(models.Model):
    _inherit = "crm.lead"

    status_check_template_id = fields.Many2one(
        string="Status Check Template", comodel_name="crm.status_check_template"
    )
    status_check_ids = fields.One2many(
        string="Check Status",
        comodel_name="crm.lead_status_check",
        inverse_name="lead_id",
    )

    @api.onchange(
        "partner_id",
        "user_id",
        "team_id",
        "funnel_type_id",
    )
    def onchange_status_check_template_id(self):
        obj_status_check_tmpl = self.env["crm.status_check_template"]
        self.status_check_template_id = False

        template_ids = obj_status_check_tmpl.search(
            [],
            order="sequence desc",
        )
        if template_ids:
            for template in template_ids:
                if self._evaluate_python_code(template):
                    self.status_check_template_id = template.id
                    break

    @api.onchange(
        "status_check_template_id",
    )
    def onchange_status_check_ids(self):
        res = []
        sequence = 0
        self.status_check_ids = [(5, 0, 0)]
        if self.status_check_template_id:
            detail_ids = self.status_check_template_id.detail_ids
            if detail_ids:
                for detail in detail_ids:
                    sequence += 1
                    new = self.status_check_ids.new(
                        {
                            "sequence": sequence,
                            "status_check_item_id": detail.status_check_item.id,
                        }
                    )
                    res.append(new.id)
            self.status_check_ids = res

    def _get_localdict(self, document):
        self.ensure_one()
        return {
            "env": self.env,
            "document": document,
        }

    @api.multi
    def _evaluate_python_code(self, template):
        res = False
        localdict = self._get_localdict(self)
        try:
            eval(template.python_code, localdict, mode="exec", nocopy=True)
            res = localdict["result"]
        except Exception as error:
            raise UserError(_("Error evaluating conditions.\n %s") % error)
        return res
