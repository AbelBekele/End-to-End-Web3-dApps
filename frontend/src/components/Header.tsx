import Link from 'next/link'
import ConnectMenu from './ConnectMenu'
const logo = '/logo.svg';

export default function Header() {
  return (
    <header>
      <nav
        className="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8"
        aria-label="Global"
      >
        <div className="flex">
          <Link
            href="/"
            className="-m-1.5 p-1.5 text-xl font-semibold text-white transition hover:text-teal-500"
          >
            <img src={logo} alt="Logo" />
          </Link>
        </div>
        <div className="flex">
          <ConnectMenu />
        </div>
      </nav>
    </header>
  )
}
