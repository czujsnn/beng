function createPod() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/create', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    
    xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr)
        console.log(xhr.responseText)
        var response = JSON.parse(xhr.responseText);
        var ip = response.ip;
        document.getElementById('response').innerHTML = 'POD IP: ' + ip;
    }
    };
    xhr.send();
}

function deletePod() {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/delete', true);
    xhr.setRequestHeader('Content-Type', 'application/json');

    xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr)
        console.log(xhr.responseText)
        var response = JSON.parse(xhr.responseText);
        var status = response.
        document.getElementById('response').innerHTML = 'Response from /delete' + response;
    }
    };
    xhr.send();
}
