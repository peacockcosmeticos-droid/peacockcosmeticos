import express from 'express';
import cors from 'cors';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcryptjs';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3002;
const JWT_SECRET = process.env.JWT_SECRET || 'peacock-admin-secret-key-2025';

// Middleware
app.use(cors());
app.use(express.json());

// Default admin credentials
const ADMIN_CREDENTIALS = {
  username: 'admin',
  password: '$2a$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi' // password: "PeacockAdmin2025!"
};

// Content storage paths
const CONTENT_FILE = path.join(__dirname, 'data', 'content.json');
const DATA_DIR = path.join(__dirname, 'data');

// Simple content data
const defaultContent = {
  metadata: {
    title: "Peecock - Sérum vegano para crescimento de cílios",
    description: "Transforme seus cílios em apenas 7 dias com o sérum Peecock. Vegano, seguro e eficaz. Frete grátis para compras acima de R$140!",
    keywords: "sérum para cílios, crescimento de cílios, cílios longos, cílios volumosos, cosmético vegano, beleza natural, cuidados com cílios, Peecock",
    author: "Peecock Cosméticos",
    ogTitle: "Peecock - Sérum vegano para crescimento de cílios",
    ogDescription: "Transforme seus cílios em apenas 7 dias com o sérum Peecock. Vegano, seguro e eficaz. Frete grátis para compras acima de R$140!",
    twitterSite: "@peecockbr",
    twitterCreator: "@peecockbr"
  },
  company: {
    name: "Peecock Cosméticos",
    cnpj: "49.861.363/0001-00",
    address: "Rua Benjamin Constant, 2154 - Centro - Piracicaba - SP",
    email: "sac@peacockcosmeticos.com.br",
    phone: "+55-19-99999-9999"
  },
  buyButtons: [
    {
      id: "header-buy",
      text: "Comprar agora",
      url: "#",
      location: "header"
    }
  ],
  lastUpdated: new Date().toISOString(),
  version: "1.0.0"
};

// Routes
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

app.post('/api/auth/login', async (req, res) => {
  try {
    const { username, password } = req.body;

    if (!username || !password) {
      return res.status(400).json({ error: 'Username and password are required' });
    }

    if (username !== ADMIN_CREDENTIALS.username) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const isValidPassword = await bcrypt.compare(password, ADMIN_CREDENTIALS.password);
    if (!isValidPassword) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }

    const token = jwt.sign(
      { username: username, role: 'admin' },
      JWT_SECRET,
      { expiresIn: '24h' }
    );

    res.json({
      token,
      user: { username, role: 'admin' },
      expiresIn: '24h'
    });
  } catch (error) {
    console.error('Login error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

app.get('/api/content', (req, res) => {
  res.json(defaultContent);
});

// Initialize and start server
async function startServer() {
  try {
    // Create data directory if it doesn't exist
    try {
      await fs.access(DATA_DIR);
    } catch {
      await fs.mkdir(DATA_DIR, { recursive: true });
    }

    // Create content file if it doesn't exist
    try {
      await fs.access(CONTENT_FILE);
    } catch {
      await fs.writeFile(CONTENT_FILE, JSON.stringify(defaultContent, null, 2));
    }

    app.listen(PORT, () => {
      console.log(`🚀 Peacock Admin Server running on port ${PORT}`);
      console.log(`📁 Content storage: ${CONTENT_FILE}`);
      console.log(`🔗 Health check: http://localhost:${PORT}/api/health`);
    });
  } catch (error) {
    console.error('Failed to start server:', error);
  }
}

startServer();
