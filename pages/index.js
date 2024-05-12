// Function to recieve JSON files
async function fetchData(path) {
  const response = await fetch(path);
  const data = await response.json();
  return data;
}

// Function to generate Hymns
async function generateHymns(path, number) {
  // Grab Templates
  const hymnTemplate = document.querySelector("#hymn-template");
  const hymns = document.querySelector("#hymns");

  // Gets book data
  await fetchData(path).then((book) => {
    // For each hymn in book
    let verseCount = 0;
    for (const hymnData in book) {
      // Clone hymn and get all relevant elements to do with that hymn
      let hymn = document.importNode(hymnTemplate.content, true);
      hymn = hymn.querySelector(".hymn");
      let hymnHeading = hymn.querySelector(".hymn-heading");

      // Set the heading to the hymn number: Book 1, Hymn ()
      hymnHeading.textContent = `Book ${number}, Hymn ${hymnData}`;

      // For each verse in a hymn duplicate the paragraph elements
      for (let i = 0; i < book[hymnData].length; i++) {
        verseCount++;
        let hymnVerse = hymn.querySelector(".hymn-verse").cloneNode(true);
        let firstPart = hymnVerse.querySelector(".first-line");
        let secondPart = hymnVerse.querySelector(".second-line");
        firstPart.textContent = book[hymnData][i][0];
        secondPart.textContent = book[hymnData][i][1];
        hymnVerse.setAttribute("data-verse", verseCount);
        hymnVerse.setAttribute("data-book", number);
        hymn.appendChild(hymnVerse);
      }
      // Remove template
      hymn.removeChild(hymn.children[1]);

      // Add it to hymns
      hymns.appendChild(hymn);
    }
  });
}

document.addEventListener("DOMContentLoaded", async function () {
  const book = document.title.split(" ")[document.title.split(" ").length - 1];
  await generateHymns(`books/filtered_book${book}.json`, book);

  const verses = document.querySelectorAll(".hymn-verse");
  verses.forEach((verse) => {
    verse.addEventListener("click", () => {
      let verseData = {
        id: verse.getAttribute("data-verse"),
        book: verse.getAttribute("data-book"),
      };
      let bookMarks =
        JSON.parse(localStorage.getItem("bookmarks")) === null
          ? []
          : JSON.parse(localStorage.getItem("bookmarks"));
      bookMarks.push(verseData);
      localStorage.setItem("bookmarks", JSON.stringify(bookMarks));
      console.log(localStorage.getItem("bookmarks"));
    });
  });
});
