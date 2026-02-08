import { Outlet, Link } from "react-router-dom";
import Navbar from "./components/Navbar";
import { AuthProvider, useAuth } from "./context/AuthContext";

function Layout() {
  const { user, logout } = useAuth();
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar>
        {user ? (
          <button onClick={logout} className="bg-red-500 px-3 py-1 rounded text-sm">Logout</button>
        ) : (
          <Link to="/login" className="bg-blue-500 px-3 py-1 rounded text-sm">Login</Link>
        )}
      </Navbar>
      <main className="p-6">
        <Outlet />
      </main>
    </div>
  );
}

export default function AppWrapper() {
  return (
    <AuthProvider>
      <Layout />
    </AuthProvider>
  );
}