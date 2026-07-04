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
          "Content-Type": "multipart/form-data"
        }
      }
    );

    setResult(response.data);

  } catch (err) {

    console.error(err);
    alert("Upload Failed");

  }

  setLoading(false);

};