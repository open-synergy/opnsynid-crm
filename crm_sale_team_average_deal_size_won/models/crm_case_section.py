# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class CrmCaseSection(models.Model):
    _inherit = "crm.case.section"

    @api.multi
    def _compute_average_deal(self):
        obj_lead = self.env["crm.lead"]
        for team in self:
            team.average_deal_size_won = 0.0
            criteria = [
                ("type", "=", "opportunity"),
                ("stage_id.probability", "=", 100.00),
                ("stage_id.on_change", "=", True),
                ("section_id", "=", team.id),
            ]
            opportunities = obj_lead.search(criteria)
            if len(opportunities) > 0:
                planned_revenues = opportunities.mapped("planned_revenue")
                team.average_deal_size_won = sum(planned_revenues) / float(
                    len(planned_revenues)
                )

    average_deal_size_won = fields.Float(
        string="Average Deal Size Won",
        compute="_compute_average_deal",
    )
