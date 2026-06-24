# Audit Tools Reference

Use this reference only after the skill triggers.

## OSV Scanner

Check:

```bash
command -v osv-scanner
osv-scanner --version
```

Default scan:

```bash
osv-scanner scan source -r .
```

If missing, ask whether to install or continue with ecosystem-native audit only.

Install options:

- macOS: `brew install osv-scanner`
- Linux: `go install github.com/google/osv-scanner/cmd/osv-scanner@latest`, or use the official release binary when Go is unavailable
- Windows: `winget install Google.osv-scanner`, or use the official release binary when winget is unavailable

Treat installation as separate from vulnerability fix approval.

## Ecosystem Detection And Audit Commands

Prefer the package manager already used by the project. In dry-run, use audit commands that do not update manifests, lockfiles, dependency folders, or caches.

| Ecosystem | Detect | Dry-run audit | Dependency tree helpers |
| --- | --- | --- | --- |
| npm | `package-lock.json`, `package.json` with npm scripts | `npm audit --json` | `npm ls <pkg>`, `npm explain <pkg>` |
| pnpm | `pnpm-lock.yaml`, `pnpm-workspace.yaml` | `pnpm audit --json` | `pnpm why <pkg>` |
| Yarn Berry | `yarn.lock`, `.yarnrc.yml` | `yarn npm audit --json` | `yarn why <pkg>` |
| Yarn Classic | `yarn.lock` without Berry config | `yarn audit --json` | `yarn why <pkg>` |
| Bun | `bun.lock`, `bun.lockb` | `bun audit` when available | `bun pm ls` |
| Python pip | `requirements.txt`, `constraints.txt` | `pip-audit -r requirements.txt` | `pipdeptree -p <pkg>` |
| Python Poetry | `pyproject.toml`, `poetry.lock` | `poetry export --format requirements.txt` plus `pip-audit -r` on exported data when safe; otherwise report limitation | `poetry show --tree` |
| Python Pipenv | `Pipfile`, `Pipfile.lock` | `pipenv check` or `pip-audit` against exported requirements when safe | `pipenv graph` |
| Go | `go.mod`, `go.sum` | `govulncheck ./...` | `go mod why -m <module>`, `go list -m all` |
| Rust | `Cargo.toml`, `Cargo.lock` | `cargo audit` | `cargo tree -i <crate>` |
| Ruby | `Gemfile`, `Gemfile.lock` | `bundle audit` | `bundle info <gem>` |
| Maven | `pom.xml` | `mvn org.owasp:dependency-check-maven:check` when configured/available; otherwise report missing audit tooling | `mvn dependency:tree` |
| Gradle | `build.gradle`, `build.gradle.kts` | dependency-check plugin task when configured/available; otherwise report missing audit tooling | `gradle dependencies`, `gradle dependencyInsight` |
| .NET | `*.csproj`, `packages.lock.json` | `dotnet list package --vulnerable --include-transitive` | `dotnet list package --include-transitive` |

## Monorepo Signals

Scan and report scope when these exist:

- `workspaces` in `package.json`
- `pnpm-workspace.yaml`
- Yarn workspaces
- `turbo.json`, `nx.json`, `lerna.json`
- Cargo `[workspace]`
- multiple `go.mod` files
- Gradle multi-project builds

## Resolution Mechanisms

Use only as a last resort:

- npm `overrides`
- pnpm `overrides`
- Yarn `resolutions`
- Python constraints
- Go `replace`
- Cargo `[patch]`
- Maven/Gradle forced versions or constraints

Before proposing one, explain why direct or parent dependency updates cannot remove the vulnerability.
