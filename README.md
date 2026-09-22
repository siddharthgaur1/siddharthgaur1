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

I build systems that have to be **right**, not just impressive — eval harnesses, retrieval pipelines, graph models, and the guardrails around them. Every number here is reproducible from a clean clone; where one isn't, the repo says so.

## Start here

<table>
<tr>
<td width="33%"><a href="https://github.com/siddharthgaur1/openeval"><img src="https://raw.githubusercontent.com/siddharthgaur1/openeval/master/docs/screenshots/eval-runs.png" alt="OpenEval"></a></td>
<td width="33%"><a href="https://github.com/siddharthgaur1/deepresearch"><img src="https://raw.githubusercontent.com/siddharthgaur1/deepresearch/main/docs/screenshots/04-report.png" alt="DeepResearch"></a></td>
<td width="33%"><a href="https://github.com/siddharthgaur1/indic-reg-bench"><img src="https://raw.githubusercontent.com/siddharthgaur1/indic-reg-bench/master/docs/social-preview.png" alt="indic-reg-bench"></a></td>
</tr>
<tr valign="top">
<td>

**[OpenEval](https://github.com/siddharthgaur1/openeval)** · [live ▶](https://openeval-frontend.onrender.com)

Self-hosted LangSmith alternative. 24 built-in evaluators, CI regression gate, one `docker compose up`. Org → project → RBAC designed in from the first migration, because multi-tenancy retrofits are where authorization bugs live.

</td>
<td>

**[DeepResearch](https://github.com/siddharthgaur1/deepresearch)**

Nine LangGraph agents: plan sub-questions, search in parallel, cross-check every claim against ≥2 sources, return a cited report. Crash-resumes on another worker. Runs end to end on Ollama for $0.

</td>
<td>

**[indic-reg-bench](https://github.com/siddharthgaur1/indic-reg-bench)**

Open benchmark on 11,957 SEBI enforcement orders, plus a [HF dataset](https://huggingface.co/datasets/siddharthgaur/indic-reg-bench). Tasks a regex can't win — the first currency amount in an order is the wrong answer 46.7% of the time.

</td>
</tr>
</table>

## Open source

**4 merged, 6 under review** in other people's projects — [MLflow](https://github.com/mlflow/mlflow/pull/25713) (a Windows checkout shipped a wheel with zero Python files), [Great Expectations](https://github.com/fivetran/great_expectations/pull/12168) [×2](https://github.com/fivetran/great_expectations/pull/12169) (undefined SQLite stddev, mypy coverage), [pdfplumber](https://github.com/jsvine/pdfplumber/pull/1386) (blank exception messages). Under review: a [`DenseGATv2Conv`](https://github.com/pyg-team/pytorch_geometric/pull/10755) layer for PyTorch Geometric, a [pdfplumber cache fix](https://github.com/jsvine/pdfplumber/pull/1397) (105 MB → 4.8 MB on a 65-page PDF), and [four more](https://github.com/pulls?q=is%3Apr+is%3Aopen+author%3Asiddharthgaur1+-user%3Asiddharthgaur1).

Plus bugs found by probing libraries I use, reported with a reproduction: [langgraph #8672](https://github.com/langchain-ai/langgraph/issues/8672), [chroma #7735](https://github.com/chroma-core/chroma/issues/7735).

## Where I don't round up

- **[elliptic-gatv2-aml](https://github.com/siddharthgaur1/elliptic-gatv2-aml)** — a published negative result: Random Forest (0.8085 illicit-F1) beats my GATv2 (0.4266). The finding *is* that the fancy model lost.
- **[query-injection-bench](https://github.com/siddharthgaur1/query-injection-bench)** — 226 attack cases that found a critical read-only bypass in my *own* Cypher guard, then measured the fix.
- **[recruit-voice-agent](https://github.com/siddharthgaur1/recruit-voice-agent)** — the results doc separates fill rate from accuracy, names the latency target it **missed**, and labels every unrun measurement as unrun.

<details>
<summary><b>10 more projects</b> — eval tooling, RAG, knowledge graphs, ML platforms, causal inference, MCP</summary>

| Project | What it does |
|---|---|
| **[llm-regressor](https://github.com/siddharthgaur1/llm-regressor)** | Regression testing for prompt and model changes; a reusable Action gates a PR in five lines. 100% branch coverage, ~2s, no API key |
| **[querypilot-v2](https://github.com/siddharthgaur1/querypilot-v2)** | English → SQL with schema-aware RAG. Write-safety is `PRAGMA query_only` plus an authorizer at the DB layer, so an injection that beats every earlier check still can't write |
| **[corpgraph-rag](https://github.com/siddharthgaur1/corpgraph-rag)** | Indian corporate network in Neo4j — GraphRAG question answering plus a GATv2 link predictor for relationships the filings don't state |
| **[ml-platform](https://github.com/siddharthgaur1/ml-platform)** | Feature store, drift monitor and real-time fraud scoring merged so the train/serve seams are real imports, not duck-typed adapters. 113 tests |
| **[autonomous-data-scientist](https://github.com/siddharthgaur1/autonomous-data-scientist)** | A CSV and *"predict churn"* → 11 agents clean, tune, evaluate and report. Generated pandas runs through an AST whitelist into a locked-down subprocess |
| **[causal-lens](https://github.com/siddharthgaur1/causal-lens)** | A/B testing (frequentist + Bayesian + CUPED), difference-in-differences, synthetic control, uplift modelling |
| **[indian-markets-mcp](https://github.com/siddharthgaur1/indian-markets-mcp)** | MCP server, 8 tools, official sources only. Resolves the latest trading day against IST, so a UTC host doesn't report yesterday's close |
| **[nse-daily-monitor](https://github.com/siddharthgaur1/nse-daily-monitor)** | Daily NSE bhavcopy checks against a trailing 60-day baseline, opening an issue when one fails. Derived metrics only, never a reconstructable quote |
| **[Sebi-Explorer](https://github.com/siddharthgaur1/Sebi-Explorer)** · [▶](https://siddharthgaur1-siddharthsebi-explorer-srcapp-kputga.streamlit.app/) | Analytics over real public SEBI enforcement orders — the corpus problem that motivated `indic-reg-bench` |
| **[rail-graph](https://github.com/siddharthgaur1/rail-graph)** · [▶](https://siddharthgaur1-siddharthrail-graph-srcapp-hme3vr.streamlit.app/) | A 600-station rail network as a graph: PageRank, betweenness, k-shortest paths, resilience simulation |

<sub>Demos run on free tiers, so an idle app first shows a wake button and takes ~40 seconds. Every one also runs locally from its repo's Quickstart with no API key.</sub>

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
