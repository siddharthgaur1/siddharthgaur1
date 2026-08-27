<p align="center">
  <a href="https://siddharth-gaur.netlify.app">
    <img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/banner.svg" alt="Siddharth Gaur — AI/ML Engineer: Graph Neural Networks, LLM Agents, Retrieval Systems" width="100%" />
  </a>
</p>

```
$ whoami
Siddharth Gaur — AI/ML Engineer, Mumbai / remote

$ cat focus.txt
Graph Neural Networks · LLM Agents · Retrieval Systems

$ ls -1 proof/
merged_oss_pr/          1
bugs_found_and_fixed/   3
green_ci_repos/         19
fabricated_numbers/     0   # empty by design, not by accident

$ echo $STATUS
open to AI/ML roles
```

<p align="center">
  <a href="https://siddharth-gaur.netlify.app"><img src="https://img.shields.io/badge/Portfolio-000000?style=flat-square&logo=googlechrome&logoColor=3B82F6&labelColor=000000" alt="Portfolio" /></a>
  <a href="https://www.linkedin.com/in/siddharth-gaur-804924293/"><img src="https://img.shields.io/badge/LinkedIn-000000?style=flat-square&logo=linkedin&logoColor=8B5CF6&labelColor=000000" alt="LinkedIn" /></a>
  <a href="mailto:siddharthgaur200304@gmail.com"><img src="https://img.shields.io/badge/Email-000000?style=flat-square&logo=gmail&logoColor=EC4899&labelColor=000000" alt="Email" /></a>
  <img src="https://img.shields.io/badge/Open_to-AI%2FML_roles_·_Mumbai%2Fremote-8B5CF6?style=flat-square&labelColor=000000" alt="Open to roles" />
</p>

<p align="center">
<code>$ profile --sections open-source flagship-projects more-projects tech-stack connect</code>
</p>

<p align="center">
  <a href="#-open-source">open-source</a> ·
  <a href="#-start-here--three-projects">flagship-projects</a> ·
  <a href="#-also-built-no-signup-no-api-key">more-projects</a> ·
  <a href="#-tech-stack">tech-stack</a> ·
  <a href="#-connect">connect</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/signal-strip.svg" alt="19 active repos, all green CI. 1 merged open-source PR. 3 real bugs found and fixed. 0 fabricated benchmark numbers." width="100%" />
</p>

<a href="https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/"><img src="https://raw.githubusercontent.com/siddharthgaur1/sebi-explorer/main/docs/demo.png" width="620" alt="SEBI Enforcement Explorer - live demo"></a>

<sub>▶ One of six live demos — **[SEBI Enforcement Explorer](https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/)**: real public SEBI enforcement orders, classified and analysed. No signup, no API key.</sub>

<p align="center"><img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/divider.svg" alt="" width="100%25" height="20" /></p>

### 📌 Open Source

Maintainer-reviewed work outside my own account — including `DenseGATv2Conv`, which lands directly on the GNN work below.

