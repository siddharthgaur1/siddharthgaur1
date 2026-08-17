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

### ▶ Live demos — click and try, no signup, no API key

| | Demo | What you'll see |
|---|---|---|
| <img src="https://raw.githubusercontent.com/siddharthgaur1/agent-eval-harness/main/docs/demo.png" width="150" alt="Agent Eval Harness scorecard"> | **[Agent Eval Harness](https://siddharthgaur1-siddharthagent-eval-harness-dashboardapp-rppgf9.streamlit.app/)** | A real detected regression between two agent versions, scored on trajectories |
| <img src="https://raw.githubusercontent.com/siddharthgaur1/rail-graph/master/docs/demo.png" width="150" alt="RailGraph network explorer"> | **[RailGraph](https://siddharthgaur1-siddharthrail-graph-srcapp-hme3vr.streamlit.app/)** | 600-station rail network — PageRank, betweenness, k-shortest-paths, resilience sim |
| <img src="https://raw.githubusercontent.com/siddharthgaur1/sebi-explorer/main/docs/demo.png" width="150" alt="SEBI Enforcement Explorer dashboard"> | **[SEBI Enforcement Explorer](https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/)** | Real public SEBI orders, classified and analysed — search, network, timeline |
| <img src="https://raw.githubusercontent.com/siddharthgaur1/querypilot/master/docs/demo.png" width="150" alt="QueryPilot natural language to SQL"> | **[QueryPilot](https://siddharthgaur1-siddharthquerypilot-srcapp-ebww0h.streamlit.app/)** | English → SQL with a DB-layer safety authorizer; runs the full safety path, no key |
| <img src="https://raw.githubusercontent.com/siddharthgaur1/ipo-gmp/master/docs/demo.png" width="150" alt="IPO GMP Predictor dashboard"> | **[IPO GMP Predictor](https://siddharthgaur1-siddharthipo-gmp-srcapp-htnhfl.streamlit.app/)** | XGBoost pipeline with time-series CV and calibrated confidence bands (synthetic data) |
| <img src="https://raw.githubusercontent.com/siddharthgaur1/llm-regression-detector/master/docs/demo.png" width="150" alt="LLM Regression Detector dashboard"> | **[LLM Regression Detector](https://siddharthgaur1-siddharthllm-regression-detector-dashboardapp.streamlit.app/)** | Golden-dataset evals across runs, per-category scoring and drift |

<sub>Hosted free on Streamlit Community Cloud; a sleeping app takes ~30–60s to wake. Each also runs locally from its repo's Quickstart with no API key.</sub>

---

### 🔨 What I Build

Seven projects I'd point you to first — what each does, what's actually hard about it, and a real measured result (not a claimed one):

| Project | What it does | What's technically hard | Measured result |
|---|---|---|---|
| [⚖️ indic-reg-bench](https://github.com/siddharthgaur1/indic-reg-bench) | An open benchmark for Indian regulatory document understanding, built on SEBI enforcement orders — five tasks, a pip-installable harness, and a [HuggingFace dataset](https://huggingface.co/datasets/siddharthgaur/indic-reg-bench). Everything else here is a system I built; this is an instrument other people measure *their* systems with | Designing tasks a regex can't solve. SEBI orders quote the noticee's own settlement pleas in phrasing identical to the ruling, so the first currency amount in a document is the wrong answer 46.7% of the time — that gap is a task, not a bug. Two proposed tasks were cut for being regex-solvable and one for having no signal at this corpus size | 11,957 orders indexed (Nov 2004 – Jul 2026), harness green in CI. **No leaderboard numbers yet, deliberately** — scores need a hand-labelled gold set, and publishing model-generated labels as ground truth would destroy the instrument |
| [🕵️ corpgraph-rag](https://github.com/siddharthgaur1/corpgraph-rag) | GraphRAG over a Neo4j graph of Indian corporate entities — directors, auditors, promoters, SEBI orders, mutual funds. English question → LLM query plan → few-shot Cypher → traversal → cited answer | The generator's own write-clause check is just a fast-fail; the real guarantee is a regex-enforced read-only guard on the Neo4j client itself, so a prompt-injected write fails before it ever reaches the database | `test_read_only_guard.py` passes independent of whether Neo4j is even running. No labeled accuracy set for generated-Cypher correctness yet — tracked as an open issue rather than glossed over |
| [🕸️ Elliptic GATv2 AML](https://github.com/siddharthgaur1/elliptic-gatv2-aml) | Flags illicit Bitcoin transactions on a 200k-node temporal graph, benchmarking GATv2/GCN against Random Forest and an MLP under identical splits | Diagnosing *why* the graph model loses — illicit nodes are ~2% of the graph, so message passing dilutes their already-informative features with a majority-class neighborhood — instead of just reporting the number | **Illicit-F1: Random Forest 0.8085 vs. GATv2 0.4266.** Random Forest wins, and the README says so. Every number traces to a committed `results/*.json` run |
| [🏗️ ml-platform](https://github.com/siddharthgaur1/ml-platform) | A feature store, a drift monitor, and a real-time fraud-scoring service (Kafka/Redpanda → Redis rolling features → XGBoost+IsolationForest → Postgres) that runs through both. Previously three separate repos, now one | Merging them is the point. Apart, the seams were load-bearing bugs: `featurestore` shipped drift detection as a *documented stub*, `ml-monitor` **duck-typed** its feature-store adapter rather than importing it, and the fraud service wrapped `import ml_monitor` in a `try/except ImportError` that returned `None` — a whole monitoring backend could silently do nothing | Online (Redis) and offline (training) features call the same function, so there's no train/serve skew. Load-tested at **29.7 req/s, p99 2700ms at 50 concurrent users** — with the bottleneck identified (`uvicorn` running without `--workers`), not hand-waved |
| [🧬 llm-regressor](https://github.com/siddharthgaur1/llm-regressor) | Model-agnostic (Claude/OpenAI/Ollama/LiteLLM) regression testing for LLM prompt and model changes, with a reusable GitHub Action that gates a pull request in five lines | Severity has to fail closed on deterministic checks (wrong format, missing fact) while treating LLM-judge score drops as directional, not absolute — conflating the two makes the gate either too paranoid to trust or too permissive to bother with | **123 tests, 100% statement and branch coverage** (`pytest --cov=llm_regressor`), running in ~2s with no API key because the vendor SDKs are faked at import level. Honest gap: no published accuracy figure for the checks themselves — that needs two live models |
| [🧭 QueryPilot v2](https://github.com/siddharthgaur1/querypilot-v2) | Natural language → SQL, rebuilt with a schema-aware RAG layer (retrieves only the 3 relevant table chunks per question, not a full schema dump), Postgres history, Docker Compose | The actual write-safety boundary is a SQLite `PRAGMA query_only` + authorizer at the DB layer — the earlier regex/LLM-self-check layers are friendly early rejections, not the guarantee, so a prompt-injection bypass of those still can't write | Real captured request-response (186.6ms, correct 3-of-4 table retrieval) in the README. No golden-set accuracy number committed yet — the eval harness exists (`eval/benchmark.py`, ported from v1's set) but needs a live LLM run, tracked as an open issue |
| [🤖 Autonomous Data Scientist](https://github.com/siddharthgaur1/autonomous-data-scientist) | Give it a CSV and *"predict churn"* — an 11-agent LangGraph pipeline cleans, explores, engineers features, tunes a model, evaluates it, and ships a report and slide deck | Generated pandas code runs through an AST whitelist policy check into a locked-down subprocess (import guard, path guard, rlimits, wall-clock kill) — a blacklist approach would miss whatever wasn't anticipated | **65 tests passing** across agents/API/graph/persistence/sandbox; real metrics from an actual run are committed in the README, not invented |

All seven have green CI, a `CHANGELOG.md`, and an open issues list of things I'd actually fix next — not manufactured busywork.

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
