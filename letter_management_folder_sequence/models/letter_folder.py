# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import fields, models


class LetterFolder(models.Model):
    _inherit = "letter.folder"

    sequence_id = fields.Many2one(string="Sequence", comodel_name="ir.sequence")
