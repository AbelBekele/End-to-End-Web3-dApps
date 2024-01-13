import { Head, Html, Main, NextScript } from 'next/document'

import {NextUIProvider} from "@nextui-org/react";

export default function Document() {
  return (
    <Html lang="en">
      <Head />
      <body className="bg-zinc-900 min-h-screen">
        <Main />
        <NextScript />
      </body>
    </Html>
  )
}
