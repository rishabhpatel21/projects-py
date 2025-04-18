# 🧾 Automated PDF & Invoice Parser

A smart tool to automatically extract data from invoices and PDF bills for small businesses. No more manual data entry!

## 🚀 Features

- Upload PDF invoices
- Extract key fields: invoice number, date, item list, price, total, etc.
- Save data to database (Supabase or MongoDB)
- Export as Excel file
- REST API support for bulk parsing

## 🛠 Tech Stack

- Python
- PyMuPDF / pdfplumber
- Tesseract OCR (for scanned PDFs)
- FastAPI
- Supabase / MongoDB
- React (optional frontend)

## 🧰 How It Works

1. Upload PDF via frontend or API.
2. Backend extracts and processes data.
3. Data saved in DB and/or exported.
4. Dashboard shows parsed invoices.

## 🗂 Folder Structure

```
invoice-parser/
├── backend/
│   ├── main.py          # Entry point for FastAPI backend
│   ├── extract.py       # Logic for extracting data from PDFs
│   ├── models.py        # Database models and schema
│   └── requirements.txt # Backend dependencies
├── samples/
│   └── demo-invoices/   # Sample PDF invoices for testing
├── frontend/            # Optional React frontend
│   ├── src/
│   └── package.json     # Frontend dependencies
├── tests/
│   ├── test_extract.py  # Unit tests for extraction logic
│   └── test_api.py      # Unit tests for API endpoints
└── README.md            # Project documentation
```

or a simplified version:

```
invoice-parser/
├── backend/
│   ├── main.py          # FastAPI backend entry point
│   ├── extract.py       # PDF data extraction logic
│   └── models.py        # Database schema
├── samples/
│   └── demo-invoices/   # Test PDF invoices
└── README.md            # Documentation
```

## 🧪 Demo

_Coming soon!_

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.