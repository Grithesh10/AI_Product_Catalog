import jsPDF from "jspdf";
import autoTable from "jspdf-autotable";

function ActionButtons({ result }) {

  const copyDescription = () => {

    navigator.clipboard.writeText(result.description);

    alert("Description copied successfully!");

  };

  const downloadJSON = () => {

    const blob = new Blob(
      [JSON.stringify(result, null, 2)],
      {
        type: "application/json"
      }
    );

    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;

    a.download = "product_catalog.json";

    a.click();

    window.URL.revokeObjectURL(url);

  };

  const exportPDF = () => {

    const doc = new jsPDF();

    doc.setFontSize(22);
    doc.setTextColor(37, 99, 235);

    doc.text("AI Product Catalog", 20, 20);

    doc.setFontSize(12);
    doc.setTextColor(120);

    doc.text(
      "Generated using AI Product Catalog Generator",
      20,
      30
    );

    autoTable(doc, {

      startY: 40,

      head: [["Field", "Value"]],

      body: [

        ["Title", result.title],

        ["Category", result.category],

        ["Brand", result.brand],

        ["Color", result.color],

        [
          "Confidence",
          `${(result.confidence * 100).toFixed(2)}%`
        ],

        [
          "Description",
          result.description
        ],

        [
          "Keywords",
          result.keywords.join(", ")
        ],

        [
          "Tags",
          result.tags.join(", ")
        ]

      ],

      theme: "grid",

      headStyles: {

        fillColor: [37, 99, 235]

      }

    });

    doc.save("AI_Product_Catalog.pdf");

  };

  return (

    <div className="action-buttons">

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

  );

}

export default ActionButtons;