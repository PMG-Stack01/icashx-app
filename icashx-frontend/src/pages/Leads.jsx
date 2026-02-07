import { useState, useEffect } from "react";
import api from "../api/client";

export default function Leads() {
  const [leads, setLeads] = useState([]);

  useEffect(() => {
    api.get("/leads/list").then((res) => setLeads(res.data));
  }, []);

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Leads</h1>
      <table className="min-w-full bg-white rounded shadow">
        <thead>
          <tr className="border-b">
            <th className="px-4 py-2">Name</th>
            <th className="px-4 py-2">Phone</th>
            <th className="px-4 py-2">Address</th>
            <th className="px-4 py-2">Status</th>
          </tr>
        </thead>
        <tbody>
          {leads.map((lead) => (
            <tr key={lead.id} className="border-t hover:bg-gray-50">
              <td className="px-4 py-2">{lead.name}</td>
              <td className="px-4 py-2">{lead.phone}</td>
              <td className="px-4 py-2">{lead.address}</td>
              <td className="px-4 py-2">
                <span className="bg-blue-100 text-blue-600 px-2 py-1 rounded">
                  {lead.status}
                </span>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}