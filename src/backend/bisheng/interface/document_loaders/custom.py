from typing import Any, List, Optional

from bisheng.interface.base import CustomAgentExecutor, CustomDocumentLoadersExecutor
from langchain.docstore.document import Document
# from llama_index import Document, SimpleDirectoryReader


class SimpleDirectoryReaderLoader(CustomDocumentLoadersExecutor):
    """SimpleDirectoryReaderLoader"""

    @staticmethod
    def function_name():
        return 'SimpleDirectoryReaderLoader'

    @classmethod
    def initialize(cls, *args, **kwargs):
        return cls.from_toolkit_and_llm(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # @classmethod
    # def from_toolkit_and_llm(cls,
    #                          file_path: str, ):
    #     documents = SimpleDirectoryReader(
    #         input_files=[file_path]
    #     ).load_data()
    #
    #     docs = []
    #
    #     for idx in documents:
    #         docs.append(Document(page_content=idx.text,
    #                              metadata=idx.metadata
    #                              ))
    #
    #     return docs


CUSTOM_LOADERS = {
    'SimpleDirectoryReaderLoader': SimpleDirectoryReaderLoader,

}
