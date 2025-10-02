document.addEventListener("DOMContentLoaded", async () => {
  const r = await fetch("/api/ping/");
  const data = await r.json();
  console.log("Ping:", data);
});
