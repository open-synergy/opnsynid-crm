# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, api, fields
from datetime import datetime
import logging


class CRMLead(models.Model):
    _inherit = "crm.lead"

    @api.multi
    @api.depends(
        "date_last_stage_update",
    )
    def _compute_day_on_stage(self):
        dt_now = datetime.now()
        for document in self:
            date_last_stage_update =\
                document.date_last_stage_update
            conv_date =\
                datetime.strptime(
                    date_last_stage_update,
                    "%Y-%m-%d %H:%M:%S"
                )
            day_on_stage =\
                abs((dt_now-conv_date).days)
            document.day_on_stage = day_on_stage

    day_on_stage = fields.Float(
        string="Day On Stage",
        compute="_compute_day_on_stage",
        store=True,
    )

    @api.model
    def cron_update_day_on_stage(self):
        logging.info(u"Compute Day On Stage")

        lead_ids = self.search([("active", "=", True)])

        lead_ids._compute_day_on_stage()
