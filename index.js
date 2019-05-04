$(document).ready(()=>{

    $('#sendData').click(function(){

    // Storing the URL
    // var imgData = $('#urlText').val();
    var fileSelect = document.getElementById('file-select');
    var files = fileSelect.files;
    console.log(files);
    // console.log(files);

    var form = new FormData();
    for (const file of files) {
      form.append('file', file);
    }
    // form.append("file", "780.png");
    console.log(form);
    // Loop through each of the selected files.

    // console.log(formData);
    //Sending AJAX CALL
    $.ajax({
      "async": true,
      "crossDomain": true,
      "url": "http://localhost:5000/api/v0.1/inference",
      "method": "POST",
      "headers": {
        "cache-control": "no-cache",
        "postman-token": "91a0d5be-9674-4788-6682-93a0ae049d3d"
      },
      "processData": false,
      "contentType": false,
      "mimeType": "multipart/form-data",
      "data": form,
      "success": function(data) {
        // DISPLAYING THE RESULT
        data = JSON.parse(data);
        console.log(data);
        console.log(data["prediction"])
        document.getElementById('result').innerHTML = data["prediction"];
      }
      });
    });
});
