import asyncio
from pprint import pprint
from typing import List
from chonkie.pipeline import Pipeline
from chonkie.chef.markdown import MarkdownDocument
from autogen_core.memory import Memory, MemoryContent, MemoryMimeType
from memory import chroma_memory




docs: List[MarkdownDocument] = (
    Pipeline()
    .fetch_from("file", dir="./docs", ext=[".md"])
    .process_with("markdown")
    .chunk_with("semantic", threshold=0.8, chunk_size=1024, similarity_window=3)
    .run()
)


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

def main():
    asyncio.run(add_docs_to_memory(chroma_memory, docs))

if __name__ == "__main__":
    main()