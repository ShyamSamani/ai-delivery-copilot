# AI Delivery Copilot — Roadmap

## What this is

A question-answering system over the documents and data of a project, built end to end: retrieval, tools, agent orchestration, evaluation, deployment.

The project it answers questions about is fictional. **Project Phoenix** is a customer service transformation — a company replacing an ageing case management platform with a cloud system and an AI knowledge assistant. It has a charter, weekly status reports, a risk register, action and decision logs, meeting minutes, milestones, a budget, and a team directory. You write all of it.

The data is fictional so you can control it: make it clean, then deliberately break it, and see exactly how your system copes.

## What it will do

Roughly in the order you'll build it.

| Question | What it forces you to build |
|---|---|
| "What's in scope for Project Phoenix?" | Basic retrieval — find the right chunk, answer from it |
| "Why is testing amber this week?" | Multi-document synthesis — status report → linked risk → meeting note |
| "Which high-severity risks threaten the October launch?" | Metadata filtering — severity and date are fields, not text |
| "What's the budget variance on the migration workstream?" | Tool use — arithmetic over structured data, not retrieval |
| "What changed since last week's report?" | Temporal reasoning and document recency |
| "Draft next week's status report" | Multi-step generation from many sources |
| "What did we decide about the supplier contract?" | Refusing to answer when the data doesn't support one |
| "What's the risk exposure and who owns it?" *(as a follow-up)* | Conversation memory and query rewriting |

The refusal case matters as much as any of the others. A system that confidently invents a decision is worse than no system.

## Why this project suits you

You know delivery. That means you can judge whether an answer is actually correct, which is the hardest part of building these systems and the part you can't do in an unfamiliar domain. Most people learn RAG over Wikipedia and have no idea whether it's working.

Delivery data is also usefully awkward: prose and tables mixed, dates that matter, owners, cross-references between documents, and information that goes stale. That awkwardness is what pushes you into the real problems rather than the tutorial ones.

---

# Tech and tools

Grouped by what they're for, with why each is here.

### Language and environment
| Tool | What it is | Why |
|---|---|---|
| **Python 3.12** | The language | Everything in this ecosystem is Python |
| **venv** | Isolated per-project Python | Stops projects breaking each other |
| **pip / requirements.txt** | Dependency management | Reproducible installs |
| **VS Code** | Editor | Debugger, terminal, Git panel, extensions |
| **pyproject.toml** | Project config | Tool settings in one standard place |

### Version control and CI/CD
| Tool | What it is | Why |
|---|---|---|
| **Git** | Version control | Non-negotiable for any real work |
| **GitHub** | Hosting and collaboration | Your portfolio lives here |
| **GitHub Actions** | CI/CD automation | Runs tests and deploys on every push |
| **Branching / PRs** | Workflow discipline | How teams actually work |

### Code quality
| Tool | What it is | Why |
|---|---|---|
| **pytest** | Test framework | Catches regressions as the system grows |
| **ruff** | Linter and formatter | Fast, catches bugs and style issues |
| **Type hints** | Optional static typing | Makes intent explicit, helps the editor help you |
| **pydantic** | Data validation via types | Enforces the shape of LLM outputs and config |

### Interface
| Tool | What it is | Why |
|---|---|---|
| **Streamlit** | Python web apps | A UI in a few lines, no frontend skills needed |
| **Streamlit Community Cloud** | Free hosting | Deploys from GitHub, redeploys on push |

### The models
| Tool | What it is | Why |
|---|---|---|
| **Ollama** | Runs LLMs locally | Free, private, no API bills while you experiment |
| **Llama 3.2 3B / Qwen2.5 3B** | Small open models | Run on a normal laptop |
| **Hugging Face Hub** | Model and dataset registry | Where open models live |
| **HF Inference Providers / Groq** | Hosted inference, free tiers | Your deployed app can't reach your laptop |
| **transformers** | HF model library | Understanding what's under the abstraction |

### Retrieval
| Tool | What it is | Why |
|---|---|---|
| **Embeddings** (bge-small, MiniLM) | Text as vectors | The foundation of semantic search |
| **sentence-transformers / fastembed** | Embedding libraries | fastembed is lighter — matters on free hosting |
| **FAISS** | Vector index | Fast, local, no server |
| **Chroma** | Vector database | Adds metadata filtering and persistence |
| **rank_bm25** | Keyword search | Catches exact terms like "RISK-004" that embeddings miss |
| **Cross-encoder reranking** | Second-pass scoring | Large accuracy gain for modest cost |

