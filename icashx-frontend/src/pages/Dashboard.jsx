import { useEffect, useState } from "react";
import api from "../api/client";
import SummaryCard from "../components/SummaryCard";

export default function Dashboard() {
  const [stats, setStats] = useState({ leads: 0, offers: 0, contracts: 0, profit: 0 });

  useEffect(() => {
    api.get("/leads/list")
       .then(res => setStats({ ...stats, leads: res.data.length }))
       .catch(() => console.log("Backend not reachable yet"));
  }, []);

  return (
    <div>
      <h1 className="text-3xl font-semibold mb-6">Overview</h1>
      <div className="grid grid-cols-4 gap-5">
        <SummaryCard title="Leads" value={stats.leads} />
        <SummaryCard title="Offers Sent" value={stats.offers} />
        <SummaryCard title="Contracts Signed" value={stats.contracts} />
        <SummaryCard title="Total Profit" value={`$${stats.profit}`} />
      </div>
    </div>
  );
}