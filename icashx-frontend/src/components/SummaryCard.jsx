export default function SummaryCard({ title, value }) {
  return (
    <div className="bg-white shadow rounded-lg p-6 text-center">
      <h2 className="text-gray-600 mb-1">{title}</h2>
      <p className="text-2xl font-bold text-blue-600">{value}</p>
    </div>
  );
}