# Legacy Repository Migration — Clean Genesis (TASK-3708)

## Reason for clean migration

The prior ManualFC Git repository (`E:/ManualFC`) accumulated historical object-store
corruption over its development history. A three-stage investigation established
that this corruption cannot be repaired without either fabricating replacement
bytes or rewriting project history — both explicitly disallowed:

- **TASK-3702** — first discovery during the TASK-3701 brand migration commit;
  investigated read-only, found 12 corrupt/missing loose objects, verdict `BLOCKED`.
- **TASK-3706** — full re-investigation with a formal safety backup, exhaustive
  search of every local worktree, an independent `.gemini` history snapshot, and
  reflog/dangling-object avenues. No authoritative recovery source found for the
  real-history objects. Verdict `BLOCKED`.
- **TASK-3707** — repaired the *infrastructure* blocking full diagnosis (a corrupt
  index file in the `ManualFC-remediation` linked worktree, plus orphaned `.idx`
  files with no matching `.pack`), which let `git fsck --full` run to completion
  for the first time. This surfaced the true, complete inventory: **13** corrupt
  objects (12 blobs + 1 full commit root tree — more severe than previously known,
  since a whole historical snapshot's tree is unreadable, not just one file).
  Verdict `BLOCKED_NEEDS_HISTORY_REWRITE` — 6 of the 13 objects are reachable from
  `main`'s real history with no available authoritative source; the remaining 7
  belong only to an internal tooling checkpoint ref, not project history.

Critically, **current `HEAD` was confirmed healthy throughout all three
investigations** — the corruption affects only specific historical commits, never
the live, working, currently-checked-out product.

Given the constraints (no history rewrite, no fabricated bytes, but a fully
healthy current state), the correct resolution is a **clean genesis migration**:
preserve the damaged repository unmodified as a forensic archive, and start a new,
independent, fully healthy Git repository from an exact snapshot of the verified
current state.

## Legacy repository

- **Path:** `E:/ManualFC` (development halts here; retained as forensic archive)
- **Final healthy HEAD:** `57d7b60320e0e64a45871e884d90d6494741b4e5`
  (`feat(manualfc): integrate TASK-3702 through TASK-3705`)
- **Forensic `.git` backup:** `E:/ManualFC-git-backup-20260912/git-backup`
  (full copy taken before any TASK-3706/3707 repair activity; verified object/pack
  counts and `refs/heads/main` match the live legacy repo)
- **Quarantined artifacts:** `E:/ManualFC-git-backup-20260912/orphaned-idx-quarantine/`
  (the corrupt worktree index and the 4 orphaned `.idx` files removed during
  TASK-3707's infrastructure repair, preserved for forensic record)
- Full corruption inventory, classification, and recovery-attempt evidence:
  see the TASK-3702, TASK-3706, and TASK-3707 reports/reports-equivalent
  conversation record referenced in `DECISIONS.md`.

## Migration date

2026-09-13

## What this new repository is

- **Path:** `E:/ManualFC-clean`
- **Genesis commit:** `4fc3e528d8465f1d266cb663b3413c576d1fbca7`
  (`chore(manualfc): establish clean production baseline`)
- An **exact, verified snapshot** of legacy HEAD `57d7b60`'s tracked file tree —
  943 tracked files, every single one confirmed byte-identical via two independent
  methods: (1) `git hash-object` on each extracted file against the blob SHA
  recorded in the legacy tree, and (2) a direct `git ls-tree -r` comparison showing
  every mode/type/blob-SHA/path tuple identical between the legacy tree and this
  repository's genesis tree. **0 mismatches, 0 missing, 0 unexpected files.**
- A **completely independent Git object database** — no shared objects, no
  `objects/info/alternates` pointing at the legacy repository, no imported packs,
  refs, reflog entries, or checkpoint refs from the old repository.
- `git fsck --full` on this repository returns **completely clean** (no output,
  exit 0) — no corrupt objects, no missing objects, no dangling objects.

## What this new repository is explicitly NOT

- **Not a continuation of the old Git ancestry.** The genesis commit has no
  parent and does not descend from `57d7b60` or any other legacy commit SHA.
  Do not `git merge`/`git rebase` this repository against the legacy one expecting
  shared history — there is none by design.
- Not a rewrite of the legacy repository — the legacy repository was never
  modified by this migration.

## Going forward

All new ManualFC development happens in `E:/ManualFC-clean`. The legacy
repository (`E:/ManualFC`) is retained read-only as a forensic/historical
reference only — for looking up how something looked in old (readable) commits,
and for task provenance predating this migration. It should not receive further
commits.
