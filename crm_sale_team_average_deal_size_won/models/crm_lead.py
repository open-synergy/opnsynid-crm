# -*- coding: utf-8 -*-
# Copyright 2017 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api, fields


class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.multi
    @api.depends(
        "section_id", "planned_revenue",
        "section_id.average_deal_size_won",
    )
    def _compute_over_average(self):
        for lead in self:
            lead.over_team_avg_deal_won = False
            if lead.section_id and lead.type == "opportunity" and \
                    lead.stage_id.probability != 100.00:
                if lead.planned_revenue > \
                        lead.section_id.average_deal_size_won:
                    lead.over_team_avg_deal_won = True

    over_team_avg_deal_won = fields.Boolean(
        string="Over Team Average Deal Size Won",
        compute="_compute_over_average",
        store=True,
    )
