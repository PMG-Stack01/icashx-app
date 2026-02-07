import { useState, useEffect } from "react";
import api from "../api/client";

export default function Leads() {
  const [leads, setLeads] = useState([]);

  useEffect(() => {
    api
      .get("/leads/list")
      .then((res) => setLeads(res.data))
      .catch(() => console.log("Failed to load leads"));
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Leads</h1>
      <table className="min-w-full bg-white rounded shadow">
        <thead>
          <tr>
            <th className="px-4 py-2 text-left">Name</th>
            <th className="px-4 py-2 text-left">Phone</th>
            <th className="px-4 py-2 text-left">Address</th>
            <th className="px-4 py-2 text-left">Status</th>
          </tr>
        </thead>
        <tbody>
          {leads.map((lead) => (
            <tr key={lead.id} className="border-t hover:bg-gray-50">
              <td className="px-4 py-2">{lead.name}</td>
              <td className="px-4 py-2">{lead.phone}</td>
              <td className="px-4 py-2">{lead.address}</td>
              <td className="px-4 py-2">{lead.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}