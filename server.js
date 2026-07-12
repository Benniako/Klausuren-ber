import express from 'express';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
const PORT = 3000;

// Log incoming requests
app.use((req, res, next) => {
  console.log(`${new Date().toISOString()} - ${req.method} ${req.url}`);
  next();
});

// Serve static assets from all relevant folders containing reference materials
app.use('/bwl', express.static(path.join(__dirname, 'bwl')));
app.use('/vwl', express.static(path.join(__dirname, 'vwl')));
app.use('/Perso', express.static(path.join(__dirname, 'Perso')));
app.use('/mathe und statistik', express.static(path.join(__dirname, 'mathe und statistik')));
app.use('/wpr', express.static(path.join(__dirname, 'wpr')));
app.use('/Klausuren trainer data', express.static(path.join(__dirname, 'Klausuren trainer data')));

// Serve the main html file for the root path
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'Klausuren trainer data', 'klausuren-trainer.html'));
});

// Serve the main html file for /index.html
app.get('/index.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'Klausuren trainer data', 'klausuren-trainer.html'));
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({ status: 'ok', time: new Date() });
});

app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server running on http://0.0.0.0:${PORT}`);
});