### Orchestration
| Tool | What it is | Why |
|---|---|---|
| **LangChain** | LLM application framework | Standard components, huge ecosystem |
| **LangGraph** | Stateful agent graphs | Loops, branching, retries, human-in-the-loop |
| **Function / tool calling** | Models invoking your code | How an LLM does arithmetic and queries data |
| **MCP** | Model Context Protocol | Standard way to expose data and tools to any AI client |

### Data
| Tool | What it is | Why |
|---|---|---|
| **pandas** | Tabular data | Risks, actions, budget, milestones |
| **Markdown / CSV / JSON** | Your source formats | Realistic mix of unstructured and structured |

### Evaluation and observability
| Tool | What it is | Why |
|---|---|---|
| **Custom eval harness** | Your questions and expected facts | The thing that tells you if changes helped |
| **ragas** | RAG-specific metrics | Faithfulness, relevance, context precision |
| **LangSmith** | Tracing and evaluation | See every step of every run; free developer tier |

### Production
| Tool | What it is | Why |
|---|---|---|
| **Docker** | Containers | Same environment everywhere |
| **Environment variables / secrets** | Config handling | Never commit an API key |
| **Caching** | Reuse of expensive results | Cuts latency and cost |
| **Guardrails** | Input and output checks | Injection, PII, refusal behaviour |

### Optional, later
| Tool | What it is | Why |
|---|---|---|
| **PEFT / LoRA** | Efficient fine-tuning | Worth understanding conceptually; rarely the right answer |
| **Hugging Face Spaces** | Alternative hosting | Free tier has been unstable through 2026 — check before relying on it |

---

# Stages

Timings assume 6–8 hours a week. They're a guide, not a target. Every stage ends with something working and deployed.

## Stage 0 — Walking skeleton
**Week 1**

Repo, virtual environment, empty Streamlit app, unit tests, GitHub Actions, live URL.

*Learn:* Python project structure, Git, GitHub, pytest, ruff, CI, cloud deployment.

**Done when:** pushing a commit runs your tests and updates a public URL without you doing anything.

## Stage 1 — The dataset
**Week 2**

Write the twelve Project Phoenix files. Build a loader. Write tests that validate the data — every risk has an owner, every action has a due date, every referenced ID exists.

Design the cross-document chains deliberately. RISK-004 (UAT environment delay) → meeting note confirming five days → status report showing Testing as Amber → ACTION-021 overdue. Build three or four chains like that. They become your hardest test cases.

*Learn:* pandas, data modelling, pydantic validation, meaningful tests.

**Done when:** CI fails if you commit a broken risk register.

## Stage 2 — Talking to a model
**Week 3**

Ollama installed. First completion from Python. Prompting properly. Getting structured JSON out reliably instead of prose. Handling the times it doesn't.

*Learn:* tokens, context windows, temperature, system vs user messages, structured output, why hallucination happens.

**Done when:** your app takes a question and returns a model-generated answer — wrong, but real.

## Stage 3 — First RAG
**Weeks 4–5**

Chunk the documents. Embed them. Store the vectors in FAISS. Retrieve the top matches. Put them in the prompt. Answer with citations.

*Learn:* embeddings, similarity, chunk size and overlap, the retrieve-augment-generate loop, prompt construction.

**Done when:** "What's in scope for Project Phoenix?" gets a correct, cited answer. This is the milestone worth aiming for around week six.

## Stage 4 — Retrieval that actually works
**Weeks 6–7**

Your first version will fail in specific ways. Fix them. Better chunking. Hybrid search so "RISK-004" matches literally. Reranking. Metadata on every chunk — document type, date, workstream.

*Learn:* chunking strategies, BM25, hybrid fusion, cross-encoders, metadata filtering, and above all **diagnosing retrieval failure** — the answer was there and you didn't find it.

**Done when:** "Why is testing amber?" pulls evidence from three different documents.

## Stage 5 — Evaluation
**Week 8**

