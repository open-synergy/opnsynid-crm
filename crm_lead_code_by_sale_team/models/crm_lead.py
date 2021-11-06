# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    @api.model
    def create(self, vals):
        obj_crm_case_section = self.env["crm.case.section"]
        section_id = vals.get("section_id", False)

        if section_id:
            criteria = [("id", "=", section_id)]
            section = obj_crm_case_section.search(criteria)
            if section.lead_sequence_id:
                sequence = self.env["ir.sequence"].next_by_id(
                    section.lead_sequence_id.id
                )
                vals["code"] = sequence
        return super(CrmLead, self).create(vals)
