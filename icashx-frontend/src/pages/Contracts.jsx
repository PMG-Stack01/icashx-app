import { useState, useEffect } from "react";
import api from "../api/client";

export default function Contracts() {
  const [contracts, setContracts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/contracts/list").then((res) => {
      setContracts(res.data || []);
      setLoading(false);
    });
  }, []);

  const downloadContract = (id) => {
    window.open(`${api.defaults.baseURL.replace("/api", "")}/api/contracts/download/${id}`);
  };

  if (loading) return <p className="p-8">Loading contracts...</p>;

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Contracts</h1>
      <div className="overflow-x-auto bg-white rounded shadow">
        <table className="min-w-full text-sm">
          <thead className="bg-gray-100 border-b">
            <tr>
              <th className="px-4 py-2">Seller</th>
              <th className="px-4 py-2">Property</th>
              <th className="px-4 py-2">Offer Price</th>
              <th className="px-4 py-2">Closing Date</th>
              <th className="px-4 py-2">Status</th>
              <th className="px-4 py-2">Actions</th>
            </tr>
          </thead>
          <tbody>
            {contracts.map((c, i) => (
              <tr key={i} className="border-t hover:bg-gray-50">
                <td className="px-4 py-2">{c.seller_name}</td>
                <td className="px-4 py-2">{c.property_address}</td>
                <td className="px-4 py-2">${c.price?.toLocaleString()}</td>
                <td className="px-4 py-2">{c.closing_date}</td>
                <td className="px-4 py-2">
                  <span
                    className={`px-2 py-1 rounded text-xs ${
                      c.status === "signed"
                        ? "bg-green-100 text-green-700"
                        : "bg-yellow-100 text-yellow-700"
                    }`}
                  >
                    {c.status || "pending"}
                  </span>
                </td>
                <td className="px-4 py-2">
                  <button
                    onClick={() => downloadContract(c.id)}
                    className="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700"
                  >
                    Download
                  </button>
                </td>
              </tr>
            ))}
            {contracts.length === 0 && (
              <tr>
                <td colSpan="6" className="text-center py-4">
                  No contracts found.
                </td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}