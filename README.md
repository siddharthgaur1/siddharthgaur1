<p align="center">
  <a href="https://siddharth-gaur.netlify.app">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/hero-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/hero-light.svg">
      <img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/hero-dark.svg" alt="Siddharth Gaur — AI/ML Engineer. Graph neural networks, LLM agents, retrieval systems. Mumbai / remote." width="100%">
    </picture>
  </a>
</p>

<p align="center">
  <a href="https://siddharth-gaur.netlify.app"><img src="https://img.shields.io/badge/Portfolio-0B0F14?style=flat-square&logo=googlechrome&logoColor=FFB627&labelColor=0B0F14" alt="Portfolio"></a>
  <a href="https://www.linkedin.com/in/siddharth-gaur-804924293/"><img src="https://img.shields.io/badge/LinkedIn-0B0F14?style=flat-square&logo=linkedin&logoColor=2DD4BF&labelColor=0B0F14" alt="LinkedIn"></a>
  <a href="mailto:siddharthgaur200304@gmail.com"><img src="https://img.shields.io/badge/Email-0B0F14?style=flat-square&logo=gmail&logoColor=FFB627&labelColor=0B0F14" alt="Email"></a>
</p>

I build systems that have to be **right**, not just impressive — evaluation harnesses, retrieval pipelines, graph models, and the guardrails around them. Every number below is reproducible from a clean clone, and where one *can't* be, the repo says so instead of quoting it.

## Start here

Three projects, each with a measured result rather than a claimed one.

<table>
<tr>
<td width="38%"><a href="https://github.com/siddharthgaur1/openeval"><img src="https://raw.githubusercontent.com/siddharthgaur1/openeval/master/docs/screenshots/eval-runs.png" width="100%" alt="OpenEval"></a></td>
<td valign="top">

### [OpenEval](https://github.com/siddharthgaur1/openeval)

Self-hosted LangSmith alternative: trace every LLM call, version prompts and datasets, run RAG and LLM-judge evals against any provider, block regressions in CI. One `docker compose up`.

**The hard part —** org → project → RBAC with per-project quotas designed in from the first migration. Multi-tenancy retrofits are where authorization bugs live.

