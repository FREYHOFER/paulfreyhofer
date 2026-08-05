import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';

const root = process.cwd();
const payloadDir = path.join(root, 'site-payload');
const parts = fs.readdirSync(payloadDir)
  .filter((name) => /^part\d{3}\.txt$/.test(name))
  .sort();

const base64 = parts
  .map((name) => fs.readFileSync(path.join(payloadDir, name), 'utf8').trim())
  .join('');

const html = zlib.gunzipSync(Buffer.from(base64, 'base64'));
const distDir = path.join(root, 'dist');

fs.rmSync(distDir, { recursive: true, force: true });
fs.mkdirSync(distDir, { recursive: true });
fs.writeFileSync(path.join(distDir, 'index.html'), html);

console.log(`Built ${path.join('dist', 'index.html')} (${html.length} bytes) from ${parts.length} payload parts.`);
