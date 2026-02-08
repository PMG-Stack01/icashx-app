import { useState, useEffect } from "react";
import api from "../api/client";

export default function Buyers() {
  const [buyers, setBuyers] = useState([]);
  const [form, setForm] = useState({ name: "", email: "", phone: "", market: "" });

  useEffect(() => {
    api.get("/buyers/match").then((res) => {
      setBuyers(res.data || []);
    });
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await api.post("/buyers/add", form);
    setBuyers([...buyers, res.data]);
    setForm({ name: "", email: "", phone: "", market: "" });
  };

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Cash Buyers</h1>

      {/* Add Buyer Form */}
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow mb-8 max-w-xl">
        <h2 className="text-xl font-semibold mb-4">Add New Buyer</h2>
        <div className="grid grid-cols-2 gap-4">
          <input
            type="text"
            placeholder="Full Name"
            value={form.name}
            onChange={(e) => setForm({ ...form, name: e.target.value })}
            className="border rounded px-3 py-2"
            required
          />
          <input
            type="email"
            placeholder="Email"
            value={form.email}
            onChange={(e) => setForm({ ...form, email: e.target.value })}
            className="border rounded px-3 py-2"
            required
          />
          <input
            type="text"
            placeholder="Phone"
            value={form.phone}
            onChange={(e) => setForm({ ...form, phone: e.target.value })}
            className="border rounded px-3 py-2"
          />
          <input
            type="text"
            placeholder="Target Market (City or ZIP)"
            value={form.market}
            onChange={(e) => setForm({ ...form, market: e.target.value })}
            className="border rounded px-3 py-2"
          />
        </div>
        <button
          type="submit"
          className="mt-4 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Add Buyer
        </button>
      </form>

      {/* Buyers Table */}
      <div className="overflow-x-auto bg-white rounded shadow">
        <table className="min-w-full text-sm text-left">
          <thead className="bg-gray-100 border-b">
            <tr>
              <th className="px-4 py-2">Name</th>
              <th className="px-4 py-2">Email</th>
              <th className="px-4 py-2">Phone</th>
              <th className="px-4 py-2">Market</th>
            </tr>
          </thead>
          <tbody>
            {buyers.map((b, i) => (
              <tr key={i} className="border-t hover:bg-gray-50">
                <td className="px-4 py-2">{b.name}</td>
                <td className="px-4 py-2">{b.email}</td>
                <td className="px-4 py-2">{b.phone}</td>
                <td className="px-4 py-2">{b.market}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}