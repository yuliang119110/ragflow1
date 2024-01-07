import unittest

from langchain.schema import Document

from bisheng.interface.document_loaders.custom import SimpleDirectoryReaderLoader


class TestSimpleDirectoryReaderLoader(unittest.TestCase):

    def test_from_toolkit_and_llm(self):
        # 准备测试数据
        file_path = 'C:\\Users\\31773\\AppData\\Local\\bisheng\\bisheng\\Cache\\8593192a-a56d-4c7c-8431-1f390a250b00\\f0fb9987af5d9c0ced3446d73094045c629e1274efb7af00d3647fe1b5760b07_李昌晋-24届-java开发实习生.pdf'  # 更改为你的文件路径

        # 调用被测试的方法
        docs = SimpleDirectoryReaderLoader.from_toolkit_and_llm(file_path)

        # 执行断言
        self.assertIsInstance(docs, list)  # 检查返回值是否是列表类型
        for doc in docs:
            self.assertIsInstance(doc, Document)  # 检查列表中每个元素是否是 Document 类型

# 如果希望直接运行测试用例，可以使用下面的代码
if __name__ == '__main__':
    unittest.main()
