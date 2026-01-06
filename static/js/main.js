console.log("hell there")

  function showForm() {
    document.getElementById("trialForm").classList.remove("hidden");
  }

  function submitForm(event) {
    event.preventDefault();
    document.getElementById("trialForm").classList.add("hidden");
    document.getElementById("successMessage").classList.remove("hidden");
  }