**[Live ▶](https://openeval-frontend.onrender.com)** · [API](https://openeval-backend.onrender.com/health) — free tier, first request cold-starts.

<img src="https://img.shields.io/badge/24_built--in_metrics-0B0F14?style=flat-square&labelColor=0B0F14&color=FFB627"> <img src="https://img.shields.io/badge/judge_runs_local_%C2%B7_%240-0B0F14?style=flat-square&labelColor=0B0F14&color=2DD4BF"> <img src="https://img.shields.io/badge/CI_regression_gate-0B0F14?style=flat-square&labelColor=0B0F14&color=94A3B8">

</td>
</tr>
<tr>
<td width="38%"><a href="https://github.com/siddharthgaur1/deepresearch"><img src="https://raw.githubusercontent.com/siddharthgaur1/deepresearch/main/docs/screenshots/04-report.png" width="100%" alt="DeepResearch"></a></td>
<td valign="top">

### [DeepResearch](https://github.com/siddharthgaur1/deepresearch)

Nine-agent LangGraph pipeline: plan sub-questions, search in parallel, cross-check every claim against ≥2 sources, return a cited report with per-claim confidence. Runs end to end on Ollama for $0.

**The hard part —** its own README flags the Docker-socket-mounted sandbox as a real container-escape vector and explains why it isn't fixed yet, rather than hiding it.

<img src="https://img.shields.io/badge/9_agents_%C2%B7_parallel_fan--out-0B0F14?style=flat-square&labelColor=0B0F14&color=FFB627"> <img src="https://img.shields.io/badge/crash--resumes_on_another_worker-0B0F14?style=flat-square&labelColor=0B0F14&color=2DD4BF"> <img src="https://img.shields.io/badge/%240_local_%C2%B7_%240.02--0.05_paid-0B0F14?style=flat-square&labelColor=0B0F14&color=94A3B8">

</td>
</tr>
<tr>
<td width="38%"><a href="https://github.com/siddharthgaur1/indic-reg-bench"><img src="https://raw.githubusercontent.com/siddharthgaur1/indic-reg-bench/master/docs/social-preview.png" width="100%" alt="indic-reg-bench"></a></td>
<td valign="top">

### [indic-reg-bench](https://github.com/siddharthgaur1/indic-reg-bench)

An open benchmark for Indian regulatory document understanding, built on SEBI enforcement orders: five tasks, a pip-installable harness, a [HuggingFace dataset](https://huggingface.co/datasets/siddharthgaur/indic-reg-bench). Everything else here is a system I built; this is an instrument others measure *their* systems with.

**The hard part —** designing tasks a regex can't win. SEBI orders quote the noticee's own settlement pleas in phrasing identical to the ruling, so the first currency amount in a document is the wrong answer 46.7% of the time.

<img src="https://img.shields.io/badge/11%2C957_orders_indexed-0B0F14?style=flat-square&labelColor=0B0F14&color=FFB627"> <img src="https://img.shields.io/badge/harness_green_in_CI-0B0F14?style=flat-square&labelColor=0B0F14&color=2DD4BF"> <img src="https://img.shields.io/badge/leaderboard_deliberately_empty-0B0F14?style=flat-square&labelColor=0B0F14&color=94A3B8">

</td>
</tr>
</table>

## Open source

Maintainer-reviewed work outside my own account. `DenseGATv2Conv` lands directly on the graph work above.

| | PR | Project |
|---|---|---|
| **Merged** | [#1386](https://github.com/jsvine/pdfplumber/pull/1386) — surface the wrapped exception class name in blank `PdfminerException` messages | pdfplumber |
| Open | [#10755](https://github.com/pyg-team/pytorch_geometric/pull/10755) — add `DenseGATv2Conv` | PyTorch Geometric |
| Open | [#10759](https://github.com/pyg-team/pytorch_geometric/pull/10759) — fix `KeyError` in `separate()` for attribute-less heterogeneous node stores | PyTorch Geometric |
| Open | [#10757](https://github.com/pyg-team/pytorch_geometric/pull/10757) — clarify `radius`/`radius_graph` CPU vs. GPU behaviour in docs | PyTorch Geometric |
| Open | [#10761](https://github.com/pyg-team/pytorch_geometric/pull/10761) — add Shapes docstrings to `TransformerConv`/`SplineConv` | PyTorch Geometric |

## Where I don't round up

- **[elliptic-gatv2-aml](https://github.com/siddharthgaur1/elliptic-gatv2-aml)** — a published negative result: Random Forest (0.8085 illicit-F1) beats my GATv2 (0.4266). The finding *is* that the fancy model lost.
- **[query-injection-bench](https://github.com/siddharthgaur1/query-injection-bench)** — found and fixed a critical read-only bypass in my *own* Cypher guard, then measured it.
- **[recruit-voice-agent](https://github.com/siddharthgaur1/recruit-voice-agent)** — the results doc separates fill rate from accuracy, names the latency target it **missed**, and labels every unrun measurement as unrun.

<details>
<summary><b>10 more projects</b> — eval harnesses, RAG, graph sims, causal inference, MCP, data-quality monitoring <i>(click to expand)</i></summary>
<br>

| Project | What it does | Demo |
|---|---|---|
| **[llm-regressor](https://github.com/siddharthgaur1/llm-regressor)** | *The library + CI gate.* Model-agnostic regression testing for prompt and model changes; a reusable GitHub Action gates a PR in five lines. 100% statement and branch coverage, ~2s with no API key | — |
| **[querypilot-v2](https://github.com/siddharthgaur1/querypilot-v2)** | English → SQL with schema-aware RAG (retrieves the 3 relevant table chunks, not a full schema dump). Write-safety is a SQLite `PRAGMA query_only` + authorizer at the DB layer, so a prompt injection that beats every earlier check still can't write | — |
| **[autonomous-data-scientist](https://github.com/siddharthgaur1/autonomous-data-scientist)** | Give it a CSV and *"predict churn"* — an 11-agent pipeline cleans, explores, engineers features, tunes, evaluates, ships a report. Generated pandas runs through an AST whitelist into a locked-down subprocess (import guard, path guard, rlimits, wall-clock kill). 80 tests | — |
| **[Sebi-Explorer](https://github.com/siddharthgaur1/Sebi-Explorer)** | Analytics over real public SEBI enforcement orders: violation classification, penalties, entity network, timeline — the corpus problem that motivated `indic-reg-bench` | [▶](https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/) |
| **[rail-graph](https://github.com/siddharthgaur1/rail-graph)** | Graph analysis of a synthetic 600-station Indian rail network — PageRank, betweenness, k-shortest paths, resilience simulation. The sim re-runs betweenness per removed node, so the naive version never finishes | [▶](https://siddharthgaur1-siddharthrail-graph-srcapp-hme3vr.streamlit.app/) |
| **[nse-daily-monitor](https://github.com/siddharthgaur1/nse-daily-monitor)** | Scheduled data-quality monitoring of the NSE bhavcopy — coverage, OHLC bounds, null rates and breadth against a trailing 60-day baseline, opening a GitHub issue when a check fails. Publishes derived metrics only, never a reconstructable quote | [▶ runs](https://github.com/siddharthgaur1/nse-daily-monitor/actions) |
| **[causal-lens](https://github.com/siddharthgaur1/causal-lens)** | Four independently usable methods for *"did this intervention actually cause this outcome"* — A/B testing (frequentist + Bayesian + CUPED), difference-in-differences, synthetic control, uplift modelling | — |
| **[indian-markets-mcp](https://github.com/siddharthgaur1/indian-markets-mcp)** | MCP server exposing Indian market and regulatory data from official sources only. `latest_day()` resolves against IST, not the host clock, so a UTC-hosted server doesn't report yesterday's close as today's every evening | — |

<sub><b>About the demos:</b> they run on Streamlit's free tier, so an idle app first shows a <i>"Zzzz — wake it up?"</i> button; one click and roughly 40 seconds brings it back. Every one also runs locally from its repo's Quickstart with no API key.</sub>


<sub>▶ demos are on free tiers and sleep when idle — the first click wakes them, which takes about a minute.</sub>

</details>

## Stack

`Python` · `PyTorch` · `PyTorch Geometric` · `LangGraph` · `scikit-learn` · `XGBoost` · `FastAPI` · `Neo4j` · `PostgreSQL` · `Redis` · `Kafka` · `ChromaDB` · `Docker` · `GitHub Actions`

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/rule-dark.svg">
    <img src="https://raw.githubusercontent.com/siddharthgaur1/siddharthgaur1/main/assets/rule-light.svg" alt="" width="100%">
  </picture>
</p>

<p align="center">
  <b>Open to AI/ML roles — Mumbai or remote.</b><br>
  <a href="mailto:siddharthgaur200304@gmail.com">siddharthgaur200304@gmail.com</a> ·
  <a href="https://www.linkedin.com/in/siddharth-gaur-804924293/">LinkedIn</a> ·
  <a href="https://siddharth-gaur.netlify.app">Portfolio</a>
</p>
