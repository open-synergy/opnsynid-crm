# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from datetime import datetime
from openerp import models, api, fields


class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.multi
    @api.depends(
        "create_date", "stage_id",
        "date_closed",
    )
    def _compute_day_elapsed(self):
        for lead in self:
            lead.day_elapsed = 0.0
            if lead.section_id and lead.type == "opportunity" and \
                    lead.stage_id.probability != 100.00:
                lead.day_elapsed = lead.day_close
            else:
                date_create = datetime.strptime(
                    lead.create_date, "%Y-%m-%d %H:%M:%S")
                today = datetime.now()
                lead.day_elapsed = (today - date_create).days

    @api.multi
    @api.depends(
        "section_id", "date_closed",
        "stage_id",
        "section_id.win_cycle",
    )
    def _compute_win_cycle(self):
        for lead in self:
            lead.over_team_avg_win_cycle = False
            if lead.section_id and lead.type == "opportunity" and \
                    lead.stage_id.probability != 100.00:
                if lead.day_elapsed > \
                        lead.section_id.average_win_cycle:
                    lead.over_team_avg_win_cycle = True

    day_elapsed = fields.Float(
        string="Day Elapsed",
        compute="_compute_day_elapsed",
        store=True,
    )
    over_team_avg_win_cycle = fields.Boolean(
        string="Over Team Average Win Cycle",
        compute="_compute_over_average",
        store=True,
    )

    @api.model
    def _update_day_elapsed(self):
        obj_lead = self.env["crm.lead"]
        criteria = [
            ("type", "=", "opportunity"),
            ("stage_id.probability", "!=", 100.00),
        ]
        obj_lead.search(criteria)._compute_day_elapsed()
