import { useEffect, useState } from "react";
import { useTranslation } from "react-i18next";
import {
    Table,
    TableBody,
    TableCell,
    TableHead,
    TableHeader,
    TableRow
} from "../../components/ui/table";
import { GPUlistApi } from "../../controllers/API";

export const CpuDetail = () => {
    const { t } = useTranslation()

    const [datalist, setDatalist] = useState([])

    const loadData = () => {
        GPUlistApi().then(res => {
            setDatalist(res.data.list.flat())
        })
    }

    useEffect(loadData, [])

    // 2s刷新一次
    useEffect(() => {
        const timer = setTimeout(loadData, 1000 * 2);

        return () => clearTimeout(timer)
    }, [open, datalist])

    return <Table className="w-full">
        <TableHeader>
            <TableRow>
                <TableHead className="w-[200px]">{t('model.machine')}</TableHead>
                <TableHead>{t('model.gpuNumber')}</TableHead>
                <TableHead>{t('model.gpuID')}</TableHead>
                <TableHead>{t('model.totalMemory')}</TableHead>
                <TableHead>{t('model.freeMemory')}</TableHead>
                <TableHead>{t('model.gpuUtilization')}</TableHead>
            </TableRow>
        </TableHeader>
        <TableBody>
            {datalist.map((el) => (
                <TableRow key={el.gpu_id}>
                    <TableCell>{el.server}</TableCell>
                    <TableCell>{el.gpu_uuid}</TableCell>
                    <TableCell>{el.gpu_id}</TableCell>
                    <TableCell>{el.gpu_total_mem}</TableCell>
                    <TableCell>{el.gpu_used_mem}</TableCell>
                    <TableCell>{(el.gpu_utility * 100).toFixed(2)}%</TableCell>
                </TableRow>
            ))}
        </TableBody>
    </Table>
};
