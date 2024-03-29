# -*- coding: utf-8 -*-
from logging import Logger

from odoo import models, fields, api
import logging
from io import BytesIO
import zipfile
import base64
import re

_logger = logging.getLogger(__name__)



class AccountBankStatementImport(models.TransientModel):
    """Add process_camt method to account.bank.statement.import."""
    _inherit = 'account.bank.statement.import'




    @api.model
    def _complete_stmts_vals(self, stmt_vals, journal_id, account_number):
        """Match partner_id if hasn't been deducted yet."""
        res = super(AccountBankStatementImport, self)._complete_stmts_vals(
            stmt_vals, journal_id, account_number,
        )
        # Since QIF doesn't provide account numbers (normal behaviour is to
        # provide 'account_number', which the generic module uses to find
        # the partner), we have to find res.partner through the name

        param_obj = self.env['ir.config_parameter']
        min_range = param_obj.env['ir.config_parameter'].search(
            [('key', '=', 'custom_bank_import_min_range')])

        max_range = param_obj.env['ir.config_parameter'].search(
            [('key', '=', 'custom_bank_import_max_range')])
        try:
            min_range = min_range[0]['value']
            max_range = max_range[0]['value']
        except IndexError as e:
            _logger.error(e)
        _logger.info(min_range)
        _logger.info(max_range)
        account_obj = self.env['account.invoice']
        for statement in res:
            for line_vals in statement['transactions']:
                if not line_vals.get('partner_id') and line_vals.get('name'):
                    if line_vals.get('note'):
                        note = line_vals['note']
                        _logger.info('test')
                        _logger.info(max_range)
                        note_numbers_list = [str(s) for s in note.split() if s.isdigit() and (len(s) >= int(min_range) and len(s) <= int(max_range))]
                        _logger.info(note_numbers_list)
                        if note_numbers_list:
                            account_invoice = account_obj.search(
                                [('origin', '=', note_numbers_list[0])], limit=1,
                            )
                            if account_invoice:
                                line_vals['partner_id'] = account_invoice['partner_id'].id
                                line_vals['note'] = note_numbers_list[0]
                                line_vals['ref'] = note_numbers_list[0]
                        else:
                            note_numbers = re.findall(r'\d+', note)
                            _logger.info(note_numbers_list)
                            note_numbers_list = [str(s) for s in note_numbers if s.isdigit() and (len(s) >= int(min_range) and len(s) <= int(max_range))]
                            if note_numbers_list:
                                account_invoice = account_obj.search(
                                    [('origin', '=', note_numbers_list[0])], limit=1,
                                )

                                if account_invoice:
                                    line_vals['partner_id'] = account_invoice['partner_id'].id
                                    line_vals['note'] = note_numbers_list[0]
                                    line_vals['ref'] = note_numbers_list[0]
        return res