Build the eval harness now, not at the end. Twenty to thirty questions with expected facts. Measure retrieval separately from answer quality. Run it in CI.

Deliberately introduce contradictory and outdated documents into the dataset and watch your scores drop.

*Learn:* retrieval metrics, faithfulness, ragas, LangSmith tracing, regression testing for non-deterministic systems.

**Done when:** you can change a chunking parameter and get a number telling you whether it helped. This stage is what separates engineering from guessing.

## Stage 6 — Tools
**Weeks 9–10**

Some questions can't be answered by retrieval. Budget variance needs arithmetic. "All risks owned by Sarah" needs a query. Give the model functions and let it decide when to call them.

*Learn:* function calling, tool schemas, argument validation, routing between retrieval and tools, failure handling.

**Done when:** "What's the budget variance on migration?" returns a correct calculated figure.

## Stage 7 — Agents and LangGraph
**Weeks 11–13**

Move from a fixed pipeline to a graph. Classify the question, route it, gather evidence, possibly loop, then answer. Handle multi-part questions.

*Learn:* LangGraph nodes, edges and state, conditional routing, loop limits, why agents fail and how to constrain them.

**Done when:** "Draft next week's status report" produces something plausible from multiple sources.

## Stage 8 — Memory and self-correcting retrieval
**Weeks 14–16**

Conversation history and follow-up questions. Query rewriting so "and who owns it?" makes sense. Agentic RAG — the system grades its own retrieval and tries a different query when the results are weak.

Expand the dataset. More documents, more conflicts, more staleness.

*Learn:* memory strategies, context management, query transformation, self-reflection loops, handling conflicting sources.

**Done when:** a three-turn conversation works, and the system says "the documents disagree" instead of picking one at random.

## Stage 9 — MCP
**Weeks 17–18**

Wrap your Project Phoenix data and tools in an MCP server so any MCP-capable client can query it.

*Learn:* the protocol, resources vs tools vs prompts, server design, why standard interfaces matter.

**Done when:** an external client can ask your server about Project Phoenix. This is the most current and least widely understood piece in the whole roadmap.

## Stage 10 — Production concerns
**Weeks 19–20**

Observability, cost and latency, caching, guardrails, prompt injection, graceful degradation, structured logging.

*Learn:* what it takes to run this for real rather than demo it.

**Done when:** you can show a trace of any request and explain what it cost and how long it took.

## Stage 11 — Containers and deployment
**Weeks 21–22**

Dockerise. Multi-stage builds. Build the image in CI. Deploy the container properly.

*Learn:* Docker, image layers, secrets in containers, deployment pipelines.

**Done when:** `docker run` starts the whole system on any machine.

## Stage 12 — Polish, and optionally fine-tuning
**Weeks 23–24**

A real README with architecture diagrams. A demo video. Documented eval results.

If you want, a small LoRA fine-tune on an open model — mainly so you can explain when fine-tuning is and isn't the right tool. Usually it isn't; retrieval solves more problems more cheaply.

**Done when:** someone can read your repo and understand the system without you explaining it.

---

# Dataset progression

The dataset gets deliberately worse over time. Each degradation forces the next capability.

| Version | What changes | What it forces |
|---|---|---|
| v1 | Clean, consistent, 12 files | Basic RAG |
| v2 | Conflicts and outdated documents | Metadata, dates, recency logic |
| v3 | More documents, richer metadata | Filtering, better retrieval |
| v4 | Structured CSVs alongside prose | Tool use |
| v5 | Questions requiring computation and multi-hop reasoning | Agents |

---

# What you'll be able to say at the end

Not "I've heard of RAG" but: *I built a system that answers questions over a document corpus, measured its accuracy, found where retrieval failed and fixed it, added tools for the questions retrieval couldn't handle, orchestrated it as an agent graph, exposed it over MCP, containerised it, and shipped it through a CI pipeline.*

With a public repo and a live URL to back it up.

---

# Two honest notes

**Frameworks churn.** LangChain and LangGraph change fast, and what's idiomatic now may not be in two years. The durable skills here are retrieval, evaluation, and engineering discipline. The frameworks are the current vehicle, not the destination.

**Don't rush.** An hour most evenings plus a longer weekend session beats a twenty-hour week you forget. Every stage ends with something working, so you always have something to show — and something to come back to.
