// src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto';

const App = () => {
  const [transactions, setTransactions] = useState([]);
  const [amount, setAmount] = useState('');
  const [type, setType] = useState('expense');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState('');
  const [description, setDescription] = useState('');
  const [token, setToken] = useState('');

  useEffect(() => {
    if (token) {
      axios.get('http://localhost:5000/transactions', { headers: { Authorization: token } })
        .then(res => setTransactions(res.data))
        .catch(err => console.error(err));
    }
  }, [token]);

  const handleAddTransaction = () => {
    axios.post('http://localhost:5000/transactions', { amount, type, category, date, description }, { headers: { Authorization: token } })
      .then(() => {
        setAmount('');
        setType('expense');
        setCategory('');
        setDate('');
        setDescription('');
      })
      .catch(err => console.error(err));
  };

  const getChartData = () => {
    const labels = [...new Set(transactions.map(t => t.date))];
    const data = labels.map(label => {
      const total = transactions
        .filter(t => t.date === label)
        .reduce((sum, t) => sum + (t.type === 'income' ? t.amount : -t.amount), 0);
      return total;
    });

    return {
      labels,
      datasets: [
        {
          label: 'Balance Over Time',
          data,
          fill: false,
          borderColor: 'blue',
        },
      ],
    };
  };

  return (
    <div>
      <h1>Finance Manager</h1>
      <input type="text" value={amount} onChange={e => setAmount(e.target.value)} placeholder="Amount" />
      <select value={type} onChange={e => setType(e.target.value)}>
        <option value="expense">Expense</option>
        <option value="income">Income</option>
      </select>
      <input type="text" value={category} onChange={e => setCategory(e.target.value)} placeholder="Category" />
      <input type="date" value={date} onChange={e => setDate(e.target.value)} />
      <input type="text" value={description} onChange={e => setDescription(e.target.value)} placeholder="Description" />
      <button onClick={handleAddTransaction}>Add Transaction</button>

      <h2>Transaction Report</h2>
      <Line data={getChartData()} />

      <button onClick={() => setToken('YOUR_JWT_TOKEN')}>Login (Replace with real JWT)</button>
    </div>
  );
};

export default App;