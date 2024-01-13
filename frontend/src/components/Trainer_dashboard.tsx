import { classNames } from '@/utils'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import SendTransaction from '@/components/SendTransaction'
import React from "react";
import {Table, TableHeader, TableColumn, TableBody, TableRow, TableCell, getKeyValue} from "@nextui-org/react";

const rows = [
    {
      key: "1",
      name: "Tony Reichert",
      role: "CEO",
      status: "Active",
    },
    {
      key: "2",
      name: "Zoey Lang",
      role: "Technical Lead",
      status: "Paused",
    },
    {
      key: "3",
      name: "Jane Fisher",
      role: "Senior Developer",
      status: "Active",
    },
    {
      key: "4",
      name: "William Howard",
      role: "Community Manager",
      status: "Vacation",
    },
  ];
  
  const columns = [
    {
      key: "name",
      label: "NAME",
    },
    {
      key: "role",
      label: "ROLE",
    },
    {
      key: "status",
      label: "STATUS",
    },
  ];
  

const inter = Inter({ subsets: ['latin'] })

export default function Trainer_dashboard() {
  return (
    <main className={classNames('relative flex-1 isolate', inter.className)}>
      <Header />

        <section className="py-10 sm:py-16 lg:py-24">
            <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
                <div className="max-w-xl mx-auto text-center">
                    <div className="inline-flex px-4 py-1.5 mx-auto rounded-full bg-red-500">
                        <p className="text-xs font-semibold tracking-widest text-white uppercase">Trainer</p>
                    </div>
                    <h2 className="mt-6 text-3xl font-bold leading-tight text-white sm:text-4xl lg:text-5xl">Effortlessly Transefer Certificates to Traniees</h2>
                </div>
            </div>
        </section>
        <div className="flex items-center justify-center">
        <div className="outer-container bg-black w-2/3">
            <div className='container bg-black max-w-40 w-30'>
            <Table aria-label="Example static collection table">
                <TableHeader>
                    <TableColumn>NAME</TableColumn>
                    <TableColumn>ROLE</TableColumn>
                    <TableColumn>STATUS</TableColumn>
                </TableHeader>
                <TableBody>
                    <TableRow key="1">
                    <TableCell>Tony Reichert</TableCell>
                    <TableCell>CEO</TableCell>
                    <TableCell>Active</TableCell>
                    </TableRow>
                    <TableRow key="2">
                    <TableCell>Zoey Lang</TableCell>
                    <TableCell>Technical Lead</TableCell>
                    <TableCell>Paused</TableCell>
                    </TableRow>
                    <TableRow key="3">
                    <TableCell>Jane Fisher</TableCell>
                    <TableCell>Senior Developer</TableCell>
                    <TableCell>Active</TableCell>
                    </TableRow>
                    <TableRow key="4">
                    <TableCell>William Howard</TableCell>
                    <TableCell>Community Manager</TableCell>
                    <TableCell>Vacation</TableCell>
                    </TableRow>
                </TableBody>
                </Table>
            </div>
        </div>
        </div>
    </main>
  )
}


