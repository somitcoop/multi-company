### 1. Migration to Odoo 17.0
**Problem/Requirement**: Migrate module from Odoo 18.0 to Odoo 17.0.

**Solution**:
- [Backend]: Update `_read_group_stage_ids` signature in `crm.lead`.
- [Files]: `models/crm_lead.py`, `__manifest__.py`, `views/crm_stage.xml`.
