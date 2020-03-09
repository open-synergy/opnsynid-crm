# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import Warning as UserError


class CRMTeam(models.Model):
    _inherit = "crm.team"

    cron_id = fields.Many2one(
        string="Cron",
        comodel_name="ir.cron",
        readonly=True,
    )
    stage_auto_archieve_ids = fields.One2many(
        string="Auto Archieve(s)",
        comodel_name="crm.stage_auto_archieve",
        inverse_name="team_id",
    )

    @api.multi
    def action_create_cron(self):
        for document in self:
            document._generate_cron()

    @api.multi
    def action_delete_cron(self):
        for document in self:
            document.cron_id.unlink()

    @api.multi
    def _generate_cron(self):
        self.ensure_one()
        data = self._prepare_cron_data()
        obj_cron = self.env["ir.cron"]
        cron = obj_cron.create(data)
        self.write({"cron_id": cron.id})

    @api.multi
    def _prepare_cron_data(self):
        self.ensure_one()
        cron_name = "CRM Auto Archieve: %s" % (
            self.name)
        return {
            "name": cron_name,
            "user_id": self.env.user.id,
            "active": True,
            "interval_number": 1,
            "interval_type": "days",
            "numbercall": -1,
            "doall": False,
            "model_id": self.env.ref("crm.model_crm_team").id,
            "code": "model.cron_auto_archieve()",
            "state": "code",
        }

    @api.model
    def cron_auto_archieve(self):
        team_id = self.search([("active", "=", True)])[0]
        team_id._auto_archieve()

    @api.multi
    def _auto_archieve(self):
        obj_crm_lead = self.env["crm.lead"]
        for auto_archieve in self.stage_auto_archieve_ids:
            criteria = [
                ("stage_id", "=", auto_archieve.stage_id.id),
                ("day_on_stage", ">", auto_archieve.day_limit)
            ]
            lead_ids = obj_crm_lead.search(criteria)
            if lead_ids:
                for lead in lead_ids:
                    lead.write({"active": False})
