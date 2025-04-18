# 🏬 Warehouse Management System with Barcode Scanner

A simple inventory and stock management system for warehouses with barcode scanner integration using camera.

## 🚀 Features

- Add / update / delete products
- Scan barcode using device camera
- Inward / outward stock tracking
- Real-time inventory dashboard
- Export reports (Excel / PDF)
- Login for staff/admin

## 🛠 Tech Stack

- Python (Django)
- PostgreSQL / Supabase
- REST API
- React + Tailwind CSS
- Quagga.js or zxing (barcode scanner)

## 📷 Barcode Support

- Use webcam or phone camera to scan barcodes
- Auto-fetch and update stock records

## 🧰 How It Works

1. Login to dashboard
2. Scan item to stock in/out
3. Inventory auto-updates
4. Generate detailed reports on inventory and transactions.

## 🗂 Folder Structure
```
├── src/                
│   ├── app/            
│   │   ├── models/         # Database models for products, users, and transactions
│   │   ├── views/          # Logic for dashboard, authentication, and inventory
│   │   ├── templates/      # HTML templates for UI
│   │   └── static/         # CSS, JavaScript, and images
│   ├── api/                # REST API endpoints and serializers
│   └── utils/              # Barcode scanning, report generation, and helpers
├── docs/                   # User guide, API docs, and changelog
├── tests/                  # Unit and integration tests
├── requirements.txt        # Python dependencies
├── manage.py               # Django management script
└── README.md               # Project overview and instructions
```

## 🧪 Demo

_Coming soon!_

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

