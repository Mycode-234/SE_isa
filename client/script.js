async function classify() {
    let inputValue = document.getElementById("userInput").value;
    let response = await fetch("https://your-vercel-backend.vercel.app/classify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: inputValue })
    });
    let data = await response.json();
    document.getElementById("result").innerText = "Prediction: " + data.prediction;
}
