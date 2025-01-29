from odoo import models, fields,_,api
from odoo.exceptions import MissingError,ValidationError,UserError
from datetime import date

class CrmAffiliate(models.Model):
    _name = "crm.affiliate"
    _description = "CRM Affiliates"
    _inherit = 'mail.thread'
    _order = 'name'
            


    name = fields.Char('Name', copy=False,required=True)
    # partner_id = fields.Many2one('res.partner','Partner', tracking=True, required=True)
    is_outdated = fields.Boolean(string="Outdated", default=False, tracking=True)
    outdated_date = fields.Date(string="Outdated Date", readonly=True)
    email = fields.Char(string='Email', tracking=True,required=True)
    phone = fields.Char(string='Phone', readonly=False, store=True, tracking=True)
    mobile = fields.Char(string='Mobile', readonly=False, store=True, tracking=True)
    
    
    # "outdated_date" field should be automatically filled when the is_outdated field is ticked.
    @api.onchange('is_outdated')
    def _onchange_is_outdated(self):
        if self.is_outdated:
            self.outdated_date = date.today()
        else:
            self.outdated_date = ''
            
    
    # Check for preventing duplicate affiliate based on email address.
    @api.constrains('email')
    def _check_email(self):
        for rec in self:
            count_email = self.search_count([('email', '=', rec.email)])
            if count_email > 1:
                raise ValidationError('The email already exist!')
