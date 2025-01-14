from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'


    affiliate_id = fields.Many2one('crm.affiliate', string="Affiliate")
    priority = fields.Selection(
        [('0', 'Low'),('2', 'Normal'),('3', 'High')],
        string="Priority",compute='_compute_priority',store=True)
    
    
    # when click on button for change stage to Won, while an outdated affiliate is selected, show an error
    def validate_affiliate(self):
        if self.affiliate_id and self.affiliate_id.is_outdated:
            raise ValidationError("You cann't mark as won a lead with an outdated affiliate!")
    
    
    def action_set_won(self):
        '''override set won button on base to validate if affiliate is outdated'''
        self.validate_affiliate()
        return super().action_set_won()
    
    def _pls_get_lead_pls_values(self, domain=[]):
        '''override onchange won stage on base to validate if affiliate is outdated'''
        if self.stage_id.is_won:
            self.validate_affiliate()
            
        return super()._pls_get_lead_pls_values(domain=domain)

    @api.depends('affiliate_id')
    def _compute_priority(self):
        # It should be "high" if an affiliate is selected and "normal" when not
        for lead in self:
            lead.priority = '3' if lead.affiliate_id else '2'
