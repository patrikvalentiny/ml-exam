from autogen_ext.memory.chromadb import ChromaDBVectorMemory, PersistentChromaDBVectorMemoryConfig

chroma_memory = ChromaDBVectorMemory(
    config=PersistentChromaDBVectorMemoryConfig(
        collection_name="documents",
        persistence_path="./chroma_db",
        k=10,
        # score_threshold=0.4,
        )
)