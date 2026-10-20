function RunSentimentAnalysis() {
    const text = document.getElementById("textToAnalyze").value;
    const request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState === 4) {
            document.getElementById("system_response").textContent =
                this.status === 200 ? this.responseText : "Request failed.";
        }
    };
    request.open("GET", "/emotionDetector?textToAnalyze=" + encodeURIComponent(text), true);
    request.send();
}
