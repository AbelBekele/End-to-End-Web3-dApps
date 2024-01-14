import { classNames } from '@/utils'
import { Inter } from 'next/font/google'
import Header from '@/components/Header'
import SendTransaction from '@/components/SendTransaction'
import {Table, TableHeader, TableColumn, TableBody, TableRow, TableCell, getKeyValue} from "@nextui-org/react";
import { useWallet } from '@txnlab/use-wallet'
import Provider from '@/components/Provider'
import React, { useEffect } from 'react';
import { useRouter } from 'next/router'
import { truncateAddress } from '@/utils'

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



export default function Page() {
    const { providers, activeAddress } = useWallet()
    const renderProviders = () => {
        return providers?.map((provider) => (
          <Provider
            activeAddress={activeAddress}
          />
        ))
      }
      const router = useRouter(); 

      React.useEffect(() => {
        async function checkAddress() {
            const response = await fetch('http://192.168.137.236:8088/trainees_hash');
            if (response.ok) {
                const data = await response.json();
                const hashes = data.map((item: { hash: string }) => item.hash);
    
                if (activeAddress === 'ZYPLVWUNKL4MNZPJNSYFTZYUDJMMDJHGLSGZDUC6NPTBRKMZWUBAYCWXBI') {
                    router.push('/trainer');
                } else if (hashes.includes(activeAddress)) {
                    router.push('/trainee');
                }
            } else {
                console.error('Failed to fetch trainees hash');
            }
        }
    
        checkAddress();
    }, [activeAddress, router]);

  return (
    <main className={classNames('relative flex-1 isolate', inter.className)}>
      <Header />

      <section className="py-10 sm:py-16 lg:py-24">
            <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
                <div className="grid items-center grid-cols-1 lg:grid-cols-2 gap-x-12 xl:gap-x-24 gap-y-12">
                    <div className="relative lg:mb-12">
                        <img className="absolute -right-0 -bottom-8 xl:-bottom-12 xl:-right-4" src="https://cdn.rareblocks.xyz/collection/celebration/images/content/3/dots-pattern.svg" alt="" />
                        <div className="pl-12 pr-6">
                            <img className="relative" src="https://10academy.org/static/media/Africa.c7db02081813640baf85.png" alt="" />
                        </div>
                        <div className="absolute left-0 pr-12 bottom-8 xl:bottom-20">
                            <div className="max-w-xs bg-red-600 rounded-lg sm:max-w-md xl:max-w-md">
                                <div className="px-3 py-4 sm:px-5 sm:py-8">
                                    <div className="flex items-start">
                                        <p className="text-3xl sm:text-4xl">📄</p>
                                        <blockquote className="ml-5">
                                            <p className="text-sm font-medium text-white sm:text-lg">Certification arena!</p>
                                        </blockquote>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div className="2xl:pl-16">
                        <h2 className="text-3xl font-bold leading-tight text-white sm:text-4xl lg:text-5xl lg:leading-tight">Precision Learning for AI and Web3 Jobs</h2>
                        <p className="text-xl leading-relaxed text-white mt-9">95% employment, community-rich cohorts, custom learning platform, pan-African, careers skills and alumni network included!</p>
                    </div>
                </div>
            </div>
        </section>

        <section className="py-10 sm:py-16 lg:py-24">
            <div className="px-4 mx-auto max-w-7xl sm:px-6 lg:px-8">
                <div className="max-w-xl mx-auto text-center">
                    <div className="inline-flex px-4 py-1.5 mx-auto rounded-full bg-red-500">
                        <p className="text-xs font-semibold tracking-widest text-white uppercase">NFT Certificates</p>
                    </div>
                    <h2 className="mt-6 text-3xl font-bold leading-tight text-white sm:text-4xl lg:text-5xl">Effortless certificate creation for trainers, easy claims for students</h2>
                    <p className="mt-4 text-base leading-relaxed text-white">A dynamic portal where trainers effortlessly create certificates and students easily claim their achievements. Streamlining certification processes for a seamless learning journey.</p>
                </div>

                <div className="grid grid-cols-1 gap-5 mt-12 sm:grid-cols-2 lg:mt-20 lg:gap-x-12">
                    {/* Repeat this div for each feature */}
                    <div className="transition-all rounded-xl duration-200 bg-red-600 hover:shadow-xl">
                        <div className="py-10 px-9">
                            <svg className="w-16 h-16 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                            </svg>
                            <h3 className="mt-8 text-4xl font-semibold text-white">Trainer</h3>
                            <p className="mt-4 text-base text-white">Revolutionizing Education with Unique Digital Certificates for Students.</p>
                        </div>
                    </div>
                    <div className="transition-all rounded-xl duration-200 bg-red-600 hover:shadow-xl">
                        <div className="py-10 px-9">
                            <svg className="w-16 h-16 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="1" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                            </svg>
                            <h3 className="mt-8 text-4xl font-semibold text-white">Trainee</h3>
                            <p className="mt-4 text-base text-white">Your Digital Passport to Achievements! Seamlessly receive and showcase your unique certificates on the blockchain.</p>
                        </div>
                    </div>
                    
                </div>
            </div>
        </section>
        <section className="py-10 sm:py-16 lg:py-24">
            <div className="max-w-6xl px-4 mx-auto sm:px-6 lg:px-8">
                <h2 className="text-3xl font-bold leading-tight text-white sm:text-4xl lg:text-5xl">Frequently Asked Questions</h2>

                <div className="flow-root mt-12 sm:mt-16">
                    <div className="divide-y divide-gray--200 -my-9">
                        <div className="py-9">
                            <p className="text-xl font-semibold text-white">How to create an account?</p>
                            <p className="mt-3 text-base text-white">Amet minim mollit non deserunt ullamco est sit aliqua dolor do amet sint. Velit officia consequat duis enim velit mollit. Exercitation veniam consequat sunt nostrud amet.</p>
                            <p className="mt-3 text-base text-white">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                        </div>

                        <div className="py-9">
                            <p className="text-xl font-semibold text-white">What payment method do you support?</p>
                            <p className="mt-3 text-base text-white">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Ut enim ad minim veniam.</p>
                        </div>

                        <div className="py-9">
                            <p className="text-xl font-semibold text-white">What payment method do you support?</p>
                            <p className="mt-3 text-base text-white">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
                        </div>

                        <div className="py-9">
                            <p className="text-xl font-semibold text-white">How do you provide support?</p>
                            <p className="mt-3 text-base text-white">
                                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt <a href="#" title="" className="text-blue-600 transition-all duration-200 hover:text-blue-700 focus:text-blue-700 hover:underline">support@10acadmey.org</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
  )
}


