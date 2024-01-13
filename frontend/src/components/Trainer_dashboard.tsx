import { classNames } from '@/utils'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import SendTransaction from '@/components/SendTransaction'
import React from "react";
import {Table, TableHeader, TableColumn, TableBody, TableRow, TableCell, getKeyValue} from "@nextui-org/react";
import { useState } from 'react';
import {Button} from "@nextui-org/react";

const rows = [
    {
      key: "1",
      name: "Kerod Sisay",
      role: "Week 1 Certificate",
      status: "Active",
    },
    {
      key: "2",
      name: "Mubarek Hussen",
      role: "Technical Lead",
      status: "Paused",
    },
    {
      key: "3",
      name: "Birehan Anteneh",
      role: "Senior Developer",
      status: "Active",
    },
    {
      key: "4",
      name: "Mikiyas Kinfemichael",
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
  const [isTouched, setIsTouched] = useState({});
  const [touchedButton, setTouchedButton] = useState({});

  const handleClick = (key, buttonNumber) => {
    setIsTouched(prevState => ({...prevState, [key]: true}));
    setTouchedButton(prevState => ({...prevState, [key]: buttonNumber}));
  };

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
                    <TableColumn>TRAINEE</TableColumn>
                    <TableColumn>WEEK</TableColumn>
                    <TableColumn>STATUS</TableColumn>
                </TableHeader>
                <TableBody>
                    {rows.map(row => (
                      <TableRow key={row.key}>
                        <TableCell>{row.name}</TableCell>
                        <TableCell>Week 1 Certificate</TableCell>
                        <TableCell className='mx-2'>
                          {isTouched[row.key] ? (
                            touchedButton[row.key] === 1 ? (
                              <Button color="success">
                                Approved
                              </Button>
                            ) : (
                              <Button color="danger">
                                Denied
                              </Button>
                            )
                          ) : (
                            <>
                              <Button className='mx-2' color="success" onClick={() => handleClick(row.key, 1)}>
                                Approve
                              </Button>
                              <Button color="danger" onClick={() => handleClick(row.key, 2)}>
                                Deny
                              </Button>
                            </>
                          )}
                        </TableCell>
                      </TableRow>
                    ))}
                </TableBody>
                </Table>
            </div>
        </div>
        </div>
    </main>
  )
}