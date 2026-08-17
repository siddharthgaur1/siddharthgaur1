# Hi, I'm Siddharth 👋

[🌐 siddharth-gaur.netlify.app](https://siddharth-gaur.netlify.app)

**AI/ML Engineer** · Building at the intersection of **graph neural networks**, **LLM agents**, and **retrieval systems**

**📍 Currently open to AI/ML Engineer roles — Mumbai / remote**

---

### 📌 Open Source

Work reviewed by maintainers outside my own account — including `DenseGATv2Conv`, which lands directly on the GNN work below.

| PR | Project | Status |
|---|---|---|
| [#1386](https://github.com/jsvine/pdfplumber/pull/1386) — surface the wrapped exception class name in blank `PdfminerException` messages | pdfplumber | **Merged** |
| [#10755](https://github.com/pyg-team/pytorch_geometric/pull/10755) — add `DenseGATv2Conv` | PyTorch Geometric | Open |
| [#10759](https://github.com/pyg-team/pytorch_geometric/pull/10759) — fix `KeyError` in `separate()` for attribute-less heterogeneous node stores | PyTorch Geometric | Open |
| [#10757](https://github.com/pyg-team/pytorch_geometric/pull/10757) — clarify `radius`/`radius_graph` CPU (k-d tree) vs. GPU (brute-force) behaviour in docs | PyTorch Geometric | Open |
| [#10761](https://github.com/pyg-team/pytorch_geometric/pull/10761) — add Shapes docstrings to `TransformerConv`/`SplineConv` | PyTorch Geometric | Open |

---

### 🔨 Projects

Everything I'd point you to, ranked. **▶ Live demo** means click and try it — no signup, no API key. What each does, what's actually hard about it, and a real measured result (not a claimed one):

| Project | What it does | What's technically hard | Measured result |
|---|---|---|---|
| **[⚖️ indic-reg-bench](https://github.com/siddharthgaur1/indic-reg-bench)**<br><sub>[📦 HuggingFace dataset](https://huggingface.co/datasets/siddharthgaur/indic-reg-bench)</sub> | An open benchmark for Indian regulatory document understanding, built on SEBI enforcement orders — five tasks and a pip-installable harness. Everything else here is a system I built; this is an instrument other people measure *their* systems with | Designing tasks a regex can't solve. SEBI orders quote the noticee's own settlement pleas in phrasing identical to the ruling, so the first currency amount in a document is the wrong answer 46.7% of the time — that gap is a task, not a bug. Two proposed tasks were cut for being regex-solvable and one for having no signal at this corpus size | 11,957 orders indexed (Nov 2004 – Jul 2026), harness green in CI. **No leaderboard numbers yet, deliberately** — scores need a hand-labelled gold set, and publishing model-generated labels as ground truth would destroy the instrument |
| **[🕵️ corpgraph-rag](https://github.com/siddharthgaur1/corpgraph-rag)** | GraphRAG over a Neo4j graph of Indian corporate entities — directors, auditors, promoters, SEBI orders, mutual funds. English question → LLM query plan → few-shot Cypher → traversal → cited answer | The generator's own write-clause check is just a fast-fail; the real guarantee is a regex-enforced read-only guard on the Neo4j client itself, so a prompt-injected write fails before it ever reaches the database | `test_read_only_guard.py` passes independent of whether Neo4j is even running. No labeled accuracy set for generated-Cypher correctness yet — tracked as an open issue rather than glossed over |
| **[🕸️ elliptic-gatv2-aml](https://github.com/siddharthgaur1/elliptic-gatv2-aml)** | Flags illicit Bitcoin transactions on a 200k-node temporal graph, benchmarking GATv2/GCN against Random Forest and an MLP under identical splits | Diagnosing *why* the graph model loses — illicit nodes are ~2% of the graph, so message passing dilutes their already-informative features with a majority-class neighborhood — instead of just reporting the number | **Illicit-F1: Random Forest 0.8085 vs. GATv2 0.4266.** Random Forest wins, and the README says so. Every number traces to a committed `results/*.json` run |
| **[🏗️ ml-platform](https://github.com/siddharthgaur1/ml-platform)** | A feature store, a drift monitor, and a real-time fraud-scoring service (Kafka/Redpanda → Redis rolling features → XGBoost+IsolationForest → Postgres) that runs through both. Previously three separate repos, now one | Merging them is the point. Apart, the seams were load-bearing bugs: `featurestore` shipped drift detection as a *documented stub*, `ml-monitor` **duck-typed** its feature-store adapter rather than importing it, and the fraud service wrapped `import ml_monitor` in a `try/except ImportError` that returned `None` — a whole monitoring backend could silently do nothing | Online (Redis) and offline (training) features call the same function, so there's no train/serve skew. Load-tested at **29.7 req/s, p99 2700ms at 50 concurrent users** — with the bottleneck identified (`uvicorn` running without `--workers`), not hand-waved |
| **[🧬 llm-regressor](https://github.com/siddharthgaur1/llm-regressor)**<br><sub>*the library + CI gate*</sub> | Model-agnostic (Claude/OpenAI/Ollama/LiteLLM) regression testing for LLM prompt and model changes, with a reusable GitHub Action that gates a pull request in five lines | Severity has to fail closed on deterministic checks (wrong format, missing fact) while treating LLM-judge score drops as directional, not absolute — conflating the two makes the gate either too paranoid to trust or too permissive to bother with | **123 tests, 100% statement and branch coverage** (`pytest --cov=llm_regressor`), running in ~2s with no API key because the vendor SDKs are faked at import level. Honest gap: no published accuracy figure for the checks themselves — that needs two live models |
| **[📉 llm-regression-detector](https://github.com/siddharthgaur1/llm-regression-detector)**<br><sub>*the dashboard + alerting*</sub><br>[▶ **Live demo**](https://siddharthgaur1-siddharthllm-regression-detector-dashboardapp.streamlit.app/)<br><img src="https://raw.githubusercontent.com/siddharthgaur1/llm-regression-detector/master/docs/demo.png" width="130" alt="LLM Regression Detector dashboard"> | The same problem as `llm-regressor` approached from the other end: where that one is a library you import and a CI gate, this is a standing harness with a golden dataset, a scoring dashboard, and Slack drift alerts | Scoring has to stay comparable across runs when the golden set itself grows — a per-category breakdown that silently rebaselines makes every drift number meaningless | Golden-dataset evals across runs with per-category scoring and drift, visible in the live dashboard above |
| **[🧭 querypilot-v2](https://github.com/siddharthgaur1/querypilot-v2)**<br>[▶ **Live demo** *(v1)*](https://siddharthgaur1-siddharthquerypilot-srcapp-ebww0h.streamlit.app/)<br><img src="https://raw.githubusercontent.com/siddharthgaur1/querypilot/master/docs/demo.png" width="130" alt="QueryPilot natural language to SQL"> | Natural language → SQL, rebuilt with a schema-aware RAG layer (retrieves only the 3 relevant table chunks per question, not a full schema dump), Postgres history, Docker Compose | The actual write-safety boundary is a SQLite `PRAGMA query_only` + authorizer at the DB layer — the earlier regex/LLM-self-check layers are friendly early rejections, not the guarantee, so a prompt-injection bypass of those still can't write | Real captured request-response (186.6ms, correct 3-of-4 table retrieval) in the README. No golden-set accuracy number committed yet — the eval harness exists (`eval/benchmark.py`, ported from v1's set) but needs a live LLM run, tracked as an open issue. **The demo above runs [v1](https://github.com/siddharthgaur1/querypilot)** — same safety path, older retrieval layer |
| **[🤖 autonomous-data-scientist](https://github.com/siddharthgaur1/autonomous-data-scientist)** | Give it a CSV and *"predict churn"* — an 11-agent LangGraph pipeline cleans, explores, engineers features, tunes a model, evaluates it, and ships a report and slide deck | Generated pandas code runs through an AST whitelist policy check into a locked-down subprocess (import guard, path guard, rlimits, wall-clock kill) — a blacklist approach would miss whatever wasn't anticipated | **65 tests passing** across agents/API/graph/persistence/sandbox; real metrics from an actual run are committed in the README, not invented |
| **[📊 agent-eval-harness](https://github.com/siddharthgaur1/agent-eval-harness)**<br>[▶ **Live demo**](https://siddharthgaur1-siddharthagent-eval-harness-dashboardapp-rppgf9.streamlit.app/)<br><img src="https://raw.githubusercontent.com/siddharthgaur1/agent-eval-harness/main/docs/demo.png" width="130" alt="Agent Eval Harness scorecard"> | Trajectory-level evaluation and variance-aware regression detection for multi-step LLM agents — scores the path an agent took, not just its final answer | Agents are stochastic, so a single bad run isn't a regression. Separating real degradation from run-to-run variance is the whole problem | The demo shows a **real detected regression** between two agent versions, scored on trajectories |
| **[⚖️ Sebi-Explorer](https://github.com/siddharthgaur1/Sebi-Explorer)**<br>[▶ **Live demo**](https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/)<br><img src="https://raw.githubusercontent.com/siddharthgaur1/sebi-explorer/main/docs/demo.png" width="130" alt="SEBI Enforcement Explorer dashboard"> | Analytics over real public SEBI enforcement orders: violation classification, penalty analysis, entity network, timeline | Classifying violation types from order prose that reuses near-identical phrasing across very different offences — the same corpus problem that motivated `indic-reg-bench` | Real public SEBI orders, classified and analysed — searchable in the live dashboard |
| **[🚆 rail-graph](https://github.com/siddharthgaur1/rail-graph)**<br>[▶ **Live demo**](https://siddharthgaur1-siddharthrail-graph-srcapp-hme3vr.streamlit.app/)<br><img src="https://raw.githubusercontent.com/siddharthgaur1/rail-graph/master/docs/demo.png" width="130" alt="RailGraph network explorer"> | Graph analysis of a synthetic 600-station Indian railway network — PageRank, betweenness, k-shortest paths, and a resilience simulation for node removal | Betweenness on a network this size is the expensive part; the resilience sim re-runs it per removed node, so the naive version doesn't finish | 600-station network, interactive in the browser — pick any two stations and remove links to watch routing degrade |
| **[📈 ipo-gmp](https://github.com/siddharthgaur1/ipo-gmp)**<br>[▶ **Live demo**](https://siddharthgaur1-siddharthipo-gmp-srcapp-htnhfl.streamlit.app/)<br><img src="https://raw.githubusercontent.com/siddharthgaur1/ipo-gmp/master/docs/demo.png" width="130" alt="IPO GMP Predictor dashboard"> | XGBoost model predicting Indian IPO listing-day returns from Grey Market Premium data | Time-ordered data punishes random splits — the validation has to be time-series CV or the model reads the future. Confidence bands have to be calibrated, not just plotted | Time-series CV with calibrated confidence bands. **Synthetic dataset** — clearly labelled, because real GMP data isn't publicly licensable |

<sub>Demos are hosted free on Streamlit Community Cloud; a sleeping app takes ~30–60s to wake. Each also runs locally from its repo's Quickstart with no API key.</sub>

The top eight have green CI, a `CHANGELOG.md`, and an open issues list of things I'd actually fix next — not manufactured busywork.

**How to check any of this in about a minute:** every measured result above names the
command that produces it. `pytest --cov=llm_regressor` reprints the coverage figure from a
clean clone with no API key, and the Elliptic F1 scores read straight out of committed
`results/*.json`. Where a number *can't* be reproduced without a paid API key, the README
says so instead of quoting one.

---

### 🧰 Tech Stack

`Python` · `SQL` · `LangGraph` · `PyTorch` · `PyTorch Geometric` · `scikit-learn` · `XGBoost` · `Neo4j` · `ChromaDB` · `FastAPI` · `Docker` · `Kafka` · `Redis` · `PostgreSQL` · `GitHub Actions`

---

### 📫 Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/siddharth-gaur-804924293/)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:siddharthgaur200304@gmail.com)
