$(document).ready(()=>{

    $('#sendData').click(function(){

    // Storing the URL
    var imgData = $('#urlText').val();

    //Sending AJAX CALL
    $.ajax({
      "async": true,
      "crossDomain": true,
      "url": "http://localhost:5000/api/v0.1/inference",
      "method": "POST",
      "headers": {
        "content-type": "application/json",
        "cache-control": "no-cache"
      },
      "processData": false,
      "data": JSON.stringify(
        {"path":imgData.toString()}
      ),
      "success": function(data) {
        // DISPLAYING THE RESULT
        document.getElementById('result').innerHTML = data['prediction'];
      }
      });
    });
});
