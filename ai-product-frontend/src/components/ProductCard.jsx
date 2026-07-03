function ProductCard({ preview, result }) {
  return (
    <div className="product-card">

      <div className="product-image">

        <img
          src={preview}
          alt="Product"
        />

      </div>

      <div className="product-details">

        <h2>{result.title}</h2>

        <div className="detail-row">
          <strong>Category</strong>
          <span>{result.category}</span>
        </div>

        <div className="detail-row">
          <strong>Brand</strong>
          <span>{result.brand}</span>
        </div>

        <div className="detail-row">
          <strong>Color</strong>
          <span>{result.color}</span>
        </div>

        <div className="detail-row">

          <strong>Confidence</strong>

          <div className="confidence-container">

            <div className="progress-bar">

              <div
                className="progress-fill"
                style={{
                  width: `${result.confidence * 100}%`
                }}
              ></div>

            </div>

            <span>

              {(result.confidence * 100).toFixed(1)}%

            </span>

          </div>

        </div>

        <div className="detail-row">
          <strong>Description</strong>
          <span>{result.description}</span>
        </div>

        <div className="detail-row">

          <strong>Keywords</strong>

          <div className="badge-container">

            {result.keywords.map((keyword, index) => (

              <span
                key={index}
                className="badge"
              >
                {keyword}
              </span>

            ))}

          </div>

        </div>

        <div className="detail-row">

          <strong>Tags</strong>

          <div className="badge-container">

            {result.tags.map((tag, index) => (

              <span
                key={index}
                className="badge tag"
              >
                {tag}
              </span>

            ))}

          </div>

        </div>

      </div>

    </div>
  );
}

export default ProductCard;