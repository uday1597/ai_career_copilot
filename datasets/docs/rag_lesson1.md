# Lesson 1 — What is RAG?

When we finish this section, you'll understand how systems like **ChatGPT with files, Microsoft Copilot, Notion AI, Perplexity, Glean, Cursor, Claude Projects**, and many enterprise AI assistants work.

---

# What is RAG?

RAG stands for **Retrieval-Augmented Generation**.

Let's break it down.

## Traditional LLM

You ask GPT:

> What is LangGraph?

GPT answers from what it learned during training.

```
User
   │
   ▼
GPT
   │
   ▼
Answer
```

### Problem

GPT **doesn't know your private data**.

It doesn't know:

- Your resume
- Your learning roadmap
- Your assessments
- Your PDFs
- Your company documentation
- Your personal notes

Unless you paste them into the prompt every time.

---

# RAG changes this

With RAG the flow becomes:

```
User
   │
   ▼
Retriever
   │
Find relevant information
   │
   ▼
GPT
   │
   ▼
Answer
```

GPT still generates the answer.

The **Retriever** simply gives GPT the right information.

---

# Example

Suppose your knowledge base contains:

```
Azure AI Search Notes

Page 1

Azure AI Search is Microsoft's managed search service...
```

You ask:

> Explain Azure AI Search.

Instead of guessing,

the system first searches the knowledge base.

It finds:

```
Azure AI Search is Microsoft's managed search service...
```

Then sends GPT:

```
Context

Azure AI Search is Microsoft's managed search service...

Question

Explain Azure AI Search.
```

GPT answers using **your notes**.

---

# Think of it like an Open Book Exam

Without RAG

```
Teacher

↓

Student Memory

↓

Answer
```

With RAG

```
Teacher

↓

Open Book

↓

Student

↓

Answer
```

GPT is still the student.

RAG gives it the book.

---

# Why not just send the whole PDF?

Imagine your Kubernetes PDF has

**500 pages.**

GPT has context window limits.

Even if it fits,

it becomes

- Slower
- More expensive
- Less accurate

Instead, RAG sends only:

```
2–5 relevant paragraphs.
```

That's the magic of retrieval.

---

# The Four Stages of RAG

Every RAG system follows these four stages.

---

## 1. Ingestion

Take documents:

```
Resume.pdf

Docker.pdf

Azure.pdf

Interview.pdf
```

↓

Extract text.

---

## 2. Chunking

Never embed an entire document.

Instead:

```
Docker Guide

↓

Chunk 1

Chunk 2

Chunk 3

Chunk 4

...
```

Think of chunks as paragraphs.

---

## 3. Embeddings

Every chunk becomes numbers.

Example:

```
"What is Docker?"

↓

[0.19,
-0.32,
0.55,
...
1536 values]
```

These numbers represent **meaning**, not words.

---

## 4. Retrieval

Question:

```
Explain Docker volumes.
```

↓

Embedding

↓

Find closest chunk

↓

Send to GPT

↓

Answer

---

# The Heart of RAG: Embeddings

This is the most important concept.

GPT cannot compare sentences directly.

Instead, it converts text into vectors.

Example:

```
Docker

↓

[0.17,
0.91,
-0.42,
...]
```

Azure

↓

```
[0.65,
-0.12,
0.28,
...]
```

These vectors live in a mathematical space.

Similar meanings end up close together.

---

Imagine a map.

```
Docker

       Kubernetes

             Containers



Azure AI

         OpenAI

              GPT



Cats

Dogs

Animals
```

Similar topics naturally cluster together.

When you ask:

> Explain containers

Your question embedding lands near:

```
Docker

Kubernetes

Containers
```

Those chunks are retrieved.

---

# Why Embeddings Are Amazing

### Keyword Search

Search:

```
automobile
```

Document:

```
car
```

No match.

---

### Embedding Search

Search:

```
automobile
```

Document:

```
car
```

Similarity:

```
99%
```

Because they mean the same thing.

This is called **Semantic Search**.

---

# Career Copilot Example

Imagine your knowledge base contains:

```
Resume

Roadmap

Assessments

Azure Notes

Docker Notes

Kubernetes Notes

Interview Questions

Personal Notes
```

User asks:

> What should I revise before my interview?

Retriever finds:

```
Week 6 Kubernetes

Assessment Week 6 Feedback

Docker Notes

Resume Missing Skills
```

GPT combines all of them into one answer.

Notice:

GPT didn't magically know the answer.

The Retriever selected the right context.

---

# Where Does pgvector Fit?

A relational database stores:

```
ID

Title

Content
```

pgvector additionally stores:

```
Embedding

[0.18,
0.44,
...]
```

Then SQL can perform:

