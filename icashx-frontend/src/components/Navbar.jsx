import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-blue-600 text-white px-6 py-3 flex justify-between items-center">
      <h1 className="text-xl font-semibold">iCashX Dashboard</h1>
      <div className="space-x-4">
        <Link to="/" className="hover:underline">Dashboard</Link>
        <Link to="/leads" className="hover:underline">Leads</Link>
        <Link to="/properties" className="hover:underline">Properties</Link>
      </div>
    </nav>
  );
}