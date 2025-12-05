# LLM Memory and RAG using AutoGen

## What is RAG
The RAG (Retrieval Augmented Generation) pattern which is common in building AI systems encompasses two distinct phases:

1. Indexing: Loading documents, chunking them, and storing them in a vector database
2. Retrieval: Finding and using relevant chunks during conversation runtime

### Indexing
Using **chonkie** to index markdown documents 
```python
docs: List[MarkdownDocument] = (
    Pipeline()
    .fetch_from("file", dir="./docs", ext=[".md"])
    .process_with("markdown")
    .chunk_with("semantic", threshold=0.8, chunk_size=1024, similarity_window=3)
    .run()
)
```
Using **ChromaDB** with to store chunks and vector embeddings

```python
chroma_memory = ChromaDBVectorMemory(
    config=PersistentChromaDBVectorMemoryConfig(
        collection_name="documents",
        persistence_path="./chroma_db",
        k=10,
        score_threshold=0.6,
        )
)
```

Adding documents to memory via **AutoGen**

```python
async def add_docs_to_memory(memory: Memory, docs: List[MarkdownDocument]) -> None: 
    for doc in docs:
        print(f"Adding document {doc.id} with {len(doc.chunks)} chunks to memory.")
        for i, chunk in enumerate(doc.chunks):
            print({"chunkId": chunk.id, "chunkIndex": i, "tokenCount": chunk.token_count, "sourceDocumentId": doc.id})
            await memory.add(
                MemoryContent(
                    content=chunk.text,
                    mime_type=MemoryMimeType.MARKDOWN,
                    metadata={"chunkId": chunk.id, "chunkIndex": i, "tokenCount": chunk.token_count, "sourceDocumentId": doc.id},
                )
            )
```