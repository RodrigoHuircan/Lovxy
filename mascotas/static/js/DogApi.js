const headers = new Headers({
  "Content-Type": "application/json",
  "x-api-key":
    "live_M9rln2JhUDPEC49u30oujUPAwgxhx4KO1r3sbWRcMpvDC6v5dc2H86yT8R27hvnl",
});

// document.addEventListener("DOMContentLoaded", function () {
//   const spinner = document.getElementById("spinner");
//   console.log(spinner); // Depuración: Verifica si el spinner se encuentra
// });

let requestOptions = {
  method: "GET",
  headers: headers,
  redirect: "follow",
};

fetch(
  "https://api.thedogapi.com/v1/images/search?limit=50&has_breeds=1",
  requestOptions
)
  .then((response) => {
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((result) => {
    mostrarData(result);
    document
      .getElementById("spinner")
      .setAttribute("style", "display: none !important;");
  })
  .catch((error) => {
    console.log("error", error);
    document
      .getElementById("spinner")
      .setAttribute("style", "display: none !important;");
  });

const mostrarData = (result) => {
  console.log(result);
  let body = "";
  for (let i = 0; i < result.length; i++) {
    const breedName =
      result[i].breeds && result[i].breeds.length > 0
        ? result[i].breeds[0].name
        : "Nombre no disponible";
    const imageUrl = result[i].url;
    body += `<tr><td class="text-center align-middle" id="TextApi">${breedName}</td>
            <td class="text-center align-middle"><img src="${imageUrl}" alt="Imagen de ${breedName}" style="max-width:300px; height:auto;"> </td></tr>`;
  }
  document.getElementById("data").innerHTML = body;
};
