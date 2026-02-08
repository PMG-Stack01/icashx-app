import { createContext, useContext, useState, useEffect } from "react";

const AuthContext = createContext(null);
export const useAuth = () => useContext(AuthContext);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);

  // Load user from localStorage at startup
  useEffect(() => {
    const savedUser = localStorage.getItem("icashx_user");
    if (savedUser) setUser(JSON.parse(savedUser));
  }, []);

  const login = (email, password) => {
    // In a real app: call backend API here
    const fakeUser = { email, token: "demo-token-123" };
    setUser(fakeUser);
    localStorage.setItem("icashx_user", JSON.stringify(fakeUser));
  };

  const register = (email, password) => {
    // In a real app: call signup endpoint
    login(email, password);
  };

  const logout = () => {
    setUser(null);
    localStorage.removeItem("icashx_user");
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  );
};