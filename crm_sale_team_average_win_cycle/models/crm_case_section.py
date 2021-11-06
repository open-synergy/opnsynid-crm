# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class CrmCaseSection(models.Model):
    _inherit = "crm.case.section"

    @api.multi
    def _compute_average_win_cycle(self):
        obj_lead = self.env["crm.lead"]
        for team in self:
            team.average_win_cycle = 0.0
            criteria = [
                ("type", "=", "opportunity"),
                ("stage_id.probability", "=", 100.00),
                ("stage_id.on_change", "=", True),
                ("section_id", "=", team.id),
            ]
            opportunities = obj_lead.search(criteria)
            if len(opportunities) > 0:
                day_close = opportunities.mapped("day_close")
                team.average_win_cycle = sum(day_close) / float(len(day_close))

    average_win_cycle = fields.Float(
        string="Average Win Cycle",
        compute="_compute_average_win_cycle",
    )
