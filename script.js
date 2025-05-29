document.getElementById("addPlantForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const form = new FormData();
  form.append("name", document.getElementById("plantName").value);
  form.append("plant_type", document.getElementById("plantType").value);
  form.append("planted_date", document.getElementById("plantDate").value);
  form.append("notes", document.getElementById("plantNotes").value);

  const imageFile = document.getElementById("plantImage").files[0];
  if (imageFile) {
    form.append("image", imageFile);
  }

  try {
    const response = await fetch("http://127.0.0.1:8000/plants/", {
      method: "POST",
      body: form,
    });

    const result = await response.json();
    console.log("Plant added:", result);
    alert("Plant added successfully!");
  } catch (error) {
    console.error("Error adding plant:", error);
    alert("Something went wrong.");
  }
});
