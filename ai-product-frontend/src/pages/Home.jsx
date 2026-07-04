import { useState } from "react";
import axios from "axios";

import UploadBox from "../components/UploadBox";
import ProductCard from "../components/ProductCard";
import PredictionTable from "../components/PredictionTable";
import ActionButtons from "../components/ActionButtons";
import LoadingSpinner from "../components/LoadingSpinner";

import "../styles/Home.css";

function Home() {
  const [image, setImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

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
        "https://grithesh1-ai-product-catalog.hf.space/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Upload Failed");
    }

    setLoading(false);
  };

  return (
    <div className="container">
      <h1>🤖 AI Product Catalog Generator</h1>

      <p className="subtitle">
        Upload any product image and AI will generate complete catalog
        information.
      </p>

      <UploadBox
        setImage={setImage}
        setPreview={setPreview}
        setResult={setResult}
        preview={preview}
      />

      <button className="analyze-btn" onClick={uploadImage}>
        Analyze Product
      </button>

      {loading && <LoadingSpinner />}

      {result && (
        <>
          <ProductCard preview={preview} result={result} />
          <PredictionTable predictions={result.top_predictions} />
          <ActionButtons result={result} />
        </>
      )}
    </div>
  );
}

export default Home;