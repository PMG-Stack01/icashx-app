import { NavLink, useLocation } from "react-router-dom";
import {
  FaHome,
  FaUserTie,
  FaBuilding,
  FaFileContract,
  FaUserCog,
  FaUsers,
} from "react-icons/fa";

export default function Sidebar() {
  const { pathname } = useLocation();

  // keep all your original links exactly as you had them
  const links = [
    { to: "/", label: "Dashboard", icon: <FaHome /> },
    { to: "/leads", label: "Leads", icon: <FaUsers /> },
    { to: "/properties", label: "Properties", icon: <FaBuilding /> },
    { to: "/buyers", label: "Buyers", icon: <FaUserTie /> },
    { to: "/contracts", label: "Contracts", icon: <FaFileContract /> },
    { to: "/settings", label: "Settings", icon: <FaUserCog /> },
  ];

  return (
    <aside className="fixed left-0 top-0 h-full w-64 bg-gray-900 text-white flex flex-col">
      {/* Header */}
      <div className="px-6 py-4 text-2xl font-bold border-b border-gray-700 sticky top-0 bg-gray-900 z-10">
        iCashX AI
      </div>

      {/* Navigation links */}
      <nav className="flex-grow overflow-y-auto mt-2 pb-4">
        {links.map((link) => (
          <NavLink
            key={link.to}
            to={link.to}
            end
            className={({ isActive }) =>
              `flex items-center px-6 py-3 text-sm rounded-md transition-colors duration-200 ${
                isActive
                  ? "bg-blue-600 text-white"
                  : "text-gray-300 hover:bg-gray-800 hover:text-white"
              }`
            }
          >
            <span className="mr-3 text-lg">{link.icon}</span>
            {link.label}
          </NavLink>
        ))}
      </nav>

      {/* Footer */}
      <footer className="px-6 py-4 border-t border-gray-700 text-xs text-gray-400">
        © {new Date().getFullYear()} iCashX
      </footer>
    </aside>
  );
}