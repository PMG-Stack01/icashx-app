import { useEffect, useState } from "react";
import api from "../api/client";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";

export default function Dashboard() {
  const [stats, setStats] = useState({
    leads: 0,
    offers: 0,
    contracts: 0,
    profit: 0,
  });

  useEffect(() => {
    // Example: Fetch summary metrics
    api.get("/leads/list").then((res) => setStats({ ...stats, leads: res.data.length }));
  }, []);

  const chartData = [
    { name: "Leads", value: stats.leads },
    { name: "Offers", value: stats.offers },
    { name: "Contracts", value: stats.contracts },
    { name: "Profit ($)", value: stats.profit },
  ];

  return (
    <div className="p-8">
      <h1 className="text-3xl font-bold mb-6">Dashboard</h1>
      <div className="grid grid-cols-4 gap-6 mb-6">
        <SummaryCard title="Leads" value={stats.leads} />
        <SummaryCard title="Offers Sent" value={stats.offers} />
        <SummaryCard title="Contracts Signed" value={stats.contracts} />
        <SummaryCard title="Total Profit" value={`$${stats.profit}`} />
      </div>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={chartData}>
          <XAxis dataKey="name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="value" fill="#3b82f6" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

const SummaryCard = ({ title, value }) => (
  <div className="bg-white shadow rounded-lg p-6">
    <h2 className="text-gray-600 mb-2">{title}</h2>
    <p className="text-2xl font-semibold">{value}</p>
  </div>
);