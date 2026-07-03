function PredictionTable({ predictions }) {

  if (!predictions || predictions.length === 0) {
    return null;
  }

  return (

    <div className="prediction-card">

      <h2>🏆 Top AI Predictions</h2>

      <table className="prediction-table">

        <thead>

          <tr>

            <th>Rank</th>
            <th>Category</th>
            <th>Confidence</th>

          </tr>

        </thead>

        <tbody>

          {predictions.map((item, index) => (

            <tr key={index}>

              <td>

                {index === 0
                  ? "🥇"
                  : index === 1
                  ? "🥈"
                  : index === 2
                  ? "🥉"
                  : `#${index + 1}`}

              </td>

              <td>{item.category}</td>

              <td>

                {(item.confidence * 100).toFixed(2)}%

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>

  );

}

export default PredictionTable;