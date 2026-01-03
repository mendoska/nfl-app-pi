<script>
  // Load saved theme on page load
  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    document.body.classList.add("dark");
  }

  const btn = document.getElementById("themeToggle");

  btn.addEventListener("click", () => {
    // toggle first
    document.body.classList.toggle("dark");

    // then save new state
    localStorage.setItem(
      "theme",
      document.body.classList.contains("dark") ? "dark" : "light"
    );
  });
</script>