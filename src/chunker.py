from pprint import pprint
from chonkie import MarkdownChef
from chonkie.pipeline import Pipeline


doc = (Pipeline()
       .fetch_from("file", dir="./docs", ext=[".md"])
       .process_with("markdown")
       .chunk_with("recursive",chunk_size=512)
       .store_in("chroma", collection_name="documents", path="./chroma_db")
       .run()
)

pprint(doc)