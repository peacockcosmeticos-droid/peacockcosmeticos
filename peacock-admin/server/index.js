import express from 'express';
import cors from 'cors';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcryptjs';
import multer from 'multer';
import fs from 'fs/promises';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = process.env.PORT || 3001;
const JWT_SECRET = process.env.JWT_SECRET || 'peacock-admin-secret-key-2025';

// Middleware
app.use(cors());
app.use(express.json());
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// Create uploads directory if it doesn't exist
const uploadsDir = path.join(__dirname, 'uploads');

async function initializeServer() {
  try {
    await fs.access(uploadsDir);
  } catch {
    await fs.mkdir(uploadsDir, { recursive: true });
  }
}

// File upload configuration
const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, uploadsDir);
  },
  filename: (req, file, cb) => {
    const uniqueSuffix = Date.now() + '-' + Math.round(Math.random() * 1E9);
    cb(null, file.fieldname + '-' + uniqueSuffix + path.extname(file.originalname));
  }
});

const upload = multer({
  storage: storage,
  limits: {
    fileSize: 50 * 1024 * 1024, // 50MB limit
  },
  fileFilter: (req, file, cb) => {
    const allowedTypes = /jpeg|jpg|png|webp|mp4|webm|ogg/;
    const extname = allowedTypes.test(path.extname(file.originalname).toLowerCase());
    const mimetype = allowedTypes.test(file.mimetype);

    if (mimetype && extname) {
      return cb(null, true);
    } else {
      cb(new Error('Only images and videos are allowed'));
    }
  }
});

// Default admin credentials (in production, this should be in a secure database)
const ADMIN_CREDENTIALS = {
  username: 'admin',
  password: '$2a$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi' // password: "PeacockAdmin2025!"
};

// Content storage paths
const CONTENT_FILE = path.join(__dirname, 'data', 'content.json');
const DATA_DIR = path.join(__dirname, 'data');

async function initializeData() {
  // Ensure data directory exists
  try {
    await fs.access(DATA_DIR);
  } catch {
    await fs.mkdir(DATA_DIR, { recursive: true });
  }

  // Initialize content file if it doesn't exist
  try {
    await fs.access(CONTENT_FILE);
  } catch {
  const initialContent = {
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
    socialMedia: {
      facebook: "https://www.facebook.com/profile.php?id=61555633298474",
      instagram: "https://www.instagram.com/peecockbr/",
      tiktok: "https://www.tiktok.com/@peecockcosmeticos?_t=ZM-8vMT8WL9Q9P&_r=1"
    },
    buyButtons: [
      {
        id: "header-buy",
        text: "Comprar agora",
        url: "#",
        location: "header"
      },
      {
        id: "main-cta-1",
        text: "Clique e compre já!",
        url: "#",
        location: "hero-section"
      },
      {
        id: "transform-cta",
        text: "Transforme seus cílios com Peecock!",
        url: "#",
        location: "results-section"
      },
      {
        id: "main-cta-2",
        text: "Clique e compre já!",
        url: "#",
        location: "benefits-section"
      },
      {
        id: "shipping-cta",
        text: "Compre a partir de duas unidades e ganhe <b>frete grátis!</b>",
        url: "#",
        location: "shipping-section"
      }
    ],
    mainHeadings: {
      hero: "Peecock:<br>o segredo por trás de cílios mais saudáveis, longos e volumosos!",
      whyChoose: "Por que escolher o sérum<br>de crescimento para cílios <span>Peecock?</span>",
      targetAudience: "O Sérum Peecock <span>é para você que:</span>",
      howToUse: "<span>Como usar</span> o sérum de crescimento para cílios?"
    },
    lastUpdated: new Date().toISOString(),
    version: "1.0.0"
  };

    await fs.writeFile(CONTENT_FILE, JSON.stringify(initialContent, null, 2));
  }
}

// Utility functions
const readContent = async () => {
  try {
    const data = await fs.readFile(CONTENT_FILE, 'utf8');
    return JSON.parse(data);
  } catch (error) {
    console.error('Error reading content:', error);
    throw new Error('Failed to read content');
  }
};

const writeContent = async (content) => {
  try {
    content.lastUpdated = new Date().toISOString();
    await fs.writeFile(CONTENT_FILE, JSON.stringify(content, null, 2));
    return content;
  } catch (error) {
    console.error('Error writing content:', error);
    throw new Error('Failed to save content');
  }
};

// Authentication middleware
const authenticateToken = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'Access token required' });
  }

  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ error: 'Invalid or expired token' });
    }
    req.user = user;
    next();
  });
};

// Routes

// Health check
app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date().toISOString() });
});

// Authentication
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

// Verify token
app.get('/api/auth/verify', authenticateToken, (req, res) => {
  res.json({ user: req.user });
});

// Content management
app.get('/api/content', async (req, res) => {
  try {
    const content = await readContent();
    res.json(content);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.get('/api/content/:section', async (req, res) => {
  try {
    const content = await readContent();
    const section = req.params.section;
    
    if (!content[section]) {
      return res.status(404).json({ error: 'Section not found' });
    }
    
    res.json(content[section]);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.put('/api/content/:section', authenticateToken, async (req, res) => {
  try {
    const content = await readContent();
    const section = req.params.section;
    
    if (!content.hasOwnProperty(section)) {
      return res.status(404).json({ error: 'Section not found' });
    }
    
    content[section] = req.body;
    const updatedContent = await writeContent(content);
    
    res.json({
      message: 'Content updated successfully',
      section: section,
      data: updatedContent[section]
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.put('/api/content', authenticateToken, async (req, res) => {
  try {
    const newContent = req.body;
    const updatedContent = await writeContent(newContent);
    
    res.json({
      message: 'All content updated successfully',
      data: updatedContent
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// File upload
app.post('/api/upload', authenticateToken, upload.single('file'), (req, res) => {
  try {
    if (!req.file) {
      return res.status(400).json({ error: 'No file uploaded' });
    }

    const fileUrl = `/uploads/${req.file.filename}`;
    
    res.json({
      message: 'File uploaded successfully',
      filename: req.file.filename,
      originalName: req.file.originalname,
      url: fileUrl,
      size: req.file.size,
      mimetype: req.file.mimetype
    });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Start server
async function startServer() {
  await initializeServer();
  await initializeData();

  app.listen(PORT, () => {
    console.log(`🚀 Peacock Admin Server running on port ${PORT}`);
    console.log(`📁 Content storage: ${CONTENT_FILE}`);
    console.log(`📂 Uploads directory: ${uploadsDir}`);
  });
}

startServer().catch(console.error);
