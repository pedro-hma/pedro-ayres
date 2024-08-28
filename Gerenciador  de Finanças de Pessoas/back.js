// server.js
const express = require('express');
const { Sequelize, DataTypes } = require('sequelize');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const cors = require('cors');
const bodyParser = require('body-parser');

require('dotenv').config();

const app = express();
app.use(express.json());
app.use(cors());
app.use(bodyParser.urlencoded({ extended: true }));

// Initialize Sequelize
const sequelize = new Sequelize(process.env.DATABASE_URL, {
  dialect: 'postgres',
  logging: false
});

// Models
const User = sequelize.define('User', {
  username: { type: DataTypes.STRING, unique: true, allowNull: false },
  password: { type: DataTypes.STRING, allowNull: false },
});

const Transaction = sequelize.define('Transaction', {
  amount: { type: DataTypes.FLOAT, allowNull: false },
  type: { type: DataTypes.ENUM('income', 'expense'), allowNull: false },
  category: { type: DataTypes.STRING },
  date: { type: DataTypes.DATEONLY, allowNull: false },
  description: { type: DataTypes.STRING },
  userId: { type: DataTypes.INTEGER, references: { model: User, key: 'id' } },
});

User.hasMany(Transaction);
Transaction.belongsTo(User);

// JWT Middleware
const authenticate = (req, res, next) => {
  const token = req.headers['authorization'];
  if (!token) return res.status(401).send('Access Denied');
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(403).send('Invalid Token');
    req.user = user;
    next();
  });
};

// Routes
app.post('/register', async (req, res) => {
  const { username, password } = req.body;
  const hashedPassword = await bcrypt.hash(password, 10);
  try {
    const user = await User.create({ username, password: hashedPassword });
    res.status(201).json({ user });
  } catch (error) {
    res.status(400).send('Error registering user');
  }
});

app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  const user = await User.findOne({ where: { username } });
  if (!user) return res.status(400).send('User not found');
  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) return res.status(400).send('Invalid credentials');
  const token = jwt.sign({ id: user.id, username: user.username }, process.env.JWT_SECRET);
  res.json({ token });
});

app.get('/transactions', authenticate, async (req, res) => {
  const transactions = await Transaction.findAll({ where: { userId: req.user.id } });
  res.json(transactions);
});

app.post('/transactions', authenticate, async (req, res) => {
  const { amount, type, category, date, description } = req.body;
  const transaction = await Transaction.create({ amount, type, category, date, description, userId: req.user.id });
  res.status(201).json(transaction);
});

app.put('/transactions/:id', authenticate, async (req, res) => {
  const { amount, type, category, date, description } = req.body;
  const transaction = await Transaction.findByPk(req.params.id);
  if (transaction.userId !== req.user.id) return res.status(403).send('Forbidden');
  await transaction.update({ amount, type, category, date, description });
  res.json(transaction);
});

app.delete('/transactions/:id', authenticate, async (req, res) => {
  const transaction = await Transaction.findByPk(req.params.id);
  if (transaction.userId !== req.user.id) return res.status(403).send('Forbidden');
  await transaction.destroy();
  res.status(204).send();
});

// Start server
app.listen(5000, async () => {
  console.log('Server is running on port 5000');
  await sequelize.sync({ force: true });
});