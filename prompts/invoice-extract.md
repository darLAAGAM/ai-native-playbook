---
prompt: invoice-extract
domain: finance
---

# Invoice Extract Prompt

```text
Extract structured invoice fields from the text below. Return JSON only.

Text:
{{invoice_text}}

Schema:
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

Rules:
- Do not infer missing amounts.
- Preserve original currency.
- Mark scanned or garbled text as low confidence.
- List conflicting totals as anomalies.
```
