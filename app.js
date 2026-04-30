const modules = [
  { id: 1, name: "Introduction", desc: "Welcome to APL and get started", progress: 100, gradient: "linear-gradient(135deg, #1a1a2e 0%, #2d2d44 100%)", label: "INTRO", status: "done" },
  { id: 2, name: "Prompt Masterclass", desc: "Master the anatomy of a perfect AI prompt", progress: 33, gradient: "linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)", label: "MASTERCLASS", status: "new" },
  { id: 3, name: "Dream Vault", desc: "Every scene you've dreamed of, in your camera roll", progress: 0, gradient: "linear-gradient(135deg, #2c1810 0%, #4a2c1a 100%)", label: "DREAM VAULT", status: null },
  { id: 4, name: "Her Aesthetic Era", desc: "Your vibe, your way — pick it and run with it", progress: 0, gradient: "linear-gradient(135deg, #1a0a2e 0%, #3d1a6e 100%)", label: "AESTHETIC ERA", status: null },
  { id: 5, name: "Boss Babe", desc: "CEO energy, money moves, rich girl prompts only", progress: 0, gradient: "linear-gradient(135deg, #1c1200 0%, #3d2c00 100%)", label: "BOSS BABE", status: null },
  { id: 6, name: "Dark & Dangerous", desc: "Moody, mysterious, magnetic vibes", progress: 0, gradient: "linear-gradient(135deg, #0a0a0a 0%, #1a0a0a 100%)", label: "DARK & DANGEROUS", status: null },
  { id: 7, name: "Daily Prompts", desc: "Fresh drops every day — never run out of content", progress: 0, gradient: "linear-gradient(135deg, #0a1a0a 0%, #1a3a1a 100%)", label: "DAILY DROPS", status: null },
  { id: 8, name: "Edit Like a Pro", desc: "Free tools that make your images look magazine-worthy", progress: 0, gradient: "linear-gradient(135deg, #0a0a1a 0%, #1a1a3a 100%)", label: "EDIT PRO", status: null },
  { id: 9, name: "AI Video Era", desc: "Turn AI images into scroll-stopping videos", progress: 0, gradient: "linear-gradient(135deg, #1a0a1a 0%, #3a1a3a 100%)", label: "AI VIDEO", status: null },
  { id: 10, name: "UGC Lab", desc: "What brands actually buy — and how to give it to them", progress: 0, gradient: "linear-gradient(135deg, #0a1a1a 0%, #1a3a3a 100%)", label: "UGC LAB", status: null },
  { id: 11, name: "Collab", desc: "How to land brand deals using your AI content", progress: 0, gradient: "linear-gradient(135deg, #1a1a0a 0%, #3a3a1a 100%)", label: "COLLAB", status: null },
  { id: 12, name: "Affiliates", desc: "Get paid to create — the affiliate playbook", progress: 0, gradient: "linear-gradient(135deg, #0a1a0a 0%, #2a3a0a 100%)", label: "AFFILIATES", status: null },
  { id: 13, name: "Monetize Your AI", desc: "Etsy, brand deals, selling prompts — turn content into cash", progress: 0, gradient: "linear-gradient(135deg, #1a0a00 0%, #4a2000 100%)", label: "MONETIZE", status: "new" },
];

function renderModules(filter = "all") {
  const grid = document.getElementById("modulesGrid");
  const filtered = modules.filter((m) => {
    if (filter === "all") return true;
    if (filter === "in-progress") return m.progress > 0 && m.progress < 100;
    if (filter === "completed") return m.progress === 100;
    if (filter === "new") return m.status === "new";
    return true;
  });

  grid.innerHTML = filtered.map((m) => `
    <div class="module-card" onclick="openModule(${m.id})">
      ${m.status === "new" ? '<span class="module-badge badge-new">New</span>' : ""}
      ${m.status === "done" ? '<span class="module-badge badge-done">✓ Done</span>' : ""}
      <div class="module-thumb" style="background: ${m.gradient}">
        <span class="module-thumb-label">${m.label}</span>
      </div>
      <div class="module-body">
        <div class="module-name">${m.name}</div>
        <div class="module-desc">${m.desc}</div>
        <div class="module-footer">
          <div class="module-progress-bar"><div class="module-progress-fill" style="width: ${m.progress}%"></div></div>
          <span class="module-pct">${m.progress}%</span>
        </div>
      </div>
    </div>
  `).join("");
}

function openModule(id) {
  const m = modules.find((x) => x.id === id);
  if (m) console.log("Opening:", m.name);
}

document.querySelectorAll(".filter-tab").forEach((tab) => {
  tab.addEventListener("click", function () {
    document.querySelectorAll(".filter-tab").forEach((t) => t.classList.remove("active"));
    this.classList.add("active");
    const map = { All: "all", "In Progress": "in-progress", Completed: "completed", New: "new" };
    renderModules(map[this.textContent] || "all");
  });
});

function updateCountdown() {
  const now = new Date();
  const midnight = new Date();
  midnight.setHours(24, 0, 0, 0);
  const diff = midnight - now;
  const h = String(Math.floor(diff / 3600000)).padStart(2, "0");
  const m = String(Math.floor((diff % 3600000) / 60000)).padStart(2, "0");
  const s = String(Math.floor((diff % 60000) / 1000)).padStart(2, "0");
  const el = document.getElementById("countdown");
  if (el) el.textContent = `${h}:${m}:${s}`;
}

setInterval(updateCountdown, 1000);
updateCountdown();
renderModules();