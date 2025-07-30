import express from 'express';
import cors from 'cors';
import compression from 'compression';
import dotenv from 'dotenv';
import cron from 'node-cron';
import path from 'path';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

import { initializeTelegramBot } from './bot/telegram.js';
import { monitorAllChains } from './bot/blockchain.js';
import { initializeDatabase } from './database/init.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(compression());
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public')));

// Initialize in-memory storage
await initializeDatabase();

console.log('🔧 ===== ENVIRONMENT CHECK =====');
console.log('🔧 TELEGRAM_BOT_TOKEN exists:', !!process.env.TELEGRAM_BOT_TOKEN);
console.log('🔧 TELEGRAM_BOT_TOKEN length:', process.env.TELEGRAM_BOT_TOKEN?.length || 0);
console.log('🔧 TELEGRAM_BOT_TOKEN preview:', process.env.TELEGRAM_BOT_TOKEN?.substring(0, 30) + '...' || 'NOT SET');
console.log('🔧 NODE_ENV:', process.env.NODE_ENV);
console.log('🔧 PORT:', process.env.PORT);
console.log('🔧 DISABLE_BOT:', process.env.DISABLE_BOT);
console.log('🔧 Full token (first 50 chars):', process.env.TELEGRAM_BOT_TOKEN?.substring(0, 50) || 'NOT SET');
console.log('🔧 ===== END ENVIRONMENT CHECK =====');

// Initialize Telegram bot
console.log('🚀 Starting BuyXanBot initialization...');

// Check if bot should be disabled
const DISABLE_BOT = process.env.DISABLE_BOT === 'true' || false; // Bot enabled by default

if (DISABLE_BOT) {
  console.log('🚫 Bot is disabled via DISABLE_BOT environment variable');
} else {
  console.log('✅ Bot is enabled');
}

if (!process.env.TELEGRAM_BOT_TOKEN) {
  console.error('❌ TELEGRAM_BOT_TOKEN not found in environment');
  console.error('   Please check your .env file');
  console.error('   All env vars:', Object.keys(process.env).join(', '));
} else {
  console.log('✅ TELEGRAM_BOT_TOKEN found');
  
  if (!DISABLE_BOT) {
    try {
      console.log('🚀 Initializing Telegram bot...');
      await initializeTelegramBot();
      console.log('✅ Telegram bot initialization completed');
    } catch (error) {
      console.error('❌ Failed to initialize Telegram bot:', error.message);
      console.error('❌ Error stack:', error.stack);
    }
  } else {
    console.log('🚫 Skipping bot initialization (disabled)');
  }
}

// API Routes
app.get('/api/status', (req, res) => {
  res.json({ 
    status: 'running',
    timestamp: new Date().toISOString(),
    version: '1.0.0'
  });
});

// Telegram webhook endpoint
app.post('/api/telegram/webhook', async (req, res) => {
  try {
    console.log('🌐 Webhook endpoint hit - /api/telegram/webhook');
    const { handleTelegramWebhook } = await import('./bot/telegram.js');
    await handleTelegramWebhook(req.body);
    res.status(200).json({ success: true });
  } catch (error) {
    console.error('🌐 Webhook error:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// Admin API Routes
app.get('/api/admin/configs', async (req, res) => {
  try {
    const { getBotConfigs } = await import('./database/queries.js');
    const configs = await getBotConfigs();
    res.json(configs);
  } catch (error) {
    console.error('Error fetching configs:', error);
    res.status(500).json({ error: 'Failed to fetch configurations' });
  }
});

app.get('/api/admin/stats', async (req, res) => {
  try {
    const { getStats } = await import('./database/queries.js');
    const stats = await getStats();
    res.json(stats);
  } catch (error) {
    console.error('Error fetching stats:', error);
    res.status(500).json({ error: 'Failed to fetch statistics' });
  }
});

// Serve admin interface
app.get('/admin', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'admin.html'));
});

// Schedule blockchain monitoring (every 10 seconds for testing)
cron.schedule('*/10 * * * * *', async () => {
  console.log('🔍 Running scheduled blockchain monitoring...');
  try {
    await monitorAllChains();
  } catch (error) {
    console.error('❌ Monitoring error:', error.message);
  }
});

// Start server
app.listen(PORT, () => {
  console.log(`🚀 BuyXanBot server running on port ${PORT}`);
  console.log(`📊 Admin interface: http://localhost:${PORT}/admin`);
  console.log(`🌐 Main interface: http://localhost:${PORT}`);
  console.log(`🤖 Bot is running in POLLING mode - send /start to your Telegram bot!`);
  console.log(`🔍 Bot token configured: ${!!process.env.TELEGRAM_BOT_TOKEN}`);
});