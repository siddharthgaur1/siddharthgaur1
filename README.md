<p align="center">
  <a href="https://siddharth-gaur.netlify.app">
    <img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/banner.svg" alt="Siddharth Gaur — AI/ML Engineer: Graph Neural Networks, LLM Agents, Retrieval Systems" width="100%" />
  </a>
</p>

<p align="center">
  <a href="https://siddharth-gaur.netlify.app"><img src="https://img.shields.io/badge/Portfolio-111827?style=flat-square&logo=googlechrome&logoColor=white" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/siddharth-gaur-804924293/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:siddharthgaur200304@gmail.com"><img src="https://img.shields.io/badge/Email-2563EB?style=flat-square&logo=gmail&logoColor=white" alt="Email" /></a>
  <img src="https://img.shields.io/badge/Open_to-AI%2FML_roles_·_Mumbai%2Fremote-7C3AED?style=flat-square" alt="Open to roles" />
</p>

<p align="center">
  <a href="#-open-source">Open Source</a> ·
  <a href="#-start-here--four-projects">Flagship Projects</a> ·
  <a href="#-also-built-no-signup-no-api-key">More Projects</a> ·
  <a href="#-tech-stack">Stack</a> ·
  <a href="#-connect">Connect</a>
</p>

<a href="https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/"><img src="https://raw.githubusercontent.com/siddharthgaur1/sebi-explorer/main/docs/demo.png" width="620" alt="SEBI Enforcement Explorer - live demo"></a>

<sub>▶ One of six live demos — **[SEBI Enforcement Explorer](https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/)**: real public SEBI enforcement orders, classified and analysed. No signup, no API key.</sub>

---

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/output/github-snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/output/github-snake.svg" />
    <img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/output/github-snake.svg" alt="Contribution graph snake animation" />
  </picture>
</p>

---

### 📌 Open Source

Maintainer-reviewed work outside my own account — including `DenseGATv2Conv`, which lands directly on the GNN work below.

