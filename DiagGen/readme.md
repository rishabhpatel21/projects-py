# 📊 Code-to-Diagram Converter

A powerful developer tool that converts Python or JavaScript code into clear, visually appealing diagrams using Mermaid.js.

## 🚀 Key Features

- **File Support**: Upload `.py` or `.js` files.
- **Diagram Types**:
    - Function flowcharts
    - Class diagrams
- **Interactive Options**:
    - View diagrams in your browser
    - Export as image or PDF

## 🛠 Technology Stack

- **Backend**: Python (AST module), FastAPI or Flask
- **Frontend**: React (optional)
- **Visualization**: Mermaid.js

## 🎯 Ideal Use Cases

- **For Developers**: Simplify code reviews and debugging.
- **For Students**: Learn and understand code structure visually.
- **For Teams**: Enhance collaboration and communication during discussions.

## 🧰 How It Works

1. **Upload Code**: Drag and drop your `.py` or `.js` file.
2. **Code Parsing**: Backend processes the code using Python's AST module.
3. **Diagram Generation**: Mermaid.js creates the visual representation.
4. **Output**: View and download the diagram.

## 🗂 Project Structure

```
code-to-diagram/
├── backend/
│   ├── parser.py        # Handles code parsing logic
│   ├── routes.py        # Defines API endpoints
├── frontend/
│   ├── components/
│   │   ├── Viewer.jsx   # Displays generated diagrams
│   │   ├── UploadForm.jsx # Handles file uploads
│   └── App.jsx          # Main React application entry point
└── README.md            # Project documentation
```

## 🧪 Demo

_Coming soon!_

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.