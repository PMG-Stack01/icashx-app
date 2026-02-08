export default function LeadCard({ lead }) {
  const statusColors = {
    new: "bg-blue-100 text-blue-700",
    analyzing: "bg-yellow-100 text-yellow-700",
    offer_sent: "bg-green-100 text-green-700",
    contract_signed: "bg-purple-100 text-purple-700",
  };

  return (
    <div className="bg-white p-5 rounded-lg shadow hover:shadow-md border border-gray-100 transition-all">
      <h3 className="text-lg font-semibold text-gray-800">{lead.name}</h3>
      <p className="text-gray-600 text-sm">{lead.phone}</p>
      <p className="text-gray-500 text-sm">{lead.address}</p>

      <div className="mt-3 flex items-center justify-between">
        <span
          className={`text-xs px-2 py-1 rounded ${
            statusColors[lead.status] || "bg-gray-100 text-gray-600"
          }`}
        >
          {lead.status?.replace("_", " ").toUpperCase() || "UNKNOWN"}
        </span>
        <button className="text-blue-600 text-sm font-medium hover:underline">
          View Details
        </button>
      </div>
    </div>
  );
}