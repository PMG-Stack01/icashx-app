import { useEffect, useState } from "react";
import api from "../api/client";

export default function Properties() {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    api
      .get("/properties/list")
      .then((res) => setProperties(res.data))
      .catch(() => console.log("Failed to load properties"));
  }, []);

  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Properties</h1>
      <table className="min-w-full bg-white rounded shadow">
        <thead>
          <tr>
            <th className="px-4 py-2 text-left">Address</th>
            <th className="px-4 py-2 text-left">Bedrooms</th>
            <th className="px-4 py-2 text-left">Bathrooms</th>
            <th className="px-4 py-2 text-left">Est. Value</th>
          </tr>
        </thead>
        <tbody>
          {properties.map((p) => (
            <tr key={p.id} className="border-t hover:bg-gray-50">
              <td className="px-4 py-2">{p.address}</td>
              <td className="px-4 py-2">{p.bedrooms}</td>
              <td className="px-4 py-2">{p.bathrooms}</td>
              <td className="px-4 py-2">${p.arv}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}