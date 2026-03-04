const API = "http://127.0.0.1:8000";

const form = document.getElementById("loan-form");
const resultDiv = document.getElementById("result");
const plotBtn = document.getElementById("plot-btn");
const plotDiv = document.getElementById("plot");

form.addEventListener("submit", async (e) => {
    e.preventDefault();
    
    // Show loading
    const btn = form.querySelector("button");
    const originalText = btn.innerText;
    btn.innerText = "⏳ Predicting...";
    btn.disabled = true;
    resultDiv.innerHTML = "";

    try {
        const data = {
            Dependents: document.getElementById("dependents").value,
            Education: document.getElementById("education").value,
            Self_Employed: document.getElementById("self_employed").value,
            Credit_History: parseFloat(document.getElementById("credit_history").value),
            Property_Area: document.getElementById("property_area").value,
            Loan_Amount_Term: parseFloat(document.getElementById("loan_amount_term").value),
            ApplicantIncome: parseFloat(document.getElementById("applicant_income").value),
            CoapplicantIncome: parseFloat(document.getElementById("coapplicant_income").value),
            LoanAmount: parseFloat(document.getElementById("loan_amount").value)
        };

        const res = await fetch(`${API}/predict`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (!res.ok) throw new Error("Prediction failed");

        const result = await res.json();

        // Dynamic result styling based on prediction
        const isApproved = result.prediction === "Approved";
        resultDiv.innerHTML = `
            <div class="result-card ${isApproved ? 'approved' : 'rejected'}">
                <h2>${result.prediction}</h2>
                <p>Approval Probability: <strong>${result.probability}%</strong></p>
            </div>
        `;
    } catch (error) {
        resultDiv.innerHTML = `
            <div class="result-card error">
                <h2>❌ Error</h2>
                <p>Failed to predict: ${error.message}. Check if server is running.</p>
            </div>
        `;
    } finally {
        btn.innerText = originalText;
        btn.disabled = false;
    }
});

plotBtn.addEventListener("click", async () => {
    plotBtn.disabled = true;
    plotBtn.innerText = "⏳ Loading Plot...";
    plotDiv.innerHTML = "";

    try {
        const res = await fetch(`${API}/plot`);
        const data = await res.json();
        plotDiv.innerHTML = `<img src="data:image/png;base64,${data.image}" alt="Dataset Scatter Plot" class="plot-image">`;
    } catch (error) {
        plotDiv.innerHTML = `<p class="error">Failed to load plot: ${error.message}</p>`;
    } finally {
        plotBtn.disabled = false;
        plotBtn.innerText = "📊 View Dataset Visualization";
    }
});
