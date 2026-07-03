import { useDropzone } from "react-dropzone";

function UploadBox({

  setImage,
  setPreview,
  setResult,
  preview

}) {

  const onDrop = (acceptedFiles) => {

    const file = acceptedFiles[0];

    if (!file) return;

    setImage(file);

    setPreview(URL.createObjectURL(file));

    setResult(null);

  };

  const {

    getRootProps,

    getInputProps,

    isDragActive

  } = useDropzone({

    onDrop,

    accept: {

      "image/*": []

    },

    multiple: false

  });

  return (

    <div
      {...getRootProps()}
      className="upload-box"
    >

      <input {...getInputProps()} />

      {preview ? (

        <img
          src={preview}
          alt="Preview"
          className="preview-image"
        />

      ) : (

        <>

          <div className="upload-icon">

            📤

          </div>

          <h2>

            Upload Product Image

          </h2>

          <p>

            {isDragActive

              ? "Drop your image here..."

              : "Drag & Drop your image here"}

          </p>

          <small>

            or click to browse

          </small>

        </>

      )}

    </div>

  );

}

export default UploadBox;