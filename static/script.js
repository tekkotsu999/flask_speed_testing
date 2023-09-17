// GETリクエストを送る関数
async function sendGetRequest() {
    const startTime = Date.now();
    const response = await fetch('/get_method');
    const data = await response.text();
    const endTime = Date.now();

    console.log(`GET Response: ${data}`);
    console.log(`GET took ${endTime - startTime} ms`);
}

// POSTリクエストを送る関数
async function sendPostRequest() {
    const startTime = Date.now();
    const response = await fetch('/post_method', {
        method: 'POST'
    });
    const data = await response.text();
    const endTime = Date.now();

    console.log(`POST Response: ${data}`);
    console.log(`POST took ${endTime - startTime} ms`);
}
