from typing import Dict, List, Optional, Type

from bisheng.interface.base import LangChainTypeCreator
from bisheng.interface.custom_lists import documentloaders_type_to_cls_dict
from bisheng.interface.document_loaders.custom import CUSTOM_LOADERS
from bisheng.interface.importing.utils import import_class
from bisheng.settings import settings
from bisheng.template.frontend_node.documentloaders import \
    DocumentLoaderFrontNode
from bisheng.utils.logger import logger
from bisheng.utils.util import build_template_from_class


class DocumentLoaderCreator(LangChainTypeCreator):
    type_name: str = 'documentloaders'

    from_method_nodes = {
        'SimpleDirectoryReaderLoader': 'from_llm_and_tools',
    }


    @property
    def frontend_node_class(self) -> Type[DocumentLoaderFrontNode]:
        return DocumentLoaderFrontNode

    # @property
    # def type_to_loader_dict(self) -> Dict:
    #
    #     return documentloaders_type_to_cls_dict

    @property
    def type_to_loader_dict(self) -> Dict:
        if self.type_dict is None:
            self.type_dict = documentloaders_type_to_cls_dict
            # Add JsonAgent to the list of agents
            for name, agent in CUSTOM_LOADERS.items():
                # TODO: validate AgentType
                self.type_dict[name] = agent  # type: ignore
        return self.type_dict

    def get_signature(self, name: str) -> Optional[Dict]:
        """Get the signature of a document loader."""
        try:
            return build_template_from_class(name, documentloaders_type_to_cls_dict)
        except ValueError as exc:
            raise ValueError(f'Documment Loader {name} not found') from exc
        except AttributeError as exc:
            logger.error(f'Documment Loader {name} not loaded: {exc}')
            return None

    def to_list(self) -> List[str]:
        return [
            documentloader.__name__
            for documentloader in self.type_to_loader_dict.values()
            if documentloader.__name__ in settings.documentloaders or settings.dev
        ]


documentloader_creator = DocumentLoaderCreator()
