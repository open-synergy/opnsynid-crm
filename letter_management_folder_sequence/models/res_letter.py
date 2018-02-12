# -*- coding: utf-8 -*-
# Copyright 2018 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, api


class ResLetter(models.Model):
    _inherit = "res.letter"

    @api.model
    def create(self, values):
        res = super(ResLetter, self).create(values)

        obj_sequence = self.env["ir.sequence"]
        if res.folder_id.sequence_id:
            sequence = res.folder_id.sequence_id
            number = obj_sequence.next_by_id(sequence.id)
            res.write({"number": number})
        return res
