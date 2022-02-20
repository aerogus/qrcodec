'use strict';

function init() {
  console.log('init');

  document.getElementById('passform').addEventListener('submit', async function (e) {
    e.preventDefault();
    console.log('submit');
    let formData = new FormData();
    formData.append('pass', pass.files[0]);
    await fetch('/cgi-bin/upload.py', {
      method: "POST",
      body: formData
    }).then((response) => {
      response.text().then((text) => {
        document.getElementById('results_wrapper').style.display = 'block';
        document.getElementById('results').innerText = text;
      });
    });
  });
}

export {init};
