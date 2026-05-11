# Invoice Extract Prompt

Extract structured invoice fields from the text below.

Return JSON only:

```json
{
  "document_type": "invoice | credit_note | receipt | statement | quote | unknown",
  "supplier_name": "",
  "supplier_tax_id": "",
  "invoice_number": "",
  "invoice_date": "",
  "due_date": "",
  "currency": "",
  "tax_base": null,
  "tax_amount": null,
  "total_amount": null,
  "payment_terms": "",
  "category_guess": "",
  "confidence": "high | medium | low",
  "anomalies": []
}
```

Rules:

- Do not infer missing amounts.
- If totals conflict, set confidence low and list anomaly.
- Preserve original currency.
- Mark scanned/garbled text as low confidence.

