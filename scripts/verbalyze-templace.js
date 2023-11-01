var isRecording = false;
var recordButton = document.getElementById("recordButton");
var summaryContainer = document.getElementById("summaryContainer");
recordButton.addEventListener("click", function() {
    isRecording = !isRecording;
    recordButton.textContent = isRecording ? "STOP RECORDING" : "START RECORDING";
    if (isRecording) {
        var existingSummarizeButton = document.getElementById("summarizeButton");
        if (existingSummarizeButton) {
            summaryContainer.removeChild(existingSummarizeButton);
        }
        var notepad = document.getElementById('textArea');
        window.addEventListener('click', function() {
            notepad.focus();
        });
    } 
    else {
        var summarizeButton = document.createElement("button");
        summarizeButton.id = "summarizeButton";
        summarizeButton.className = "center";
        summarizeButton.textContent = "SUMMARIZE";
        summarizeButton.addEventListener("click", function() {
            const text = textArea.value;
            console.log("Text sent for summarization:", text);
        window.location.href = "/download"});
        summaryContainer.appendChild(summarizeButton);
    }})