import { useContext, useEffect, useRef, useState } from "react";
import { useNodes } from "reactflow";
import { ChatType } from "../../types/chat";
import BuildTrigger from "./buildTrigger";
import ChatTrigger from "./chatTrigger";

import * as _ from "lodash";
import { TabsContext } from "../../contexts/tabsContext";
import { getBuildStatus } from "../../controllers/API";
import FormModal from "../../modals/formModal";
import { NodeType } from "../../types/flow";

export default function Chat({ flow }: { flow: ChatType['flow'], reactFlowInstance: any }) {
  const [open, setOpen] = useState(false);
  const [isBuilt, setIsBuilt] = useState(false); // 构建完成
  const [canOpen, setCanOpen] = useState(false); // 是否可打开对话
  const { tabsState } = useContext(TabsContext);

  // 打开对话框快捷键
  useEffect(() => {
    const handleKeyDown = (event: KeyboardEvent) => {
      if (
        (event.key === "K" || event.key === "k") &&
        (event.metaKey || event.ctrlKey) &&
        isBuilt
      ) {
        event.preventDefault();
        setOpen((oldState) => !oldState);
      }
    };
    document.addEventListener("keydown", handleKeyDown);
    return () => {
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, [isBuilt]);

  // 获取构建状态
  useEffect(() => {
    // Define an async function within the useEffect hook
    const fetchBuildStatus = async () => {
      const response = await getBuildStatus(flow.id);
      setIsBuilt(response.built);
    };

    // Call the async function
    fetchBuildStatus();
  }, [flow]);

  // 根据tabsState跟新build和canopen状态
  const prevNodesRef = useRef<any[] | undefined>();
  // const firstChange = useRef(true)
  const nodes = useNodes();
  useEffect(() => {
    const prevNodes = prevNodesRef.current;
    const currentNodes = nodes.map((node: NodeType) =>
      _.cloneDeep(node.data.node.template)
    );
    if (
      tabsState &&
      tabsState[flow.id] &&
      tabsState[flow.id].isPending &&
      JSON.stringify(prevNodes) !== JSON.stringify(currentNodes)
    ) {
      // 上一次与当前node template不同，改变build状态
      setIsBuilt(false);
      // !firstChange.current && console.log('有变更 :>> ');
    }
    // 有input keys时打开canopen
    if (
      tabsState &&
      tabsState[flow.id] &&
      tabsState[flow.id].formKeysData &&
      tabsState[flow.id].formKeysData.input_keys &&
      tabsState[flow.id].formKeysData.input_keys.length
      // Object.keys(tabsState[flow.id].formKeysData.input_keys).length > 0
    ) {
      setCanOpen(true);
    } else {
      setCanOpen(false);
    }

    prevNodesRef.current = currentNodes;
  }, [tabsState, flow.id]);

  return (
    <>
      <div>
        {/* 构建按钮 */}
        <BuildTrigger
          open={open}
          flow={flow}
          setIsBuilt={setIsBuilt}
          isBuilt={isBuilt}
        />
        {/* 对话表单 */}
        {isBuilt &&
          tabsState[flow.id] &&
          tabsState[flow.id].formKeysData &&
          canOpen && (
            <FormModal
              key={flow.id}
              flow={flow}
              open={open}
              setOpen={setOpen}
            />
          )}
        {/* 对话按钮 */}
        <ChatTrigger
          canOpen={canOpen}
          open={open}
          setOpen={setOpen}
          isBuilt={isBuilt}
        />
      </div>
    </>
  );
}