```sql
ORDER BY embedding <=> query_embedding
```

and return:

> The 5 most similar chunks.

This is semantic search inside PostgreSQL.

---

# Our Implementation Roadmap

We'll build exactly this architecture:

```
PDF

↓

Extract Text

↓

Chunk

↓

Embedding

↓

PostgreSQL (pgvector)

↓

Similarity Search

↓

GPT-5

↓

Answer
```

This is a production-quality architecture that can later be extended with:

- Metadata filtering
- Hybrid Search
- Re-ranking
- Context Compression
- Multi-document Retrieval

---

# Key Takeaways

- **RAG = Retrieval + Generation**
- GPT generates the answer.
- The Retriever finds relevant information.
- Documents are split into chunks.
- Chunks are converted into embeddings.
- Embeddings capture semantic meaning.
- pgvector stores embeddings in PostgreSQL.
- Similarity search finds the most relevant chunks.
- GPT answers using retrieved context instead of guessing.

---

# Summary Flow

```
User Question
       │
       ▼
Embed Question
       │
       ▼
Vector Search
       │
       ▼
Top K Chunks
       │
       ▼
Prompt + Context
       │
       ▼
GPT-5
       │
       ▼
Answer
```

---

# Next Lesson

In the next lesson we'll build the database layer by creating a **KnowledgeDocument** table that stores:

- Document metadata
- Text chunks
- Embeddings
- Source information

This will become the foundation of our RAG system.



# Lesson 2 — Building a Production RAG System

In Lesson 1, we learned the theory behind RAG.

In this lesson, we implement it step by step and gradually evolve it into an enterprise-grade Retrieval-Augmented Generation system.

The goal was **not** to build the most advanced system immediately, but to understand why each improvement exists and what problem it solves.

---

# Stage 1 — Knowledge Base

## Step 1 — KnowledgeDocument

We first created a `KnowledgeDocument` table.

Instead of storing only files, we store **searchable knowledge**.

Each record contains:

* Content
* Document Type
* Source
* Metadata
* Embedding Vector

This becomes the central knowledge base for our AI assistant.

---

## Step 2 — Chunking

Large documents should never be embedded as a whole.

Instead,

```
PDF

↓

Chunk 1

Chunk 2

Chunk 3

...

Chunk N
```

Each chunk represents a small logical section.

### Why?

Smaller chunks produce:

* Better embeddings
* Better retrieval
* Better answers

Chunking is one of the most important design decisions in every RAG system.

---

## Step 3 — Embeddings

Each chunk is converted into a vector using OpenAI Embeddings.

```
Chunk

↓

Embedding Model

↓

1536-Dimensional Vector
```

The vector represents the meaning of the text.

Instead of matching words,

the database matches meanings.

---

## Step 4 — Store in pgvector

Each chunk and its embedding are stored inside PostgreSQL.

```
Chunk

+

Embedding

↓

KnowledgeDocument
```

Now PostgreSQL becomes a semantic search engine.

---

# Stage 2 — Semantic Search

When the user asks a question,

```
Question

↓

Embedding

↓

Vector Search

↓

Most Similar Chunks
```

Example:

Document

```
Docker volumes persist data.
```

Question

```
How do I save container data?
```

Even though the wording is different,

Vector Search retrieves the Docker Volumes chunk because it understands semantic similarity.

---

# Stage 3 — Basic RAG

After retrieval,

we build the prompt.

```
Context

+

Question

↓

GPT

↓

Answer
```

Prompt Example

```
Context

...

Question

...

Answer ONLY using the supplied context.
```

At this stage, we have our first working Retrieval-Augmented Generation system.

---

# Stage 4 — Hybrid Search

## Problem

Vector Search is excellent for semantic meaning.

Keyword Search is excellent for exact matches.

Example

Question

```
Azure AI Search Pricing
```

Keyword Search often performs better.

Question

```
How do I persist container data?
```

Vector Search performs better.

Instead of choosing one,

we combine both.

Pipeline

```
Question

↓

Vector Search

+

Keyword Search

↓

Merge Results
```

This is called **Hybrid Search**.

Almost every enterprise RAG system uses some form of Hybrid Search.

---

# Stage 5 — Re-ranking

Hybrid Search returns many candidate chunks.

Not every chunk is equally useful.

Pipeline

```
Question

↓

Hybrid Search

↓

20 Candidate Chunks

↓

Re-ranker

↓

Best 5 Chunks
```

The Re-ranker scores every chunk based on its relevance.

Instead of sending everything to GPT,

we send only the best chunks.

Benefits:

* Better answers
* Less noise
* Lower token usage

---

# Stage 6 — Context Compression

Even the best chunks contain unnecessary information.

