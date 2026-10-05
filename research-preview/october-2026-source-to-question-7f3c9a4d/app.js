const menuButton = document.querySelector("[data-menu-button]");
const navigation = document.querySelector("[data-navigation]");

if (menuButton && navigation) {
  menuButton.addEventListener("click", () => {
    const expanded = menuButton.getAttribute("aria-expanded") === "true";
    menuButton.setAttribute("aria-expanded", String(!expanded));
    navigation.classList.toggle("is-open", !expanded);
  });

  navigation.addEventListener("click", (event) => {
    if (event.target instanceof HTMLAnchorElement) {
      navigation.classList.remove("is-open");
      menuButton.setAttribute("aria-expanded", "false");
    }
  });
}

document.querySelectorAll("[data-tabs]").forEach((tabs) => {
  const buttons = [...tabs.querySelectorAll("[data-tab]")];
  const panels = [...tabs.querySelectorAll("[data-panel]")];

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const target = button.getAttribute("data-tab");
      buttons.forEach((candidate) => candidate.setAttribute("aria-selected", String(candidate === button)));
      panels.forEach((panel) => { panel.hidden = panel.id !== target; });
    });

    button.addEventListener("keydown", (event) => {
      if (!['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
      event.preventDefault();
      const current = buttons.indexOf(button);
      const offset = event.key === 'ArrowRight' ? 1 : -1;
      buttons[(current + offset + buttons.length) % buttons.length].focus();
    });
  });
});

const handleData = {
  spices: {
    move: "M001 · Mark 16:1",
    source: "“Mary Magdalene, Mary the mother of James, and Salome, bought spices, that they might come and anoint him.”",
    modes: "Lexical · material-cultural · translation",
    said: "The phrase is exact source evidence inside M001 and can anchor separately governed lexical or burial-practice research.",
    unknown: "No historical practice claim is established by the Move or by model memory alone.",
    question: "What exact, dated historical sources bear on spices used in first-century Jewish burial practice?"
  },
  mary: {
    move: "M001 · Mark 16:1",
    source: "“Mary Magdalene, Mary the mother of James, and Salome…”",
    modes: "Entity · source occurrence · identity restraint",
    said: "Mary Magdalene is an explicitly named participant and part of the collective agent in this exact Move.",
    unknown: "The Move alone does not establish every cross-source identity claim or later Reception relation.",
    question: "Which governed occurrences can be linked by exact source reference without assuming more historical identity than the evidence supports?"
  },
  risen: {
    move: "M011 · Mark 16:6",
    source: "“He has risen.”",
    modes: "Lexical · source-language form · language-in-use",
    said: "M011 represents the independently asserted operation ‘rise’; the exact SBLGNT handle ἠγέρθη is available in the bounded lexical pilot evidence.",
    unknown: "This Move alone does not establish a complete theology, causal history, or every possible meaning of resurrection.",
    question: "What can the supplied source-language and comparison evidence establish about this form without turning etymology into passage meaning?"
  }
};

const explorer = document.querySelector("[data-handle-explorer]");
if (explorer) {
  const buttons = [...explorer.querySelectorAll("[data-handle]")];
  const fields = {
    move: explorer.querySelector("[data-handle-move]"),
    source: explorer.querySelector("[data-handle-source]"),
    modes: explorer.querySelector("[data-handle-modes]"),
    said: explorer.querySelector("[data-handle-said]"),
    unknown: explorer.querySelector("[data-handle-unknown]"),
    question: explorer.querySelector("[data-handle-question]")
  };

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      const value = handleData[button.dataset.handle];
      if (!value) return;
      buttons.forEach((candidate) => candidate.classList.toggle("is-active", candidate === button));
      Object.entries(fields).forEach(([key, node]) => { if (node) node.textContent = value[key]; });
    });
  });
}

