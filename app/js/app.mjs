'use strict';

function init() {

  // décodage de l'image
  document.getElementById('decode-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    let formData = new FormData();
    formData.append('img', img.files[0]);
    await fetch('/cgi-bin/decode.py', {
      method: "POST",
      body: formData
    }).then((response) => {
      response.text().then((text) => {
        document.getElementById('results_wrapper').style.display = 'block';
        document.getElementById('results').innerText = text;
      });
    });
  });

  // encodage du contenu
  document.getElementById('encode-form').addEventListener('submit', async function (e) {
    e.preventDefault();
    let formData = new FormData();
    formData.append('content', content.value);
    await fetch('/cgi-bin/encode.py', {
      method: "POST",
      body: formData
    }).then((response) => {
      response.text().then((data) => {
        document.getElementById('results_wrapper').style.display = 'block';
        document.getElementById('results').innerHTML = data;
      });
    });
  });

}

export {init};
