# Hi, I'm Siddharth 👋

[🌐 siddharth-gaur.netlify.app](https://siddharth-gaur.netlify.app)

**AI/ML Engineer** · Building at the intersection of **graph neural networks**, **LLM agents**, and **retrieval systems**

---

### 🔬 Research

**GNN-based root cause analysis for network topologies** — two working prototypes:

- **Transductive** — localises root causes within a single fixed topology.
- **Inductive** — trained across multiple topologies, generalises to a **previously unseen topology** at inference, so a new network doesn't need a retrained model.

*(Prototypes; not yet published — happy to walk through the approach.)*

---

### 🔨 What I Build

**LLM agents & multi-agent systems**

| Project | What it does | Stack |
|---|---|---|
| [🤖 Autonomous Data Scientist](https://github.com/siddharthgaur1/autonomous-data-scientist) | Give it a CSV and *"predict churn"* — it cleans the data, engineers features, tunes the winning model, evaluates it honestly, and ships a model card and slide deck. Generated code runs in a locked-down sandbox | LangGraph · OpenAI · FastAPI · Redis |
| [⚖️ Research + Debate Agent](https://github.com/siddharthgaur1/research-debate-agent) | Agents research in parallel, argue both sides, audit their own sources for bias, and arbitrate into a report where every claim carries a citation and a confidence score | LangGraph · OpenAI · ChromaDB · FastAPI |
| [🏦 Credit Memo Agent](https://github.com/siddharthgaur1/credit-memo-agent) | Drafts a business loan credit memo: checklist gaps, financials extracted with a source page and row label on every figure, ratios computed in Python rather than by the model. A balance sheet that doesn't balance is a finding, not a silent correction. Runs fully offline on Ollama — the cloud path is opt-in and can't activate by accident | LangGraph · Ollama · pdfplumber · FastAPI |
| [🕸️ Text-to-Graph Agent](https://github.com/siddharthgaur1/text-to-graph-agent) | Natural language → executed Cypher over a knowledge graph. A wrong relationship direction doesn't throw, it returns an empty set that reads as "no data" — so entities resolve to node identities first, hops are planned, and a validator binds parameters and injects a LIMIT before anything runs | LangGraph · Neo4j · ChromaDB · FastAPI |

**Retrieval & RAG**

| Project | What it does | Stack |
|---|---|---|
| [🔎 RAG Hybrid Search](https://github.com/siddharthgaur1/rag-hybrid-search) | Dense + BM25 retrieval fused with Reciprocal Rank Fusion, a cross-encoder reranker on top, and an LLM-as-judge that catches hallucinated citations before they reach the user | ChromaDB · BM25 · cross-encoder · FastAPI |
| [📊 FinRAG](https://github.com/siddharthgaur1/finrag) | RAG over long, dense financial PDFs (annual reports, RBI circulars) — hybrid retrieval plus a faithfulness check on every answer | ChromaDB · MiniLM · Claude / Ollama |

**AI engineering & evaluation**

| Project | What it does | Stack |
|---|---|---|
| [🧪 Agent Eval Harness](https://github.com/siddharthgaur1/agent-eval-harness) | Scores multi-step agent *trajectories*, not prompt/response pairs: right tools, right order, recovered from failures, stayed in budget — and did anything the agent actually did justify the answer it gave? Catches the fluent final report quoting a metric no tool in the run ever produced. Every score cites the step indices it rests on | OpenAI · Pydantic · FastAPI · pytest |
| [🚦 LLM Regression Detector](https://github.com/siddharthgaur1/llm-regression-detector) | Prompts drift silently. A CI harness that runs a golden dataset through every prompt change, scores it, and alerts on regressions before they ship | OpenAI · pytest · GitHub Actions |
| [🧭 QueryPilot](https://github.com/siddharthgaur1/querypilot) | Natural language → SQL against a live introspected schema, with three layered safety checks (blocklist, prefix check, read-only engine) so a bypass at one layer still fails safe | Claude / Ollama · SQLite · Streamlit |

**Applied ML & data**

| Project | What it does | Stack |
|---|---|---|
| [⚖️ SEBI Enforcement Explorer](https://github.com/siddharthgaur1/sebi-explorer) | Turns SEBI's unstructured HTML order listing (~11k orders) into a searchable dataset — violation classification, entity extraction, and pattern analytics | BeautifulSoup · NetworkX · Streamlit · Plotly |
| [🚂 RailGraph](https://github.com/siddharthgaur1/rail-graph) | Treats India's rail network as a graph rather than a timetable: PageRank for station importance, betweenness to find the junctions whose failure disrupts the most traffic | NetworkX · Folium · Plotly |
| [📈 IPO GMP Predictor](https://github.com/siddharthgaur1/ipo-gmp) | Models IPO listing-day returns from Grey Market Premium and subscription signals, using time-series CV to avoid leaking future market regimes *(synthetic dataset — demonstrates the pipeline, not validated on real markets)* | XGBoost · scikit-learn · Streamlit |

---

### 🧰 Tech Stack

**Languages**  
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://python.org) [![SQL](https://img.shields.io/badge/SQL-003B57?logo=postgresql&logoColor=white)](https://www.postgresql.org) [![Java](https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=white)](https://openjdk.org)

**LLMs / Agents / RAG**  
[![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?logo=langchain&logoColor=white)](https://langchain-ai.github.io/langgraph/) [![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)](https://openai.com) [![Anthropic](https://img.shields.io/badge/Anthropic_Claude-blueviolet)](https://anthropic.com) [![ChromaDB](https://img.shields.io/badge/ChromaDB-purple)](https://trychroma.com) [![Ollama](https://img.shields.io/badge/Ollama-local_LLM-black)](https://ollama.ai)

**ML / Graph**  
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org) [![PyG](https://img.shields.io/badge/PyG-GNN-blueviolet)](https://pyg.org) [![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org) [![XGBoost](https://img.shields.io/badge/XGBoost-orange)](https://xgboost.ai) [![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org) [![NetworkX](https://img.shields.io/badge/NetworkX-2C7FB8)](https://networkx.org)

**Infrastructure**  
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com) [![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://docker.com) [![Redis](https://img.shields.io/badge/Redis-DC382D?logo=redis&logoColor=white)](https://redis.io) [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io) [![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions) [![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)](https://sqlite.org) [![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com)

---

### 📌 Open Source

Proposed a fix for [**Textualize/rich**](https://github.com/Textualize/rich) (56k ⭐) — `CONTRIBUTING.md` still tells new contributors to run `poetry shell`, which Poetry removed in 2.0, so setup fails at step one. Fix posted on [#3817](https://github.com/Textualize/rich/issues/3817), documenting the officially recommended `eval $(poetry env activate)`.

---

### 📫 Connect

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/siddharth-gaur-804924293/)
[![Email](https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white)](mailto:siddharthgaur200304@gmail.com)
