import Head from 'next/head'
import Page from '@/components/Page'

import {NextUIProvider} from "@nextui-org/react";

export default function Home() {
  // 2. Wrap NextUIProvider at the root of your app
  return (
    <NextUIProvider>
          <>
          <Head>
            <title> Certification | 10 Academy</title>
          </Head>

          <Page />
    </>
    </NextUIProvider>
  );
}

