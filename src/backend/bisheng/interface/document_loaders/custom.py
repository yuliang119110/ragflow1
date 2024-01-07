import logging

from langchain.document_loaders.pdf import BasePDFLoader

from bisheng.interface.base import CustomDocumentLoadersExecutor
from langchain.docstore.document import Document
from llama_index import SimpleDirectoryReader
from typing import Any, List
from bisheng.utils.logger import logger


class SimpleDirectoryReaderLoader(BasePDFLoader):
    """SimpleDirectoryReaderLoader"""

    @staticmethod
    def function_name():
        return 'SimpleDirectoryReaderLoader'

    @classmethod
    def initialize(cls, *args, **kwargs):
        return cls.from_toolkit_and_llm(*args, **kwargs)

    def __init__(self, file_path: str):
        super().__init__(file_path)

    # @classmethod
    def load(self) -> List[Document]:
        logger.info("进入到了llamaindex的流程里里面了")
        return self.from_toolkit_and_llm(self.file_path)

    @classmethod
    def from_toolkit_and_llm(cls,
                             file_path: str,
                             **kwargs: Any):
        logger.info("进入到了llamaindex的流程里里面-> file_path", file_path)
        logger.info(f'进入到了llamaindex的流程里里面 file_path={file_path}')
        documents = SimpleDirectoryReader(
            input_files=[file_path]
        ).load_data()

        docs = list()

        for idx in documents:
            docs.append(Document(page_content=idx.text,
                                 # metadata=idx.metadata
                                 ))
        logger.info("现在我们来看一下load之后的文本信息 docs-> ", docs)
        logger.info(f'现在我们来看一下load之后的文本信息 docs={docs}')
        return docs

    # def load(self) -> List[Document]:
    #     return self.from_toolkit_and_llm(self.file_path)


CUSTOM_LOADERS = {
    'SimpleDirectoryReaderLoader': SimpleDirectoryReaderLoader,

}
