# Copyright 2025 ForgeFlow S.L. (https://www.forgeflow.com)
# Copyright 2025 ACSONE SA/NV (https://www.acsone.eu)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CrmLead(models.Model):
    _inherit = "crm.lead"

    stage_id = fields.Many2one(check_company=True)

    @api.model
    def _read_group_stage_ids(self, stages, domain, order):
        # Only return the stages the user has access to due to the new
        # multi company rule
        res = super()._read_group_stage_ids(stages, domain, order)
        return stages.search([("id", "in", res.ids)])

    @api.depends("team_id", "type", "company_id")
    def _compute_stage_id(self):
        for lead in self:
            if not lead.stage_id:
                lead.stage_id = lead._stage_find(
                    domain=[
                        ("fold", "=", False),
                        ("company_id", "in", [False, lead.company_id.id]),
                    ]
                ).id
