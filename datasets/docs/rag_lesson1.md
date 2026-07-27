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