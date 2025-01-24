from odoo import api, fields, models


class AccountMove(models.Model):
    """This class extends the base 'account.move' model to introduce a new
    field, 'is_exchange', which allows users to manually apply an exchange
    rate for a transaction. When this option is enabled, users can specify
    the exchange rate through the 'rate' field."""
    
    _inherit = 'account.move'

    is_exchange = fields.Boolean(
        string='Apply Manual Exchange',
        help='Check this box if you want to manually apply an exchange rate for this transaction.'
    )
    rate = fields.Float(
        string='Rate', 
        help='Specify the exchange rate.', 
        default=1
    )


class AccountMoveLine(models.Model):
    """Extends account.move.line to apply the manual exchange rate set in the journal entry."""
    
    _inherit = 'account.move.line'

    @api.onchange('amount_currency')
    def _onchange_amount_currency(self):
        """Automatically apply the manual exchange rate when amount_currency is changed."""
        if self.move_id.is_exchange and self.move_id.rate and self.currency_id and self.currency_id != self.company_id.currency_id:
            self.debit = self.amount_currency * self.move_id.rate if self.amount_currency > 0 else 0
            self.credit = abs(self.amount_currency * self.move_id.rate) if self.amount_currency < 0 else 0

    @api.onchange('currency_id')
    def _onchange_currency_id(self):
        """Recalculate the debit and credit when the currency is changed."""
        if self.move_id.is_exchange and self.move_id.rate and self.currency_id and self.currency_id != self.company_id.currency_id:
            self.debit = self.amount_currency * self.move_id.rate if self.amount_currency > 0 else 0
            self.credit = abs(self.amount_currency * self.move_id.rate) if self.amount_currency < 0 else 0
