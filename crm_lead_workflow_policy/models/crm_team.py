# -*- coding: utf-8 -*-
# Copyright 2020 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class CRMTeam(models.Model):
    _inherit = "crm.team"

    lead_won_group_ids = fields.Many2many(
        string="Allowed to Won",
        comodel_name="res.groups",
        relation="rel_team_won_groups",
        column1="team_id",
        column2="group_id",
    )
    lead_lost_group_ids = fields.Many2many(
        string="Allowed to Lost",
        comodel_name="res.groups",
        relation="rel_team_lost_groups",
        column1="team_id",
        column2="group_id",
    )
    lead_archieve_group_ids = fields.Many2many(
        string="Allowed to Archieve",
        comodel_name="res.groups",
        relation="rel_team_archieve_groups",
        column1="team_id",
        column2="group_id",
    )
    lead_restore_group_ids = fields.Many2many(
        string="Allowed to Restore",
        comodel_name="res.groups",
        relation="rel_team_restore_groups",
        column1="team_id",
        column2="group_id",
    )
