# Copyright 2021 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import Warning as UserError


class ChangeSalesperson(models.TransientModel):
    _name = "crm.lead.change_salesperson"
    _description = "Change Salesperson"

    @api.model
    def _default_lead_id(self):
        return self._context.get("active_id", False)

    lead_id = fields.Many2one(
        string="Lead/Opportunity",
        comodel_name="crm.lead",
        required=True,
        default=lambda self: self._default_lead_id(),
    )
    user_id = fields.Many2one(
        string="Salesperson",
        comodel_name="res.users",
        required=False,
    )

    @api.multi
    def action_confirm(self):
        for wiz in self:
            wiz._update_salesperson()

    @api.multi
    def _update_salesperson(self):
        self.ensure_one()
        if self.user_id == self.lead_id.user_id:
            msg = _("Salesperson must different than existing Salesperson")
            raise UserError(msg)
        user_id = self.user_id and self.user_id.id or False
        self.lead_id.write({"user_id": user_id})
        if self.user_id:
            obj_history = self.env["crm.lead.salesperson_history"]
            obj_history.create({"lead_id": self.lead_id.id, "user_id": self.user_id.id})
