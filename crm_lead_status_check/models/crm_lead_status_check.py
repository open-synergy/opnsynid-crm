# -*- coding: utf-8 -*-
# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError
from odoo.tools.safe_eval import safe_eval as eval


class CRMLeadStatusCheck(models.Model):
    _name = "crm.lead_status_check"
    _description = "CRM Lead Status Check"

    lead_id = fields.Many2one(
        string="#Lead",
        comodel_name="crm.lead",
    )
    sequence = fields.Integer(
        string="Sequence",
        default=1,
    )
    status_check_item_id = fields.Many2one(
        string="Status Check Item",
        comodel_name="crm.status_check_item",
    )

    @api.multi
    def _compute_status_ok(self):
        for document in self:
            document.status_ok = False
            result = \
                document._evaluate_python_code()
            if result:
                document.status_ok = result

    status_ok = fields.Boolean(
        string="Status Ok",
        compute="_compute_status_ok"
    )

    def _get_localdict(self, document):
        self.ensure_one()
        return {
            "env": self.env,
            "document": document.lead_id,
        }

    @api.multi
    def _evaluate_python_code(self):
        res = False
        localdict = self._get_localdict(self)
        try:
            eval(self.status_check_item_id.python_code,
                 localdict, mode="exec", nocopy=True)
            res = localdict["result"]
        except Exception as error:
            raise UserError(_(
                "Error evaluating conditions.\n %s") % error)
        return res
