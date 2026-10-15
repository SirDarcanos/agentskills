// Offline Pi skill-loader/Markdown check. Pass an existing Pi package directory.
// No session, model, extension, settings, credential or installation operations.
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const repo = path.resolve(here, '../../..');
const runtime = path.resolve(process.argv[2] || '');
assert(process.argv[2], 'Pass an existing installed Pi package directory; no auto-install');
const info = JSON.parse(fs.readFileSync(path.join(runtime, 'package.json'), 'utf8'));
assert.equal(info.name, '@earendil-works/pi-coding-agent');
const loaderPath = path.join(runtime, 'dist/core/skills.js');
const { loadSkills, formatSkillsForPrompt } = await import(pathToFileURL(loaderPath));
const { marked } = await import(pathToFileURL(path.join(runtime, 'node_modules/marked/lib/marked.esm.js')));
const sha = data => createHash('sha256').update(data).digest('hex');
const scratch = fs.mkdtempSync(path.join(os.tmpdir(), 'composable-pi-loader-'));
const options = skillPaths => ({ cwd: scratch, agentDir: path.join(scratch, 'empty-agent'),
  skillPaths, includeDefaults: false });
const records = [];
try {
  const packages = ['workflow', 'writing', 'models'].flatMap(group =>
    fs.readdirSync(path.join(repo, group), { withFileTypes: true })
      .filter(entry => entry.isDirectory() && fs.existsSync(path.join(repo, group, entry.name, 'SKILL.md')))
      .map(entry => ({ name: entry.name, relative: `${group}/${entry.name}` })))
    .sort((a, b) => a.name.localeCompare(b.name));
  assert(packages.length > 0, 'no skill packages discovered');
  const names = packages.map(item => item.name);
  assert.equal(new Set(names).size, names.length, 'duplicate source skill names');
  const copies = [];
  for (const [index, { name, relative }] of packages.entries()) {
    const source = path.join(repo, relative);
    const copy = path.join(scratch, `location-${index}`, name);
    fs.cpSync(source, copy, { recursive: true, dereference: false });
    copies.push(copy);
    const result = loadSkills(options([copy]));
    assert.deepEqual(result.diagnostics, [], name);
    assert.equal(result.skills.length, 1, name);
    const skill = result.skills[0];
    assert.equal(skill.name, name);
    assert.equal(skill.filePath, path.join(copy, 'SKILL.md'));
    assert.equal(sha(fs.readFileSync(skill.filePath)), sha(fs.readFileSync(path.join(source, 'SKILL.md'))));
    const prompt = formatSkillsForPrompt(result.skills);
    assert.equal(prompt.includes(`<name>${name}</name>`), !skill.disableModelInvocation);
    records.push({ name, commandOnly: skill.disableModelInvocation,
      entry_sha256: sha(fs.readFileSync(skill.filePath)), diagnostics: [],
      resolved: `<isolated>/location-${index}/${name}/SKILL.md` });
  }
  const aggregate = loadSkills(options(copies));
  assert.equal(aggregate.skills.length, names.length);
  assert.deepEqual(aggregate.diagnostics, []);
  // Real loader collision semantics: first source wins with a diagnostic.
  const duplicate = path.join(scratch, 'duplicate', names[0]);
  fs.cpSync(copies[0], duplicate, { recursive: true });
  const collision = loadSkills(options([copies[0], duplicate]));
  assert.equal(collision.skills.length, 1);
  assert.equal(collision.skills[0].filePath, path.join(copies[0], 'SKILL.md'));
  assert(collision.diagnostics.some(item => item.type === 'collision'));
  const bad = path.join(scratch, 'invalid');
  fs.mkdirSync(bad);
  fs.writeFileSync(path.join(bad, 'SKILL.md'), '---\nname: invalid\n---\n# Missing description\n');
  const invalid = loadSkills(options([bad]));
  assert.equal(invalid.skills.length, 0);
  assert(invalid.diagnostics.length > 0);
  const missing = loadSkills(options([path.join(scratch, 'absent')]));
  assert.equal(missing.skills.length, 0);
  assert(missing.diagnostics.length > 0);
  const rendering = [];
  const documents = ['README.md', 'docs/design/composable-delivery-validation.md',
    'docs/validation/composable-acceptance/README.md',
    ...packages.flatMap(({ relative }) => [`${relative}/SKILL.md`, `${relative}/README.md`])];
  for (const relative of documents) {
    const raw = fs.readFileSync(path.join(repo, relative), 'utf8');
    const body = raw.replace(/^---\r?\n[\s\S]*?\r?\n---\r?\n/, '');
    const html = marked.parse(body);
    assert(html.includes('<h1'), relative);
    rendering.push({ path: relative, sha256: sha(raw), headings: (html.match(/<h[1-6]/g) || []).length,
      tables: (html.match(/<table>/g) || []).length });
    if (relative === 'docs/validation/composable-acceptance/README.md') {
      assert(html.includes('<table>') && html.includes('AC16'), 'acceptance table rendering');
    }
  }
  fs.mkdirSync(path.join(here, 'results'), { recursive: true });
  fs.writeFileSync(path.join(here, 'results/pi.json'), JSON.stringify({ node: process.version,
    runtime: { name: info.name, version: info.version, loader_sha256: sha(fs.readFileSync(loaderPath)) },
    packages: records, collision: 'first wins, diagnostic emitted', invalid: 'not loaded, diagnostic',
    missing: 'not loaded, diagnostic', rendering,
    limits: 'Explicit-path Pi loader only; no installed CLI, command expansion or semantic invocation' }, null, 2) + '\n');
  console.log(`${records.length} isolated Pi loader entries; collision/invalid/missing checks passed; ${rendering.length} Markdown documents rendered.`);
} finally {
  fs.rmSync(scratch, { recursive: true, force: true });
}