| PR | Project | Status |
|---|---|---|
| [#1386](https://github.com/jsvine/pdfplumber/pull/1386) — surface the wrapped exception class name in blank `PdfminerException` messages | pdfplumber | **Merged** |
| [#10755](https://github.com/pyg-team/pytorch_geometric/pull/10755) — add `DenseGATv2Conv` | PyTorch Geometric | Open |
| [#10759](https://github.com/pyg-team/pytorch_geometric/pull/10759) — fix `KeyError` in `separate()` for attribute-less heterogeneous node stores | PyTorch Geometric | Open |
| [#10757](https://github.com/pyg-team/pytorch_geometric/pull/10757) — clarify `radius`/`radius_graph` CPU vs. GPU behaviour in docs | PyTorch Geometric | Open |
| [#10761](https://github.com/pyg-team/pytorch_geometric/pull/10761) — add Shapes docstrings to `TransformerConv`/`SplineConv` | PyTorch Geometric | Open |

---

### 🏆 Start here — four projects

What each does, what's actually hard about it, and a real measured result (not a claimed one).

| Project | What's technically hard | Measured result |
|---|---|---|
| **[⚖️ indic-reg-bench](https://github.com/siddharthgaur1/indic-reg-bench)** — an open benchmark for Indian regulatory document understanding on SEBI enforcement orders: five tasks, pip-installable harness, [HF dataset](https://huggingface.co/datasets/siddharthgaur/indic-reg-bench). *Everything else here is a system I built; this is an instrument others measure* their *systems with* | Designing tasks a regex can't solve. SEBI orders quote the noticee's own settlement pleas in phrasing identical to the ruling, so the first currency amount in a document is the wrong answer 46.7% of the time — that gap is a task, not a bug. Two proposed tasks were cut for being regex-solvable, one for having no signal at this corpus size | 11,957 orders indexed (Nov 2004 – Jul 2026), harness green in CI. **No leaderboard numbers yet, deliberately** — scores need a hand-labelled gold set, and publishing model-generated labels as ground truth would destroy the instrument |
| **[🕸️ elliptic-gatv2-aml](https://github.com/siddharthgaur1/elliptic-gatv2-aml)** — flags illicit Bitcoin transactions on a 200k-node temporal graph, benchmarking GATv2/GCN against Random Forest and an MLP under identical splits | Diagnosing *why* the graph model loses — illicit nodes are ~2% of the graph, so message passing dilutes their already-informative features with a majority-class neighborhood — instead of just reporting the number | **Illicit-F1: Random Forest 0.8085 vs. GATv2 0.4266.** Random Forest wins, and the README says so. Every number traces to a committed `results/*.json` run |
| **[🕵️ corpgraph-rag](https://github.com/siddharthgaur1/corpgraph-rag)** — GraphRAG over a Neo4j graph of Indian corporate entities (directors, auditors, promoters, SEBI orders). Question → LLM query plan → few-shot Cypher → traversal → cited answer | The generator's own write-clause check is just a fast-fail; the real guarantee is a regex-enforced read-only guard on the Neo4j client itself, so a prompt-injected write fails before it reaches the database | `test_read_only_guard.py` passes independent of whether Neo4j is even running. No labeled accuracy set for generated-Cypher correctness yet — tracked as an open issue rather than glossed over |
| **[🏗️ ml-platform](https://github.com/siddharthgaur1/ml-platform)** — feature store + drift monitor + real-time fraud scoring (Kafka/Redpanda → Redis → XGBoost+IsolationForest → Postgres) running through both. Previously three repos, now one | Merging them is the point. Apart, the seams were load-bearing bugs: `featurestore` shipped drift detection as a *documented stub*, the monitor **duck-typed** its feature-store adapter rather than importing it, and the fraud service wrapped `import ml_monitor` in a `try/except ImportError` returning `None` — a whole monitoring backend could silently do nothing | No train/serve skew: online (Redis) and offline (training) features call the same function. Load-tested at **29.7 req/s, p99 2700ms at 50 concurrent users**, with the bottleneck identified (`uvicorn` without `--workers`), not hand-waved |

All four have green CI, a `CHANGELOG.md`, and an open issues list of things I'd actually fix next.

**Check any of it in a minute:** `pytest --cov=llm_regressor` reprints the coverage figure from a clean clone with no API key; the Elliptic F1 scores read straight out of committed `results/*.json`. Where a number *can't* be reproduced without a paid API key, the README says so instead of quoting one.

---

### ▶ Also built, no signup, no API key

<details>
<summary><strong>11 more projects — eval harnesses, RAG, graph sims, IPO forecasting, data-quality monitoring, causal inference, MCP, security benchmarking</strong> (click to expand)</summary>
<br />

| Project | What it does | |
|---|---|---|
| **[agent-eval-harness](https://github.com/siddharthgaur1/agent-eval-harness)** | Trajectory-level evaluation for multi-step LLM agents — scores the path taken, not just the final answer. Agents are stochastic, so separating real degradation from run-to-run variance is the whole problem | [▶ **demo**](https://siddharthgaur1-siddharthagent-eval-harness-dashboardapp-rppgf9.streamlit.app/) — a real detected regression between two agent versions |
| **[llm-regressor](https://github.com/siddharthgaur1/llm-regressor)** | *The library + CI gate.* Model-agnostic (Claude/OpenAI/Ollama/LiteLLM) regression testing for prompt and model changes; a reusable GitHub Action gates a PR in five lines. **123 tests, 100% statement and branch coverage**, ~2s with no API key | — |
| **[llm-regression-detector](https://github.com/siddharthgaur1/llm-regression-detector)** | *The dashboard + alerting.* Same problem from the other end: a standing harness with a golden dataset, per-category scoring and Slack drift alerts | [▶ **demo**](https://siddharthgaur1-siddharthllm-regression-detector-dashboardapp.streamlit.app/) — evals and drift across runs |
| **[querypilot-v2](https://github.com/siddharthgaur1/querypilot-v2)** | English → SQL with a schema-aware RAG layer (retrieves the 3 relevant table chunks, not a full schema dump). The write-safety boundary is a SQLite `PRAGMA query_only` + authorizer at the DB layer, so a prompt-injection bypass of the earlier checks still can't write | [▶ **demo**](https://siddharthgaur1-siddharthquerypilot-srcapp-ebww0h.streamlit.app/) — runs [v1](https://github.com/siddharthgaur1/querypilot): same safety path, older retrieval |
| **[autonomous-data-scientist](https://github.com/siddharthgaur1/autonomous-data-scientist)** | Give it a CSV and *"predict churn"* — an 11-agent LangGraph pipeline cleans, explores, engineers features, tunes, evaluates, and ships a report and deck. Generated pandas runs through an AST **whitelist** into a locked-down subprocess (import guard, path guard, rlimits, wall-clock kill). **65 tests passing** | — |
| **[Sebi-Explorer](https://github.com/siddharthgaur1/Sebi-Explorer)** | Analytics over real public SEBI enforcement orders: violation classification, penalties, entity network, timeline — the corpus problem that motivated `indic-reg-bench` | [▶ **demo**](https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/) — search, network, timeline |
| **[rail-graph](https://github.com/siddharthgaur1/rail-graph)** | Graph analysis of a synthetic 600-station Indian railway network — PageRank, betweenness, k-shortest paths, resilience simulation. The sim re-runs betweenness per removed node, so the naive version doesn't finish | [▶ **demo**](https://siddharthgaur1-siddharthrail-graph-srcapp-hme3vr.streamlit.app/) — remove links, watch routing degrade |
| **[ipo-gmp](https://github.com/siddharthgaur1/ipo-gmp)** | XGBoost predicting Indian IPO listing-day returns from Grey Market Premium. Time-ordered data punishes random splits, so validation is time-series CV with calibrated bands. **Synthetic dataset**, clearly labelled — real GMP data isn't publicly licensable | [▶ **demo**](https://siddharthgaur1-siddharthipo-gmp-srcapp-htnhfl.streamlit.app/) — CV and confidence bands |
| **[nse-daily-monitor](https://github.com/siddharthgaur1/nse-daily-monitor)** | Scheduled data-quality monitoring of the NSE equity bhavcopy — coverage, OHLC bounds, null rates and breadth checked against a trailing 60-day baseline, opening a GitHub issue when a check fails. Publishes **derived metrics only**, never a reconstructable quote, so it runs in public without redistributing exchange data. Built on [nse-warehouse](https://github.com/siddharthgaur1/nse-warehouse) | [▶ **run history**](https://github.com/siddharthgaur1/nse-daily-monitor/actions) — the uptime is the artifact |
| **[causal-lens](https://github.com/siddharthgaur1/causal-lens)** | Causal inference toolkit — four independently usable methods for "did this intervention actually cause this outcome," not just correlation: A/B testing (frequentist + Bayesian + CUPED), difference-in-differences, synthetic control, and uplift modelling | — |
| **[indian-markets-mcp](https://github.com/siddharthgaur1/indian-markets-mcp)** | An MCP server exposing Indian market and regulatory data — NSE bhavcopy, NIFTY constituents, AMFI NAVs, SEBI orders — from official, openly published sources only. `latest_day()` resolves against IST, not the host's local clock, so a UTC-hosted server doesn't report yesterday's close as today's for part of every evening | — |
| **[query-injection-bench](https://github.com/siddharthgaur1/query-injection-bench)** | An adversarial benchmark for prompt injection against NL-to-SQL/Cypher agents: 226 cases, five scored defences, a false-positive set that counts. Found a **critical read-only bypass in my own Cypher guard** — a `//` inside a string literal blinded the validator to a `DETACH DELETE` the database would have executed | [FINDINGS.md](https://github.com/siddharthgaur1/query-injection-bench/blob/master/FINDINGS.md) — attack success rate 0.221 → 0.130 after the fix |

<sub>Demos are hosted free on Streamlit Community Cloud; a sleeping app takes ~30–60s to wake. Each also runs locally from its repo's Quickstart with no API key.</sub>

</details>

---

### 🧰 Tech Stack

`Python` · `SQL` · `LangGraph` · `PyTorch` · `PyTorch Geometric` · `scikit-learn` · `XGBoost` · `Neo4j` · `ChromaDB` · `FastAPI` · `Docker` · `Kafka` · `Redis` · `PostgreSQL` · `GitHub Actions`

---

### 📫 Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/siddharth-gaur-804924293/)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:siddharthgaur200304@gmail.com)

<p align="center">
  <img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/footer.svg" alt="" width="100%" />
</p>
