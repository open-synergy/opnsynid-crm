# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models


class CreateMasterProject(models.TransientModel):
    _name = "business.create_master_project"
    _description = "Create Master Project"

    @api.model
    def _default_lead_id(self):
        return self._context.get("active_id", False)

    name = fields.Char(
        string="Project Name",
    )
    parent_analytic_id = fields.Many2one(
        string="Parent Analytic Account",
        comodel_name="account.analytic.account",
    )
    lead_id = fields.Many2one(
        string="Lead/Opportunity",
        comodel_name="crm.lead",
        required=True,
        default=lambda self: self._default_lead_id(),
    )

    @api.multi
    def action_confirm(self):
        for wiz in self:
            wiz._create_project()

    @api.multi
    def _create_project(self):
        self.ensure_one()
        obj_project = self.env["project.project"]
        project = obj_project.create(self._prepare_project_data())
        self.lead_id.write({"project_id": project.id})

    @api.multi
    def _prepare_project_data(self):
        self.ensure_one()
        lead = self.lead_id
        return {
            "name": self.name or lead.name,
            "partner_id": lead.partner_id
            and lead.partner_id.commercial_partner_id.id
            or False,
            "parent_id": self.parent_analytic_id
            and self.parent_analytic_id.id
            or False,
            "user_id": lead.user_id.id,
        }
