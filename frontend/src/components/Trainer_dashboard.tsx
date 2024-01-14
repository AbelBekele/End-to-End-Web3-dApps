import { classNames } from '@/utils'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import SendTransaction from '@/components/SendTransaction'
import {Table, TableHeader, TableColumn, TableBody, TableRow, TableCell, getKeyValue} from "@nextui-org/react";
import axios from 'axios';
import React, { useEffect, useState } from 'react';
import {Button} from "@nextui-org/react";



const oldData = [
    {
      key: "1",
      name: "Kerod Sisay",
      week: "Week 1 Certificate",
      status: "Active",
    },
    {
      key: "2",
      name: "Mubarek Hussen",
      week: "Technical Lead",
      status: "Paused",
    },
    {
      key: "3",
      name: "Birehan Anteneh",
      week: "Senior Developer",
      status: "Active",
    },
    {
      key: "4",
      name: "Mikiyas Kinfemichael",
      week: "Community Manager",
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
  const [urls, setUrls] = useState<{ [key: string]: string }>({});
  
  // const handleClick = (key, buttonNumber) => {
  //   setIsTouched(prevState => ({...prevState, [key]: true}));
  //   setTouchedButton(prevState => ({...prevState, [key]: buttonNumber}));
  // };

  const [rows, setRows] = useState([]);

  async function handleClick(key: string, week: number, trainer: string) {
    if (urls[key]) {
        // If the URL is already available, just return
        return;
    }

    setIsTouched(prevState => ({ ...prevState, [key]: true }));

    const response = await fetch('http://192.168.137.236:8088/create_certificate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            full_name: trainer,
            week: `Week ${week} Certificate`
        })
    });

    if (response.ok) {
        const data = await response.json();
        const hash = data.ipfs_hash;
        const url = `https://aqua-advanced-eel-969.mypinata.cloud/ipfs/${hash}`;

        setUrls(prevState => ({ ...prevState, [key]: url }));
    } else {
        console.error('Failed to create certificate');
    }
}

  useEffect(() => {
    fetch('http://192.168.137.236:8088/trainees')
      .then(response => response.json())
      .then(data => {
        const transformedData = data.map((item, index) => ({
          key: String(index + 1),
          trainee: item.trainee,
          status: `week-${index + 1}`,
          week: item.status === "Active" ? "uncert" : item.status,
        }));
        setRows(transformedData);
      })
      .catch(error => console.error('Error:', error));
  }, []);

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
        
        <div className="mb-6 flex items-center justify-center">
        <div className="outer-container bg-black w-2/3">
        <p className="text-3xl text-white mb-2">Create student certificates</p>
            <div className='container bg-black max-w-40 w-30'>
            <Table aria-label="Certification">
            <TableHeader>
                <TableColumn>TRAINER</TableColumn>
                <TableColumn>WEEK</TableColumn>
                <TableColumn>STATUS</TableColumn>
            </TableHeader>
            <TableBody >
                <TableRow key="4">
                    <TableCell>Abel Bekele</TableCell>
                    <TableCell>Week 5 Certificate</TableCell>
                    <TableCell onClick={() => handleClick("4", 5)}>
                        <Button color="success">
                            Created
                        </Button>
                    </TableCell>
                </TableRow>
                <TableRow key="5">
                    <TableCell>Mubarek Hussen</TableCell>
                    <TableCell>Week 5 certificate</TableCell>
                    <TableCell>
                    <Button 
                        color={isTouched["5"] ? "warning" : "primary"} 
                        onClick={() => handleClick("5", 5, 'Mubarek Hussen')}
                    >
                        {isTouched["5"] ? (urls["5"] ? <a href={urls["5"]}>Show</a> : 'Requested') : 'Request'}
                    </Button>  
                </TableCell>
                </TableRow>
                <TableRow key="6">
                    <TableCell>Kerod Sisay</TableCell>
                    <TableCell>Week 5 Certificate</TableCell>
                    <TableCell>
                        <Button 
                            color={isTouched["6"] ? "warning" : "primary"} 
                            onClick={() => handleClick("6", 5)}
                        >
                            {isTouched["6"] ? (urls["6"] ? <a href={urls["6"]}>Show</a> : 'Requested') : 'Request'}
                        </Button>  
                    </TableCell>
                </TableRow>
            </TableBody>
        </Table>
            </div>
        </div>
        </div>
        <div className="flex items-center justify-center">
        <div className="outer-container bg-black w-2/3">
        <p className="text-3xl text-white mb-2">Transfer student certificates</p>
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
                    <TableCell>{row.trainee}</TableCell>
                    <TableCell>{row.week}</TableCell>
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
        <div className="mt-10 flex items-center justify-center">
          </div>
    </main>
  )
}