Instead of sending

```
Entire Chunk
```

we send

```
Only Relevant Sentences
```

Example

Chunk

```
Docker

Images

Volumes

Networking

Compose
```

Question

```
Explain Docker Volumes.
```

Compressed Context

```
Volumes persist data.

Volumes survive container deletion.
```

Benefits:

* Faster responses
* Lower cost
* Better focus
* Better answer quality

---

# Stage 7 — Metadata Filtering

Searching every document is inefficient.

Knowledge Base

```
Resume

Roadmap

Assessments

Docker Notes

Azure Notes

Interview Notes
```

Question

```
Summarize my resume.
```

Instead of searching everything,

the Query Analyzer detects

```
resume
```

Retriever performs

```
Search Resume Only
```

Benefits:

* Faster retrieval
* Higher precision
* Better scalability

---

# Stage 8 — Conversation Memory

Users ask follow-up questions.

Example

```
Explain Docker.
```

Assistant replies.

User

```
What about volumes?
```

Without memory,

retrieval searches

```
What about volumes?
```

which lacks context.

Conversation Memory stores previous interactions,

allowing the system to understand what "volumes" refers to.

---

# Stage 9 — Query Rewriting

Conversation Memory enables Query Rewriting.

Conversation

```
Explain Docker.

↓

What about volumes?
```

Internally rewritten as

```
Explain Docker Volumes.
```

The rewritten query is used only for retrieval.

GPT still responds naturally to the user's original question.

Benefits:

* Better follow-up retrieval
* Improved multi-turn conversations
* Higher answer accuracy

---

# Final Production RAG Pipeline

```
User Question
        │
        ▼
Conversation Memory
        │
        ▼
Query Rewriter
        │
        ▼
Query Analyzer
        │
        ▼
Metadata Filter
        │
        ▼
Hybrid Search
        │
        ▼
Merge Results
        │
        ▼
Re-ranker
        │
        ▼
Context Compression
        │
        ▼
Prompt Builder
        │
        ▼
GPT-5
        │
        ▼
Final Answer
```

---

# Why We Built It in This Order

Each stage solves a limitation of the previous stage.

1. Store knowledge in a searchable format.
2. Split documents into meaningful chunks.
3. Generate semantic embeddings.
4. Store embeddings in pgvector.
5. Retrieve semantically similar chunks.
6. Build the first working RAG system.
7. Improve retrieval with Hybrid Search.
8. Improve relevance using Re-ranking.
9. Reduce tokens with Context Compression.
10. Narrow the search using Metadata Filtering.
11. Preserve conversation using Memory.
12. Rewrite follow-up questions for better retrieval.

Rather than building a complex RAG system all at once, we improved it incrementally, understanding the purpose behind every enhancement.

---

# Enterprise RAG Architecture

Modern AI assistants such as ChatGPT (Files), Microsoft Copilot, Perplexity, Claude Projects, and Glean follow a similar architecture.

```
User
   │
   ▼
Conversation Memory
   │
   ▼
Query Rewriter
   │
   ▼
Query Analyzer
   │
   ▼
Metadata Filter
   │
   ▼
Hybrid Retriever
   │
   ▼
Re-ranker
   │
   ▼
Context Compression
   │
   ▼
Prompt Builder
   │
   ▼
Large Language Model
   │
   ▼
Final Answer
```

The difference between simple RAG and enterprise RAG lies not in GPT itself, but in the quality of the retrieval pipeline.

---

# Key Takeaways

* RAG is much more than Vector Search.
* Chunking directly impacts retrieval quality.
* Embeddings enable semantic understanding.
* pgvector turns PostgreSQL into a semantic search engine.
* Hybrid Search combines semantic and keyword matching.
* Re-ranking selects the most relevant context.
* Context Compression reduces tokens while preserving meaning.
* Metadata Filtering narrows the search space.
* Conversation Memory enables multi-turn interactions.
* Query Rewriting improves retrieval for follow-up questions.
* A strong retrieval pipeline produces significantly better LLM responses.

---

# What's Next — Agentic RAG

Traditional RAG answers questions using retrieved knowledge.

Agentic RAG takes this one step further.

Instead of RAG being the entire application,

it becomes one capability of an AI Agent.

```
User
   │
   ▼
AI Agent
   │
   ├── Tool Calling
   ├── RAG
   ├── Database
   ├── APIs
   ├── Reasoning
   └── Planning
        │
        ▼
Final Response
```

In Agentic RAG, the agent decides:

* When to call a tool.
* When to search the knowledge base.
* When to combine multiple tools with RAG.
* When to answer directly without external retrieval.

This is the architecture used by modern AI copilots and forms the next stage of our learning journey.
