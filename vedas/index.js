// Function to recieve JSON files
async function fetchData(path) {
  const response = await fetch(path);
  const data = await response.json();
  return data;
}

// Function to generate Hymns
async function generateHymns(path) {
  // Grab Templates
  const hymnTemplate = document.querySelector("#hymn-template");
  const hymns = document.querySelector("#hymns");

  // Gets book data
  await fetchData(path).then((book) => {
    // For each hymn in book
    for (const hymnData in book) {
      // Clone hymn and get all relevant elements to do with that hymn
      let hymn = document.importNode(hymnTemplate.content, true);
      hymn = hymn.querySelector(".hymn");
      let hymnHeading = hymn.querySelector(".hymn-heading");

      // Set the heading to the hymn number: Book 1, Hymn ()
      hymnHeading.textContent = `Book 1, Hymn ${hymnData}`;

      // For each verse in a hymn duplicate the paragraph elements
      for (let i = 0; i < book[hymnData].length; i++) {
        let hymnVerse = hymn.querySelector(".hymn-verse").cloneNode(true);
        let firstPart = hymnVerse.querySelector(".first-line");
        let secondPart = hymnVerse.querySelector(".second-line");
        firstPart.textContent = book[hymnData][i][0];
        secondPart.textContent = book[hymnData][i][1];
        hymn.appendChild(hymnVerse);
      }
      // Remove template
      hymn.removeChild(hymn.children[1]);

      // Add it to hymns
      hymns.appendChild(hymn);
    }
  });
}

document.addEventListener("DOMContentLoaded", function () {
  generateHymns("books/filtered_book1.json");
});
