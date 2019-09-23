# odoo_custom_bank_import v11<br/>
odoo11 Add a custom Seach for origin number of a invoice<br/>

Add a custom search for bank.statement.line validation<br/>

<strong>Inherit bank.import.statement model to match bank.statement with the invoice.origin field.</strong>
<br/>
The Custom Bank import searches within the Bank import line for numbers that have 9 digits.

If successful, the system searches for invoices that have an identical number in the account.invoice.origin field. 

If successful, the linked partner is returned.


<strong>Caution: This Model is needs the account_bank_statement_import</strong>

 
