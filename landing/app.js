const DEMO_DATA_URL = "./demo-data.json";

const state = {
  queries: [],
  activeQuery: null,
};

function normalize(text) {
  return text.trim().toLowerCase();
}

function formatTimestamp(timestamp) {
  return timestamp;
}

function createElement(tagName, textContent) {
  const element = document.createElement(tagName);
  if (textContent !== undefined) {
    element.textContent = textContent;
  }
  return element;
}

function clearNode(node) {
  node.replaceChildren();
}

function renderPresets(container, queries, onSelect) {
  clearNode(container);

  queries.forEach((query) => {
    const button = createElement("button", query.label);
    button.type = "button";
    button.dataset.prompt = query.prompt;
    button.addEventListener("click", () => onSelect(query));
    container.appendChild(button);
  });
}

function renderResults(container, query, inputValue) {
  clearNode(container);

  if (!query) {
    container.appendChild(createElement("p", "No matching bundled demo clip found."));
    return;
  }

  const querySummary = createElement("p");
  const queryStrong = createElement("strong", inputValue);
  querySummary.append("Query: ");
  querySummary.appendChild(queryStrong);

  const detailSummary = createElement(
    "p",
    `Showing the closest trimmed preview from bundled example data for "${query.label}".`,
  );

  container.appendChild(querySummary);
  container.appendChild(detailSummary);

  query.results.forEach((result) => {
    const article = createElement("article");
    const heading = createElement("h3", result.clip_label);
    const details = document.createElement("dl");

    [
      ["Camera", result.camera],
      ["Timestamp", formatTimestamp(result.timestamp)],
      ["Score", result.score.toFixed(2)],
    ].forEach(([label, value]) => {
      const row = document.createElement("div");
      row.appendChild(createElement("dt", label));
      row.appendChild(createElement("dd", value));
      details.appendChild(row);
    });

    article.appendChild(heading);
    article.appendChild(details);
    container.appendChild(article);
  });
}

function findMatchingQuery(queries, value) {
  const normalizedValue = normalize(value);
  if (!normalizedValue) {
    return null;
  }

  let bestMatch = null;
  let bestScore = 0;

  queries.forEach((query) => {
    const prompt = normalize(query.prompt);
    const label = normalize(query.label);
    let score = 0;

    if (normalizedValue === prompt || normalizedValue === label) {
      score = 100;
    } else if (normalizedValue.includes(prompt) || prompt.includes(normalizedValue)) {
      score = 50;
    } else if (normalizedValue.includes(label) || label.includes(normalizedValue)) {
      score = 40;
    }

    prompt.split(/\s+/).forEach((word) => {
      if (word.length > 3 && normalizedValue.includes(word)) {
        score += 1;
      }
    });

    if (score > bestScore) {
      bestScore = score;
      bestMatch = query;
    }
  });

  return bestScore > 0 ? bestMatch : null;
}

function setActiveQuery(query, input, results) {
  state.activeQuery = query;
  input.value = query ? query.prompt : input.value;
  renderResults(results, query, input.value);
}

async function loadDemoData() {
  const response = await fetch(DEMO_DATA_URL);
  if (!response.ok) {
    throw new Error(`Failed to load demo data: ${response.status}`);
  }
  return response.json();
}

document.addEventListener("DOMContentLoaded", async () => {
  const form = document.getElementById("sample-search-form");
  const input = document.getElementById("sample-query-input");
  const results = document.getElementById("sample-results");
  const presets = document.getElementById("sample-presets");

  if (!form || !input || !results || !presets) {
    return;
  }

  results.textContent = "Loading bundled demo clips...";

  try {
    state.queries = await loadDemoData();
    renderPresets(presets, state.queries, (query) => {
      input.value = query.prompt;
      setActiveQuery(query, input, results);
    });

    const initialQuery = state.queries[0] ?? null;
    if (initialQuery) {
      input.value = initialQuery.prompt;
      setActiveQuery(initialQuery, input, results);
    }

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const matchedQuery = findMatchingQuery(state.queries, input.value);
      setActiveQuery(matchedQuery, input, results);
    });
  } catch (error) {
    results.textContent = "Bundled sample search data could not be loaded.";
    console.error(error);
  }
});
