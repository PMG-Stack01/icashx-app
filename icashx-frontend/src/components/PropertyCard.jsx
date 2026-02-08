export default function PropertyCard({ property }) {
  return (
    <div className="bg-white rounded-lg shadow border border-gray-100 hover:shadow-md transition-all overflow-hidden">
      <div className="p-5">
        <h3 className="text-lg font-semibold text-gray-800 mb-1">
          {property.address}
        </h3>
        <p className="text-sm text-gray-600">
          {property.bedrooms} Bed · {property.bathrooms} Bath
        </p>
        <p className="text-sm text-gray-500">
          Year Built: {property.year_built || "N/A"}
        </p>

        <div className="mt-4 grid grid-cols-2 gap-2 text-sm">
          <div>
            <p className="text-gray-500">ARV</p>
            <p className="font-semibold">${property.arv?.toLocaleString() || "—"}</p>
          </div>
          <div>
            <p className="text-gray-500">Repair Cost</p>
            <p className="font-semibold">${property.repair_cost?.toLocaleString() || "—"}</p>
          </div>
          <div>
            <p className="text-gray-500">Cash Offer</p>
            <p className="font-semibold">${property.cash_offer?.toLocaleString() || "—"}</p>
          </div>
          <div>
            <p className="text-gray-500">Profit</p>
            <p className="font-semibold text-green-600">
              ${property.profit_estimate?.toLocaleString() || "—"}
            </p>
          </div>
        </div>

        <div className="mt-4">
          <button className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 text-sm rounded">
            View Deal
          </button>
        </div>
      </div>
    </div>
  );
}