| PR | Project | Status |
|---|---|---|
| [#1386](https://github.com/jsvine/pdfplumber/pull/1386) — surface the wrapped exception class name in blank `PdfminerException` messages | pdfplumber | **Merged** |
| [#10755](https://github.com/pyg-team/pytorch_geometric/pull/10755) — add `DenseGATv2Conv` | PyTorch Geometric | Open |
| [#10759](https://github.com/pyg-team/pytorch_geometric/pull/10759) — fix `KeyError` in `separate()` for attribute-less heterogeneous node stores | PyTorch Geometric | Open |
| [#10757](https://github.com/pyg-team/pytorch_geometric/pull/10757) — clarify `radius`/`radius_graph` CPU vs. GPU behaviour in docs | PyTorch Geometric | Open |
| [#10761](https://github.com/pyg-team/pytorch_geometric/pull/10761) — add Shapes docstrings to `TransformerConv`/`SplineConv` | PyTorch Geometric | Open |

<p align="center"><img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/divider.svg" alt="" width="100%25" height="20" /></p>

### 🏆 Start here — three projects

Each with a real measured result, not a claimed one.

<table>
<tr>
<td width="40%"><a href="https://github.com/siddharthgaur1/openeval"><img src="https://raw.githubusercontent.com/siddharthgaur1/openeval/master/docs/screenshots/eval-runs.png" width="100%" alt="OpenEval"></a></td>
<td valign="top">

**[📊 OpenEval](https://github.com/siddharthgaur1/openeval)** — self-hosted LangSmith/Helicone alternative: trace every LLM call, version prompts and datasets, run RAG/LLM-judge evals against any provider, block regressions in CI. One `docker compose up`, no vendor lock-in.

Hard part: org → project → RBAC with per-project quotas designed in from the first migration, not bolted onto a single-tenant schema later — multi-tenancy retrofits are where authorization bugs live.

<img src="https://img.shields.io/badge/metrics-17_built--in-000000?style=flat-square&labelColor=000000&color=3B82F6" alt="17 metrics"> <img src="https://img.shields.io/badge/default_judge-local_Ollama%2C_%240-000000?style=flat-square&labelColor=000000&color=8B5CF6" alt="local, free by default"> <img src="https://img.shields.io/badge/CI-PR_regression_gate-000000?style=flat-square&labelColor=000000&color=EC4899" alt="CI regression gate">

</td>
</tr>
<tr>
<td width="40%"><a href="https://github.com/siddharthgaur1/deepresearch"><img src="https://raw.githubusercontent.com/siddharthgaur1/deepresearch/main/docs/screenshots/04-report.png" width="100%" alt="DeepResearch"></a></td>
<td valign="top">

**[🔎 DeepResearch](https://github.com/siddharthgaur1/deepresearch)** — 9-agent LangGraph pipeline: plan sub-questions, search in parallel, cross-check every claim against ≥2 sources, hand back a cited report with per-claim confidence. Runs end to end on Ollama for $0.

Hard part: the README's own **Security considerations** section flags its Docker-socket-mounted sandbox as a real container-escape vector and explains why it isn't fixed yet, rather than hiding it.

<img src="https://img.shields.io/badge/agents-9%2C_parallel_fan--out-000000?style=flat-square&labelColor=000000&color=3B82F6" alt="9 agents"> <img src="https://img.shields.io/badge/checkpointed-crash--resumes_on_another_worker-000000?style=flat-square&labelColor=000000&color=8B5CF6" alt="checkpointed"> <img src="https://img.shields.io/badge/cost-%240_local%2C_%240.02--0.05%2Fjob_paid-000000?style=flat-square&labelColor=000000&color=EC4899" alt="cost">

</td>
</tr>
<tr>
<td width="40%"><a href="https://github.com/siddharthgaur1/indic-reg-bench"><img src="https://raw.githubusercontent.com/siddharthgaur1/indic-reg-bench/master/docs/social-preview.png" width="100%" alt="indic-reg-bench"></a></td>
<td valign="top">

**[⚖️ indic-reg-bench](https://github.com/siddharthgaur1/indic-reg-bench)** — an open benchmark for Indian regulatory document understanding on SEBI enforcement orders: five tasks, pip-installable harness, [HF dataset](https://huggingface.co/datasets/siddharthgaur/indic-reg-bench). Everything else here is a system I built; this is an instrument others measure *their* systems with.

Hard part: designing tasks a regex can't solve — SEBI orders quote the noticee's own settlement pleas in phrasing identical to the ruling, so the first currency amount in a document is the wrong answer 46.7% of the time.

<img src="https://img.shields.io/badge/orders_indexed-11%2C957-000000?style=flat-square&labelColor=000000&color=3B82F6" alt="orders indexed"> <img src="https://img.shields.io/badge/harness-green_in_CI-000000?style=flat-square&labelColor=000000&color=8B5CF6" alt="CI green"> <img src="https://img.shields.io/badge/leaderboard-deliberately_empty-000000?style=flat-square&labelColor=000000&color=EC4899" alt="no leaderboard yet">

</td>
</tr>
</table>

**Check any of it in a minute:** `pytest --cov=llm_regressor` reprints the coverage figure from a clean clone with no API key; the Elliptic F1 scores read straight out of committed `results/*.json`. Where a number *can't* be reproduced without a paid API key, the README says so instead of quoting one.

<sub>Also worth a look — same bar, not pictured to keep this page short: **[corpgraph-rag](https://github.com/siddharthgaur1/corpgraph-rag)** (GraphRAG with a regex-enforced read-only Neo4j guard), **[elliptic-gatv2-aml](https://github.com/siddharthgaur1/elliptic-gatv2-aml)** (honest negative result: RF 0.8085 beats GATv2 0.4266 illicit-F1), **[ml-platform](https://github.com/siddharthgaur1/ml-platform)** (feature store + drift + fraud scoring, 113 tests), **[query-injection-bench](https://github.com/siddharthgaur1/query-injection-bench)** (found and fixed a critical bypass in my own Cypher guard).</sub>

<p align="center"><img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/divider.svg" alt="" width="100%25" height="20" /></p>

### ▶ Also built, no signup, no API key

<details>
<summary><strong>10 more projects — eval harnesses, RAG, graph sims, IPO forecasting, data-quality monitoring, causal inference, MCP</strong> (click to expand)</summary>
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

<sub>Demos are hosted free on Streamlit Community Cloud; a sleeping app takes ~30–60s to wake. Each also runs locally from its repo's Quickstart with no API key.</sub>

</details>

<p align="center"><img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/divider.svg" alt="" width="100%25" height="20" /></p>

### 🧰 Tech Stack

<p>
<img src="https://img.shields.io/badge/Python-000000?style=flat-square&logo=python&logoColor=3B82F6" alt="Python" />
<img src="https://img.shields.io/badge/SQL-000000?style=flat-square" alt="SQL" />
<img src="https://img.shields.io/badge/LangGraph-000000?style=flat-square" alt="LangGraph" />
<img src="https://img.shields.io/badge/PyTorch-000000?style=flat-square&logo=pytorch&logoColor=EC4899" alt="PyTorch" />
<img src="https://img.shields.io/badge/PyTorch_Geometric-000000?style=flat-square" alt="PyTorch Geometric" />
<img src="https://img.shields.io/badge/scikit--learn-000000?style=flat-square&logo=scikitlearn&logoColor=8B5CF6" alt="scikit-learn" />
<img src="https://img.shields.io/badge/XGBoost-000000?style=flat-square" alt="XGBoost" />
<img src="https://img.shields.io/badge/Neo4j-000000?style=flat-square&logo=neo4j&logoColor=3B82F6" alt="Neo4j" />
<img src="https://img.shields.io/badge/ChromaDB-000000?style=flat-square" alt="ChromaDB" />
<img src="https://img.shields.io/badge/FastAPI-000000?style=flat-square&logo=fastapi&logoColor=EC4899" alt="FastAPI" />
<img src="https://img.shields.io/badge/Docker-000000?style=flat-square&logo=docker&logoColor=8B5CF6" alt="Docker" />
<img src="https://img.shields.io/badge/Kafka-000000?style=flat-square&logo=apachekafka&logoColor=3B82F6" alt="Kafka" />
<img src="https://img.shields.io/badge/Redis-000000?style=flat-square&logo=redis&logoColor=EC4899" alt="Redis" />
<img src="https://img.shields.io/badge/PostgreSQL-000000?style=flat-square&logo=postgresql&logoColor=8B5CF6" alt="PostgreSQL" />
<img src="https://img.shields.io/badge/GitHub_Actions-000000?style=flat-square&logo=githubactions&logoColor=3B82F6" alt="GitHub Actions" />
</p>

<p align="center"><img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/divider.svg" alt="" width="100%25" height="20" /></p>

### 📫 Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/siddharth-gaur-804924293/)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:siddharthgaur200304@gmail.com)

<p align="center">
  <img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/footer.svg" alt="" width="100%" />
</p>
