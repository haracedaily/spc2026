const people = [
"조윤","권태현",
"조은결","김성훈","허현정","유지산",
"이준우","김민정","진미경","김민정",
"최준호","박지수","박상우","이종희","심정호",
"이서우","박윤빈","조용민","김윤선","이태경",
"황동건","원가희","김선희","박초롱","채란",
"이상욱","신혜진","한은태","박준하","이민지"
];

let mode = null;
let dragged = null;

/* 👥 사람 생성 */
function renderPool() {
  const pool = document.getElementById("pool");
  pool.innerHTML = "";

  people.forEach(p => {
    const div = document.createElement("div");
    div.className = `person ${p.gender}`;
    div.draggable = true;
    div.textContent = `${p.name} (${p.skill})`;

    div.addEventListener("dragstart", () => dragged = div);

    pool.appendChild(div);
  });
}

/* 🪑 드롭 */
document.querySelectorAll(".seat").forEach(seat => {
  seat.addEventListener("dragover", e => e.preventDefault());

  seat.addEventListener("drop", () => {
    if (!dragged) return;

    if (seat.firstChild) {
      // swap
      let temp = seat.firstChild;
      seat.appendChild(dragged);
      document.getElementById("pool").appendChild(temp);
    } else {
      seat.appendChild(dragged);
    }
  });
});

/* 🎲 랜덤 */
function shuffleSeats() {
  const seats = Array.from(document.querySelectorAll(".seat"));
  const assigned = seats.map(s => s.firstChild).filter(Boolean);

  for (let i = assigned.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [assigned[i], assigned[j]] = [assigned[j], assigned[i]];
  }

  seats.forEach((seat, i) => {
    seat.innerHTML = "";
    if (assigned[i]) seat.appendChild(assigned[i]);
  });
}

/* 🔄 교환모드 */
function enableSwapMode() {
  mode = "swap";
  let first = null;

  document.querySelectorAll(".seat").forEach(seat => {
    seat.onclick = () => {
      if (!seat.firstChild) return;

      if (!first) {
        first = seat;
        seat.style.outline = "2px solid red";
      } else {
        let temp = seat.innerHTML;
        seat.innerHTML = first.innerHTML;
        first.innerHTML = temp;
        first.style.outline = "";
        first = null;
      }
    };
  });
}

/* 🧹 초기화 */
function resetSeats() {
  const pool = document.getElementById("pool");

  document.querySelectorAll(".seat").forEach(seat => {
    if (seat.firstChild) {
      pool.appendChild(seat.firstChild);
    }
  });
}

/* 초기 실행 */
renderPool();

const seats = document.querySelectorAll(".seat");
const pool = document.getElementById("pool");

/* 초기 렌더 */
function init() {
  pool.innerHTML = "";

  people.forEach(name => {
    const div = document.createElement("div");
    div.className = "person";
    div.draggable = true;
    div.textContent = name;

    div.ondragstart = () => current = div;

    pool.appendChild(div);
  });
}

let current = null;

/* 드롭 */
seats.forEach(seat => {
  seat.ondragover = e => e.preventDefault();

  seat.ondrop = () => {
    if (!current) return;

    if (seat.firstChild) {
      pool.appendChild(seat.firstChild);
    }

    seat.appendChild(current);
  };
});

/* 랜덤 (좌석 내부만) */
function shuffleSeats() {
  let assigned = Array.from(seats)
    .map(s => s.firstChild)
    .filter(Boolean);

  for (let i = assigned.length - 1; i > 0; i--) {
    let j = Math.floor(Math.random() * (i + 1));
    [assigned[i], assigned[j]] = [assigned[j], assigned[i]];
  }

  seats.forEach((seat, i) => {
    if (assigned[i]) {
      seat.innerHTML = "";
      seat.appendChild(assigned[i]);
    }
  });
}

/* 초기화 */
function resetSeats() {
  seats.forEach(seat => {
    if (seat.firstChild) {
      pool.appendChild(seat.firstChild);
    }
  });
}

init();