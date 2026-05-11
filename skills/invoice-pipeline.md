# Skill: Invoice Pipeline

## Trigger

Run when finance/admin inboxes contain supplier invoice emails or when backfilling invoice history.

## Inputs

- Inbox or label
- Date range
- Drive destination folder
- Review sheet

## Procedure

1. Find emails with PDF attachments.
2. Extract PDF text.
3. Classify document type: invoice, credit note, receipt, statement, quote, unknown.
4. Extract supplier, tax ID, invoice number, invoice date, due date, currency, base, tax, total.
5. Store original PDF in Drive with predictable filename.
6. Append review row with confidence, Drive link, and source email.
7. Escalate scanned PDFs, low confidence, duplicates, and multi-currency anomalies.

## Guardrails

- Do not auto-pay.
- Do not post to accounting without human approval.
- Store original evidence.
- Keep confidence and source link on every row.

