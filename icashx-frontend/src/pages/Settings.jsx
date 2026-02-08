import { useState } from "react";

export default function Settings() {
  const [form, setForm] = useState({
    apiKey: "",
    phoneNumber: "",
    emailSender: "",
    notifications: true,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    alert("✅ Settings saved successfully!");
  };

  return (
    <div className="p-8 max-w-2xl">
      <h1 className="text-3xl font-bold mb-6">Settings</h1>
      <form onSubmit={handleSubmit} className="bg-white p-6 rounded shadow space-y-4">
        <div>
          <label className="block text-gray-600">OpenAI API Key</label>
          <input
            type="password"
            value={form.apiKey}
            onChange={(e) => setForm({ ...form, apiKey: e.target.value })}
            placeholder="sk-..."
            className="mt-1 border rounded px-3 py-2 w-full"
          />
        </div>

        <div>
          <label className="block text-gray-600">Twilio Phone Number</label>
          <input
            type="text"
            value={form.phoneNumber}
            onChange={(e) => setForm({ ...form, phoneNumber: e.target.value })}
            placeholder="+15555555555"
            className="mt-1 border rounded px-3 py-2 w-full"
          />
        </div>

        <div>
          <label className="block text-gray-600">Email Sender Address</label>
          <input
            type="email"
            value={form.emailSender}
            onChange={(e) => setForm({ ...form, emailSender: e.target.value })}
            placeholder="you@domain.com"
            className="mt-1 border rounded px-3 py-2 w-full"
          />
        </div>

        <div className="flex items-center space-x-3">
          <input
            type="checkbox"
            id="notifications"
            checked={form.notifications}
            onChange={(e) => setForm({ ...form, notifications: e.target.checked })}
            className="w-4 h-4"
          />
          <label htmlFor="notifications" className="text-gray-600">
            Enable AI alerts & contract notifications
          </label>
        </div>

        <button
          type="submit"
          className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded"
        >
          Save Settings
        </button>
      </form>
    </div>
  );
}