import { useState } from "react";
import axios from "axios";
import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";
import "./Upload.css";

function Upload() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const file = e.target.files[0];

    if (!file) return;

    setImage(file);
    setPreview(URL.createObjectURL(file));
    setResult(null);
  };

  const uploadImage = async () => {
    if (!image) {
      alert("Please select an image");
      return;
    }

    const formData = new FormData();
    formData.append("file", image);

    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);
    } catch (error) {
      console.error(error);

      if (error.response) {
        alert(JSON.stringify(error.response.data));
      } else {
        alert(error.message);
      }
    }

    setLoading(false);
  };

  const copyDescription = () => {
    if (!result) return;

    navigator.clipboard.writeText(result.description);
    alert("Description copied successfully!");
  };

  const downloadJSON = () => {
    if (!result) return;

    const blob = new Blob(
      [JSON.stringify(result, null, 2)],
      {
        type: "application/json",
      }
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = "product_catalog.json";
    a.click();

    URL.revokeObjectURL(url);
  };

  const exportPDF = () => {
    if (!result) return;

    const doc = new jsPDF();

    doc.setFontSize(22);
    doc.setTextColor(37, 99, 235);
    doc.text("AI Product Catalog", 20, 20);

    doc.setFontSize(12);
    doc.setTextColor(100);
    doc.text("Generated using AI Product Catalog Generator", 20, 30);

    autoTable(doc, {
      startY: 40,

      head: [["Field", "Value"]],

      body: [
        ["Title", result.title],
        ["Category", result.category],
        ["Brand", result.brand],
        ["Color", result.color],
        ["Confidence", `${(result.confidence * 100).toFixed(2)} %`],
        ["Description", result.description],
        [
          "Keywords",
          Array.isArray(result.keywords)
            ? result.keywords.join(", ")
            : result.keywords,
        ],
        [
          "Tags",
          Array.isArray(result.tags)
            ? result.tags.join(", ")
            : result.tags,
        ],
      ],

      theme: "grid",

      headStyles: {
        fillColor: [37, 99, 235],
      },
    });

    doc.save("AI_Product_Catalog.pdf");
  };

  return (
    <div className="main-container">
      <div className="hero">
        <h1>🤖 AI Product Catalog Generator</h1>

        <p>
          Upload any product image and let AI generate product details
          automatically.
        </p>
      </div>

      <div className="upload-card">
        <input type="file" onChange={handleChange} />

        {preview && (
          <img
            src={preview}
            alt="Preview"
            className="preview-image"
          />
        )}

        <button onClick={uploadImage}>
          Analyze Product
        </button>

        {loading && (
          <div className="loading">
            <div className="spinner"></div>

            <p>AI is analyzing your product...</p>
          </div>
        )}
      </div>

      {result && (
        <div className="result-card">
          <h2>📦 Product Details</h2>

          <div className="row">
            <strong>Title</strong>
            <span>{result.title}</span>
          </div>

          <div className="row">
            <strong>Category</strong>
            <span>{result.category}</span>
          </div>

          <div className="row">
            <strong>Brand</strong>
            <span>{result.brand}</span>
          </div>

          <div className="row">
            <strong>Color</strong>
            <span>{result.color}</span>
          </div>

          <div className="row">
            <strong>Confidence</strong>

            <div className="confidence-box">
              <div className="progress">
                <div
                  className="progress-fill"
                  style={{
                    width: `${result.confidence * 100}%`,
                  }}
                ></div>
              </div>

              <span className="confidence-text">
                {(result.confidence * 100).toFixed(1)}%
              </span>
            </div>
          </div>

          <div className="row">
            <strong>Description</strong>

            <span>{result.description}</span>
          </div>

          <div className="row">
            <strong>Keywords</strong>

            <span>
              {Array.isArray(result.keywords)
                ? result.keywords.join(", ")
                : result.keywords}
            </span>
          </div>

          <div className="row">
            <strong>Tags</strong>

            <span>
              {Array.isArray(result.tags)
                ? result.tags.join(", ")
                : result.tags}
            </span>
          </div>

          <div className="button-group">
            <button onClick={copyDescription}>
              📋 Copy Description
            </button>

            <button onClick={downloadJSON}>
              📥 Download JSON
            </button>

            <button onClick={exportPDF}>
              📄 Export PDF
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Upload;