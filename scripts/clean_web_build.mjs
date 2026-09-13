import { rmSync } from 'node:fs';
import { resolve, sep } from 'node:path';

const output = resolve('dist', 'web');
const expectedSuffix = `${sep}dist${sep}web`;

if (!output.endsWith(expectedSuffix)) {
  throw new Error(`Refuz curățarea unui output neașteptat: ${output}`);
}

rmSync(output, { recursive: true, force: true });
