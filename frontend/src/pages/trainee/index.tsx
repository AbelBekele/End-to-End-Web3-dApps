import Head from 'next/head'
import Page from '@/components/Trainer_dashboard'

import {NextUIProvider} from "@nextui-org/react";
import Trainer_dashboard from '@/components/Trainee_dashboard';
import Trainee_dashboard from '@/components/Trainee_dashboard';

export default function Home() {
  // 2. Wrap NextUIProvider at the root of your app
  return (
    <NextUIProvider>
          <>
          <Head>
            <title> Trainee | 10 Academy</title>
          </Head>

          <Trainee_dashboard/>
    </>
    </NextUIProvider>
  );
}

